#!/usr/bin/env python3
"""
Debug script to analyze the HTML structure of target websites
"""

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, quote
import json
import time

def analyze_site_structure(site_url, movie_name):
    """Analyze the actual HTML structure of a site"""
    print(f"🔍 Analyzing {site_url}")
    print("=" * 50)
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    try:
        # Get main page
        print("📄 Getting main page...")
        response = requests.get(site_url, headers=headers, timeout=10)
        print(f"Status: {response.status_code}")
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Find search form
            print("\n🔍 Looking for search form...")
            forms = soup.find_all('form')
            print(f"Found {len(forms)} forms")
            
            for i, form in enumerate(forms):
                print(f"\nForm {i+1}:")
                print(f"  Method: {form.get('method', 'GET')}")
                print(f"  Action: {form.get('action', 'N/A')}")
                
                inputs = form.find_all('input')
                for inp in inputs:
                    print(f"    Input: {inp.get('name', 'N/A')} - {inp.get('type', 'text')}")
            
            # Try to search
            print(f"\n🔍 Searching for: {movie_name}")
            search_query = quote(movie_name)
            search_url = f"{site_url}/?s={search_query}"
            print(f"Search URL: {search_url}")
            
            search_response = requests.get(search_url, headers=headers, timeout=10)
            print(f"Search Status: {search_response.status_code}")
            
            if search_response.status_code == 200:
                search_soup = BeautifulSoup(search_response.text, 'html.parser')
                
                # Look for movie links
                print("\n🔍 Looking for movie links...")
                
                # Try different selectors
                selectors = [
                    'a[href*="/movie/"]',
                    'a[href*="/film/"]',
                    '.movie-item a',
                    '.film-item a',
                    'article a',
                    '.post a',
                    'h2 a',
                    'h3 a',
                    '.title a',
                    'a[href*="movie"]',
                    'a[href*="film"]'
                ]
                
                for selector in selectors:
                    links = search_soup.select(selector)
                    if links:
                        print(f"\n✅ Found {len(links)} links with selector: {selector}")
                        for j, link in enumerate(links[:3]):  # Show first 3
                            href = link.get('href')
                            text = link.get_text().strip()
                            print(f"  {j+1}. {text} -> {href}")
                        break
                else:
                    print("❌ No movie links found with any selector")
                
                # Look for any links that might be movies
                print("\n🔍 Looking for any potential movie links...")
                all_links = search_soup.find_all('a', href=True)
                movie_links = []
                
                for link in all_links:
                    href = link.get('href', '').lower()
                    text = link.get_text().strip()
                    if (href and not href.startswith('http') and 
                        any(keyword in href for keyword in ['movie', 'film', 'watch']) and
                        len(text) > 3):
                        movie_links.append((text, link.get('href')))
                
                if movie_links:
                    print(f"✅ Found {len(movie_links)} potential movie links:")
                    for text, href in movie_links[:5]:
                        print(f"  - {text} -> {href}")
                else:
                    print("❌ No potential movie links found")
                
                # Save HTML for manual inspection
                with open(f'debug_{site_url.replace("https://", "").replace("/", "_")}_search.html', 'w', encoding='utf-8') as f:
                    f.write(search_response.text)
                print(f"\n💾 Saved search page HTML to debug_{site_url.replace('https://', '').replace('/', '_')}_search.html")
                
            else:
                print(f"❌ Search failed with status: {search_response.status_code}")
        
        else:
            print(f"❌ Failed to get main page: {response.status_code}")
            
    except Exception as e:
        print(f"❌ Error analyzing {site_url}: {e}")

def analyze_movie_page(movie_url):
    """Analyze a specific movie page for streaming links"""
    print(f"\n🎬 Analyzing movie page: {movie_url}")
    print("=" * 50)
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    try:
        response = requests.get(movie_url, headers=headers, timeout=10)
        print(f"Status: {response.status_code}")
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Look for streaming links
            print("\n🔍 Looking for streaming links...")
            
            streaming_selectors = [
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
            
            found_links = []
            for selector in streaming_selectors:
                links = soup.select(selector)
                if links:
                    print(f"\n✅ Found {len(links)} links with selector: {selector}")
                    for link in links:
                        href = link.get('href')
                        text = link.get_text().strip()
                        if href:
                            found_links.append((text, href))
                            print(f"  - {text} -> {href}")
            
            # Look for iframes
            print("\n🔍 Looking for iframe embeds...")
            iframes = soup.find_all('iframe', src=True)
            if iframes:
                print(f"✅ Found {len(iframes)} iframes:")
                for iframe in iframes:
                    src = iframe.get('src')
                    print(f"  - {src}")
            
            # Look for video tags
            print("\n🔍 Looking for video tags...")
            videos = soup.find_all('video')
            if videos:
                print(f"✅ Found {len(videos)} video tags:")
                for video in videos:
                    sources = video.find_all('source')
                    for source in sources:
                        src = source.get('src')
                        if src:
                            print(f"  - {src}")
            
            # Save HTML for manual inspection
            with open(f'debug_movie_page.html', 'w', encoding='utf-8') as f:
                f.write(response.text)
            print(f"\n💾 Saved movie page HTML to debug_movie_page.html")
            
            return found_links
        else:
            print(f"❌ Failed to get movie page: {response.status_code}")
            
    except Exception as e:
        print(f"❌ Error analyzing movie page: {e}")
    
    return []

if __name__ == "__main__":
    sites = [
        "https://www.5movierulz.rich",
        "https://www.moviezwap.pink"
    ]
    
    test_movie = "The Matrix"
    
    for site in sites:
        analyze_site_structure(site, test_movie)
        print("\n" + "="*80 + "\n")
        time.sleep(2)  # Be respectful
    
    print("🔍 Debug analysis complete!")
    print("Check the saved HTML files for manual inspection.")