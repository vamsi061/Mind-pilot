import requests
import time
import random
import json
import re
from urllib.parse import urljoin, urlparse, quote
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, WebDriverException
from webdriver_manager.chrome import ChromeDriverManager
from config import STREAMING_WEBSITES, USER_AGENTS, REQUEST_TIMEOUT, MAX_RETRIES, REQUEST_DELAY
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class MovieScraper:
    def __init__(self):
        self.session = requests.Session()
        self.ua = UserAgent()
        self.driver = None
        self.setup_session()
    
    def setup_session(self):
        """Setup the requests session with headers and retry strategy"""
        self.session.headers.update({
            'User-Agent': random.choice(USER_AGENTS),
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
        })
    
    def setup_selenium_driver(self):
        """Setup Selenium WebDriver for JavaScript-heavy sites"""
        try:
            chrome_options = Options()
            chrome_options.add_argument('--headless')
            chrome_options.add_argument('--no-sandbox')
            chrome_options.add_argument('--disable-dev-shm-usage')
            chrome_options.add_argument('--disable-gpu')
            chrome_options.add_argument('--window-size=1920,1080')
            chrome_options.add_argument(f'--user-agent={random.choice(USER_AGENTS)}')
            
            self.driver = webdriver.Chrome(
                service=webdriver.chrome.service.Service(ChromeDriverManager().install()),
                options=chrome_options
            )
            return True
        except Exception as e:
            logger.error(f"Failed to setup Selenium driver: {e}")
            return False
    
    def close_selenium_driver(self):
        """Close Selenium WebDriver"""
        if self.driver:
            try:
                self.driver.quit()
            except:
                pass
            self.driver = None
    
    def make_request(self, url, use_selenium=False):
        """Make HTTP request with retry logic"""
        for attempt in range(MAX_RETRIES):
            try:
                if use_selenium and self.driver:
                    self.driver.get(url)
                    time.sleep(3)  # Wait for page to load
                    return self.driver.page_source
                else:
                    response = self.session.get(url, timeout=REQUEST_TIMEOUT)
                    response.raise_for_status()
                    return response.text
            except Exception as e:
                logger.warning(f"Attempt {attempt + 1} failed for {url}: {e}")
                if attempt < MAX_RETRIES - 1:
                    time.sleep(REQUEST_DELAY * (attempt + 1))
                else:
                    logger.error(f"All attempts failed for {url}")
                    return None
    
    def search_movie_on_site(self, site_config, movie_name):
        """Search for a movie on a specific streaming site"""
        results = []
        site_name = site_config['name']
        
        try:
            # Construct search URL
            search_query = quote(movie_name)
            search_url = f"{site_config['search_url']}{search_query}"
            
            logger.info(f"Searching {site_name} for: {movie_name}")
            
            # Make request
            html_content = self.make_request(search_url, use_selenium=True)
            if not html_content:
                return results
            
            # Parse results
            soup = BeautifulSoup(html_content, 'html.parser')
            
            # Extract movie links (this will vary by site)
            movie_links = self.extract_movie_links(soup, site_config)
            
            for link in movie_links[:5]:  # Limit to first 5 results
                movie_url = urljoin(site_config['base_url'], link)
                movie_info = self.extract_movie_info(movie_url, site_config)
                if movie_info:
                    results.append(movie_info)
            
            time.sleep(site_config.get('delay', 2))
            
        except Exception as e:
            logger.error(f"Error searching {site_name}: {e}")
        
        return results
    
    def extract_movie_links(self, soup, site_config):
        """Extract movie links from search results page"""
        links = []
        site_name = site_config['name'].lower()
        
        # Common selectors for movie links
        selectors = [
            'a[href*="/movie/"]',
            'a[href*="/film/"]',
            '.movie-item a',
            '.film-item a',
            '.search-item a',
            'a[class*="movie"]',
            'a[class*="film"]'
        ]
        
        for selector in selectors:
            found_links = soup.select(selector)
            if found_links:
                links.extend([link.get('href') for link in found_links if link.get('href')])
                break
        
        # If no links found with selectors, try to find any links that might be movies
        if not links:
            all_links = soup.find_all('a', href=True)
            for link in all_links:
                href = link.get('href', '').lower()
                if any(keyword in href for keyword in ['movie', 'film', 'watch']):
                    links.append(link.get('href'))
        
        return list(set(links))  # Remove duplicates
    
    def extract_movie_info(self, movie_url, site_config):
        """Extract movie information and streaming links from movie page"""
        try:
            html_content = self.make_request(movie_url, use_selenium=True)
            if not html_content:
                return None
            
            soup = BeautifulSoup(html_content, 'html.parser')
            
            # Extract movie title
            title = self.extract_title(soup, site_config)
            
            # Extract streaming links
            streaming_links = self.extract_streaming_links(soup, site_config)
            
            if title and streaming_links:
                return {
                    'title': title,
                    'url': movie_url,
                    'site': site_config['name'],
                    'streaming_links': streaming_links
                }
            
        except Exception as e:
            logger.error(f"Error extracting movie info from {movie_url}: {e}")
        
        return None
    
    def extract_title(self, soup, site_config):
        """Extract movie title from page"""
        title_selectors = [
            'h1',
            '.movie-title',
            '.film-title',
            '.title',
            '[class*="title"]'
        ]
        
        for selector in title_selectors:
            title_elem = soup.select_one(selector)
            if title_elem:
                return title_elem.get_text().strip()
        
        return None
    
    def extract_streaming_links(self, soup, site_config):
        """Extract streaming links from movie page"""
        streaming_links = []
        
        # Common selectors for streaming links
        link_selectors = [
            'a[href*="watch"]',
            'a[href*="stream"]',
            'a[href*="play"]',
            '.watch-link',
            '.stream-link',
            '.play-button',
            'a[class*="watch"]',
            'a[class*="stream"]'
        ]
        
        for selector in link_selectors:
            links = soup.select(selector)
            for link in links:
                href = link.get('href')
                if href:
                    full_url = urljoin(site_config['base_url'], href)
                    if self.is_valid_streaming_url(full_url):
                        streaming_links.append({
                            'url': full_url,
                            'text': link.get_text().strip() or 'Watch Movie'
                        })
        
        return streaming_links
    
    def is_valid_streaming_url(self, url):
        """Check if URL is a valid streaming URL"""
        if not url:
            return False
        
        # Check for common streaming URL patterns
        streaming_patterns = [
            r'watch',
            r'stream',
            r'play',
            r'video',
            r'embed',
            r'player'
        ]
        
        url_lower = url.lower()
        return any(re.search(pattern, url_lower) for pattern in streaming_patterns)
    
    def search_all_sites(self, movie_name):
        """Search for movie across all configured streaming sites"""
        all_results = []
        
        # Setup Selenium driver for JavaScript-heavy sites
        self.setup_selenium_driver()
        
        try:
            for site_config in STREAMING_WEBSITES:
                if not site_config.get('enabled', True):
                    continue
                
                site_results = self.search_movie_on_site(site_config, movie_name)
                all_results.extend(site_results)
                
                # Add delay between sites to be respectful
                time.sleep(random.uniform(1, 3))
        
        finally:
            self.close_selenium_driver()
        
        return all_results
    
    def validate_streaming_urls(self, results):
        """Validate and test streaming URLs"""
        validated_results = []
        
        for result in results:
            validated_links = []
            for link in result['streaming_links']:
                if self.test_streaming_url(link['url']):
                    validated_links.append(link)
            
            if validated_links:
                result['streaming_links'] = validated_links
                validated_results.append(result)
        
        return validated_results
    
    def test_streaming_url(self, url):
        """Test if a streaming URL is accessible"""
        try:
            response = self.session.head(url, timeout=5, allow_redirects=True)
            return response.status_code == 200
        except:
            return False