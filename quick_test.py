#!/usr/bin/env python3
"""
Quick test to verify the new sites are working
"""

from scraper import MovieScraper
from config import STREAMING_WEBSITES
import json

def quick_test():
    """Quick test of a few sites"""
    print("🎬 Quick Test - New Sites")
    print("=" * 40)
    
    scraper = MovieScraper()
    
    # Test a few key sites
    test_sites = ["iBOMMA", "MovieRulz", "JioRockers"]
    test_movie = "The Matrix"
    
    for site_name in test_sites:
        site_config = next((site for site in STREAMING_WEBSITES if site['name'] == site_name), None)
        
        if not site_config:
            print(f"❌ Site {site_name} not found")
            continue
            
        print(f"🔍 Testing {site_name}...")
        
        try:
            results = scraper.search_movie_on_site(site_config, test_movie)
            
            if results:
                print(f"✅ Found {len(results)} results")
                for i, result in enumerate(results[:1], 1):
                    print(f"  {i}. {result['title']}")
                    print(f"     Streaming Links: {len(result['streaming_links'])}")
            else:
                print("❌ No results")
                
        except Exception as e:
            print(f"❌ Error: {str(e)[:50]}...")
        
        print()

if __name__ == "__main__":
    quick_test()