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
            logger.info(f"Searching {site_name} for: {movie_name}")
            
            # First, get the main page to find the search form
            main_page = self.make_request(site_config['base_url'], use_selenium=True)
            if not main_page:
                return results
            
            soup = BeautifulSoup(main_page, 'html.parser')
            
            # Find search form and submit search
            search_form = soup.find('form', {'method': 'get'}) or soup.find('form', {'method': 'post'})
            if search_form:
                # Try to find search input
                search_input = search_form.find('input', {'name': 's'}) or search_form.find('input', {'type': 'search'}) or search_form.find('input', {'placeholder': lambda x: x and 'search' in x.lower()})
                
                if search_input:
                    # Construct search URL
                    search_query = quote(movie_name)
                    search_url = f"{site_config['base_url']}/?s={search_query}"
                    
                    logger.info(f"Searching {site_name} at: {search_url}")
                    
                    # Make search request
                    search_results = self.make_request(search_url, use_selenium=True)
                    if search_results:
                        # Parse search results
                        results_soup = BeautifulSoup(search_results, 'html.parser')
                        
                        # Extract movie links from search results
                        movie_links = self.extract_movie_links_from_search(results_soup, site_config)
                        
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

    def extract_movie_links_from_search(self, soup, site_config):
        """Extract movie links from search results page specifically for these sites"""
        links = []
        
        # Try multiple selectors for these specific sites
        selectors = [
            'article a[href*="/movie/"]',
            'article a[href*="/film/"]',
            '.movie-item a',
            '.film-item a',
            '.search-item a',
            '.post a[href*="/movie/"]',
            '.post a[href*="/film/"]',
            'h2 a',
            'h3 a',
            '.title a',
            '.movie-title a',
            'a[href*="/movie/"]',
            'a[href*="/film/"]'
        ]
        
        for selector in selectors:
            found_links = soup.select(selector)
            if found_links:
                for link in found_links:
                    href = link.get('href')
                    if href and not href.startswith('http'):
                        # Make sure it's a relative link to a movie page
                        if any(keyword in href.lower() for keyword in ['movie', 'film', 'watch', 'stream']):
                            links.append(href)
                if links:
                    break
        
        # If still no links, try a broader approach
        if not links:
            all_links = soup.find_all('a', href=True)
            for link in all_links:
                href = link.get('href', '')
                # Look for links that seem to be movie pages
                if (href and not href.startswith('http') and 
                    any(keyword in href.lower() for keyword in ['movie', 'film', 'watch', 'stream']) and
                    not any(keyword in href.lower() for keyword in ['category', 'tag', 'author', 'page'])):
                    links.append(href)
        
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
            'a[href*="embed"]',
            'a[href*="player"]',
            '.watch-link',
            '.stream-link',
            '.play-button',
            '.embed-link',
            'a[class*="watch"]',
            'a[class*="stream"]',
            'a[class*="play"]',
            'a[class*="embed"]',
            '.btn-watch',
            '.btn-stream',
            '.btn-play'
        ]
        
        for selector in link_selectors:
            links = soup.select(selector)
            for link in links:
                href = link.get('href')
                if href:
                    full_url = urljoin(site_config['base_url'], href)
                    if self.is_valid_streaming_url(full_url):
                        link_text = link.get_text().strip()
                        if not link_text:
                            link_text = link.get('title', '') or link.get('alt', '') or 'Watch Movie'
                        
                        streaming_links.append({
                            'url': full_url,
                            'text': link_text
                        })
        
        # Also look for iframe embeds which are common on these sites
        iframes = soup.find_all('iframe', src=True)
        for iframe in iframes:
            src = iframe.get('src')
            if src and self.is_valid_streaming_url(src):
                streaming_links.append({
                    'url': src,
                    'text': 'Direct Stream (Embedded Player)'
                })
        
        # Look for video sources
        video_tags = soup.find_all('video')
        for video in video_tags:
            sources = video.find_all('source')
            for source in sources:
                src = source.get('src')
                if src and self.is_valid_streaming_url(src):
                    streaming_links.append({
                        'url': src,
                        'text': 'Direct Video Stream'
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
            r'player',
            r'\.mp4',
            r'\.m3u8',
            r'\.webm',
            r'\.avi',
            r'\.mkv'
        ]
        
        # Also check for common streaming domains
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
            'streamcherry'
        ]
        
        url_lower = url.lower()
        
        # Check for streaming patterns
        has_streaming_pattern = any(re.search(pattern, url_lower) for pattern in streaming_patterns)
        
        # Check for streaming domains
        has_streaming_domain = any(domain in url_lower for domain in streaming_domains)
        
        # Check if it's a direct video file
        is_video_file = any(ext in url_lower for ext in ['.mp4', '.m3u8', '.webm', '.avi', '.mkv'])
        
        return has_streaming_pattern or has_streaming_domain or is_video_file
    
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