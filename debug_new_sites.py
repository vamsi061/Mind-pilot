#!/usr/bin/env python3
"""
Debug script to analyze the actual HTML structure of the new streaming sites
"""

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, quote
import json
import time

def analyze_site_structure(site_url, movie_name, search_param="q"):
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
            
            # Try different search URL patterns
            search_patterns = [
                f"{site_url}/?{search_param}=",
                f"{site_url}/search?{search_param}=",
                f"{site_url}/search/?{search_param}=",
                f"{site_url}/?s=",
                f"{site_url}/search?s=",
                f"{site_url}/search/?s="
            ]
            
            for pattern in search_patterns:
                search_query = quote(movie_name)
                search_url = f"{pattern}{search_query}"
                print(f"\n🔍 Trying search URL: {search_url}")
                
                try:
                    search_response = requests.get(search_url, headers=headers, timeout=10)
                    print(f"Search Status: {search_response.status_code}")
                    
                    if search_response.status_code == 200:
                        search_soup = BeautifulSoup(search_response.text, 'html.parser')
                        
                        # Look for movie links with various selectors
                        selectors_to_try = [
                            'a[href*="/movie/"]',
                            'a[href*="/film/"]',
                            'a[href*="/torrent/"]',
                            '.movie-item a',
                            '.film-item a',
                            '.search-item a',
                            'article a',
                            '.post a',
                            'h2 a',
                            'h3 a',
                            '.title a',
                            '.movie-title a',
                            'a[href*="movie"]',
                            'a[href*="film"]',
                            'a[href*="torrent"]',
                            '.name a',  # For 1337x
                            '.torrent-name a'  # For torrent sites
                        ]
                        
                        found_links = []
                        for selector in selectors_to_try:
                            links = search_soup.select(selector)
                            if links:
                                print(f"\n✅ Found {len(links)} links with selector: {selector}")
                                for j, link in enumerate(links[:3]):  # Show first 3
                                    href = link.get('href')
                                    text = link.get_text().strip()
                                    print(f"  {j+1}. {text} -> {href}")
                                    found_links.append((text, href))
                                break
                        
                        if not found_links:
                            print("❌ No movie links found with any selector")
                            
                            # Look for any links that might be movies
                            print("\n🔍 Looking for any potential movie links...")
                            all_links = search_soup.find_all('a', href=True)
                            movie_links = []
                            
                            for link in all_links:
                                href = link.get('href', '')
                                text = link.get_text().strip()
                                if (href and len(text) > 3 and 
                                    not href.startswith('http') and
                                    not any(keyword in href.lower() for keyword in ['category', 'tag', 'author', 'page', 'home', 'about'])):
                                    movie_links.append((text, href))
                            
                            if movie_links:
                                print(f"✅ Found {len(movie_links)} potential movie links:")
                                for text, href in movie_links[:5]:
                                    print(f"  - {text} -> {href}")
                        
                        # Save HTML for manual inspection
                        filename = f'debug_{site_url.replace("https://", "").replace("/", "_")}_search.html'
                        with open(filename, 'w', encoding='utf-8') as f:
                            f.write(search_response.text)
                        print(f"\n💾 Saved search page HTML to {filename}")
                        
                        if found_links:
                            return found_links
                            
                except Exception as e:
                    print(f"❌ Error with search URL {search_url}: {e}")
                    continue
        else:
            print(f"❌ Failed to get main page: {response.status_code}")
            
    except Exception as e:
        print(f"❌ Error analyzing {site_url}: {e}")
    
    return []

def test_specific_sites():
    """Test specific sites that should work"""
    sites_to_test = [
        ("https://www.ibomma.art", "q"),
        ("https://www.movierulz.art", "s"),
        ("https://www.jiorockers.art", "s"),
        ("https://www.1337x.to", "q")
    ]
    
    test_movie = "The Matrix"
    
    for site_url, search_param in sites_to_test:
        print(f"\n{'='*80}")
        results = analyze_site_structure(site_url, test_movie, search_param)
        if results:
            print(f"✅ Successfully found {len(results)} results from {site_url}")
        else:
            print(f"❌ No results found from {site_url}")
        time.sleep(2)  # Be respectful

if __name__ == "__main__":
    print("🔍 Debug Analysis of New Streaming Sites")
    print("Analyzing why the scraper isn't finding movies")
    print()
    
    test_specific_sites()
    
    print("\n✅ Debug analysis complete!")
    print("Check the saved HTML files for manual inspection.")