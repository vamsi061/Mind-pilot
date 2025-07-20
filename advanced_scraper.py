#!/usr/bin/env python3
"""
Advanced Movie AI Agent with Selenium-based scraping for direct streaming URLs
"""

import json
import time
import re
import logging
from urllib.parse import urljoin, quote, urlparse
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import requests

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class AdvancedMovieScraper:
    def __init__(self):
        self.driver = None
        self.setup_driver()
        
    def setup_driver(self):
        """Setup Chrome driver with headless options"""
        try:
            chrome_options = Options()
            chrome_options.add_argument("--headless")
            chrome_options.add_argument("--no-sandbox")
            chrome_options.add_argument("--disable-dev-shm-usage")
            chrome_options.add_argument("--disable-gpu")
            chrome_options.add_argument("--window-size=1920,1080")
            chrome_options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
            chrome_options.add_argument("--disable-blink-features=AutomationControlled")
            chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
            chrome_options.add_experimental_option('useAutomationExtension', False)
            
            self.driver = webdriver.Chrome(options=chrome_options)
            self.driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
            logger.info("Chrome driver setup completed")
            
        except Exception as e:
            logger.error(f"Failed to setup Chrome driver: {e}")
            self.driver = None
    
    def close_driver(self):
        """Close the browser driver"""
        if self.driver:
            self.driver.quit()
            self.driver = None
    
    def search_movie(self, movie_name, language=None, year=None):
        """Search for movie across all configured sites"""
        results = []
        
        # Configure sites with their specific search patterns
        sites = [
            {
                "name": "MoviezWap",
                "base_url": "https://www.moviezwap.pink",
                "search_url": "https://www.moviezwap.pink/search.php",
                "search_param": "q",
                "results_selector": "a[href*='/movie/']",
                "streaming_selectors": [
                    "a[href*='watch']",
                    "a[href*='stream']",
                    "a[href*='play']",
                    "a[href*='embed']",
                    "iframe[src*='stream']",
                    "iframe[src*='embed']"
                ]
            },
            {
                "name": "5MovieRulz",
                "base_url": "https://www.5movierulz.rich",
                "search_url": "https://www.5movierulz.rich/search_movies",
                "search_param": "s",
                "results_selector": "a[href*='/movie/']",
                "streaming_selectors": [
                    "a[href*='watch']",
                    "a[href*='stream']",
                    "a[href*='play']",
                    "a[href*='embed']",
                    "iframe[src*='stream']",
                    "iframe[src*='embed']"
                ]
            }
        ]
        
        for site in sites:
            try:
                logger.info(f"Searching {site['name']} for: {movie_name}")
                site_results = self.search_site(site, movie_name, language, year)
                results.extend(site_results)
                time.sleep(2)  # Be respectful
                
            except Exception as e:
                logger.error(f"Error searching {site['name']}: {e}")
                continue
        
        return results
    
    def search_site(self, site_config, movie_name, language=None, year=None):
        """Search a specific site for movies"""
        results = []
        
        try:
            # Construct search query
            search_query = movie_name
            if year:
                search_query += f" {year}"
            if language:
                search_query += f" {language}"
            
            # Build search URL
            search_param = site_config['search_param']
            search_url = f"{site_config['search_url']}?{search_param}={quote(search_query)}"
            
            logger.info(f"Searching URL: {search_url}")
            
            # Navigate to search page
            self.driver.get(search_url)
            time.sleep(3)  # Wait for page to load
            
            # Wait for results to load
            try:
                WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, site_config['results_selector']))
                )
            except TimeoutException:
                logger.warning(f"No results found on {site_config['name']}")
                return results
            
            # Extract movie links
            movie_links = self.driver.find_elements(By.CSS_SELECTOR, site_config['results_selector'])
            
            for link in movie_links[:5]:  # Limit to first 5 results
                try:
                    href = link.get_attribute('href')
                    title = link.text.strip()
                    
                    if href and title:
                        logger.info(f"Found movie: {title}")
                        
                        # Get streaming URLs from movie page
                        streaming_urls = self.extract_streaming_urls(href, site_config)
                        
                        if streaming_urls:
                            results.append({
                                "title": title,
                                "language": language or "Unknown",
                                "quality": "HD",
                                "streaming_urls": streaming_urls,
                                "source": site_config['name'],
                                "movie_url": href
                            })
                
                except Exception as e:
                    logger.error(f"Error processing movie link: {e}")
                    continue
        
        except Exception as e:
            logger.error(f"Error searching site {site_config['name']}: {e}")
        
        return results
    
    def extract_streaming_urls(self, movie_url, site_config):
        """Extract actual streaming URLs from movie page"""
        streaming_urls = []
        
        try:
            logger.info(f"Extracting streaming URLs from: {movie_url}")
            
            # Navigate to movie page
            self.driver.get(movie_url)
            time.sleep(3)  # Wait for page to load
            
            # Wait for content to load
            try:
                WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.TAG_NAME, "body"))
                )
            except TimeoutException:
                logger.warning("Page load timeout")
                return streaming_urls
            
            # Look for streaming links
            for selector in site_config['streaming_selectors']:
                try:
                    elements = self.driver.find_elements(By.CSS_SELECTOR, selector)
                    
                    for element in elements:
                        if selector.startswith('iframe'):
                            src = element.get_attribute('src')
                            if src and self.is_streaming_url(src):
                                streaming_urls.append({
                                    "url": src,
                                    "type": "iframe",
                                    "text": "Embedded Player"
                                })
                        else:
                            href = element.get_attribute('href')
                            text = element.text.strip()
                            
                            if href and self.is_streaming_url(href):
                                streaming_urls.append({
                                    "url": href,
                                    "type": "direct",
                                    "text": text or "Stream"
                                })
                
                except Exception as e:
                    logger.error(f"Error with selector {selector}: {e}")
                    continue
            
            # Look for video sources
            video_elements = self.driver.find_elements(By.TAG_NAME, "video")
            for video in video_elements:
                sources = video.find_elements(By.TAG_NAME, "source")
                for source in sources:
                    src = source.get_attribute('src')
                    if src and self.is_streaming_url(src):
                        streaming_urls.append({
                            "url": src,
                            "type": "video",
                            "text": "Direct Video"
                        })
            
            # Look for embedded players in page source
            page_source = self.driver.page_source
            soup = BeautifulSoup(page_source, 'html.parser')
            
            # Find iframes with streaming content
            iframes = soup.find_all('iframe', src=True)
            for iframe in iframes:
                src = iframe.get('src')
                if src and self.is_streaming_url(src):
                    streaming_urls.append({
                        "url": src,
                        "type": "iframe",
                        "text": "Embedded Stream"
                    })
            
            # Look for direct video links in page source
            video_links = soup.find_all('a', href=True)
            for link in video_links:
                href = link.get('href')
                if href and self.is_streaming_url(href):
                    text = link.get_text().strip()
                    streaming_urls.append({
                        "url": href,
                        "type": "direct",
                        "text": text or "Video Link"
                    })
        
        except Exception as e:
            logger.error(f"Error extracting streaming URLs: {e}")
        
        return streaming_urls
    
    def is_streaming_url(self, url):
        """Check if URL is a streaming URL"""
        if not url:
            return False
        
        # Streaming patterns
        streaming_patterns = [
            r'\.m3u8',
            r'\.mp4',
            r'\.webm',
            r'\.avi',
            r'\.mkv',
            r'stream',
            r'embed',
            r'player',
            r'watch',
            r'play'
        ]
        
        # Streaming domains
        streaming_domains = [
            'youtube.com',
            'vimeo.com',
            'dailymotion.com',
            'streamable.com',
            'vidcloud',
            'vidstream',
            'streamango',
            'openload',
            'rapidvideo',
            'streamcherry',
            'gofile.io',
            'mega.nz',
            'drive.google.com'
        ]
        
        url_lower = url.lower()
        
        # Check for streaming patterns
        has_pattern = any(re.search(pattern, url_lower) for pattern in streaming_patterns)
        
        # Check for streaming domains
        has_domain = any(domain in url_lower for domain in streaming_domains)
        
        # Check for direct video files
        is_video_file = any(ext in url_lower for ext in ['.mp4', '.m3u8', '.webm', '.avi', '.mkv'])
        
        return has_pattern or has_domain or is_video_file
    
    def search_all_sites(self, movie_name, language=None, year=None):
        """Main search function"""
        try:
            results = self.search_movie(movie_name, language, year)
            
            if results:
                return {
                    "status": "success",
                    "results": results,
                    "total_found": len(results)
                }
            else:
                return {
                    "status": "not_found",
                    "message": f"No streaming URLs found for '{movie_name}'. Try searching with a different title.",
                    "results": []
                }
        
        except Exception as e:
            logger.error(f"Search error: {e}")
            return {
                "status": "error",
                "message": f"Error during search: {str(e)}",
                "results": []
            }
        
        finally:
            self.close_driver()

def main():
    """Main function for testing"""
    scraper = AdvancedMovieScraper()
    
    try:
        # Test search
        movie_name = "The Matrix"
        result = scraper.search_all_sites(movie_name)
        
        print(json.dumps(result, indent=2))
        
    except Exception as e:
        print(f"Error: {e}")
    
    finally:
        scraper.close_driver()

if __name__ == "__main__":
    main()