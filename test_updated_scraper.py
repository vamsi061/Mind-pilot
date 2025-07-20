#!/usr/bin/env python3
"""
Test script for the updated Movie AI Agent with correct search URLs
"""

from scraper import MovieScraper
import json
import time

def test_updated_scraper():
    """Test the updated scraper with correct search URLs"""
    print("🎬 Testing Updated Movie AI Agent")
    print("=" * 50)
    
    scraper = MovieScraper()
    
    # Test with a movie that should be available
    test_movie = "The Matrix"
    
    print(f"🔍 Testing search for: {test_movie}")
    print("-" * 30)
    
    try:
        # Search for the movie
        results = scraper.search_all_sites(test_movie)
        
        print(f"✅ Found {len(results)} results")
        
        if results:
            for i, result in enumerate(results, 1):
                print(f"\n  {i}. {result['title']}")
                print(f"     Site: {result['site']}")
                print(f"     URL: {result['url']}")
                print(f"     Streaming Links: {len(result['streaming_links'])}")
                
                for j, link in enumerate(result['streaming_links'], 1):
                    print(f"       {j}. {link['text']}")
                    print(f"          {link['url']}")
            
            # Save results to file
            with open('updated_test_results.json', 'w') as f:
                json.dump(results, f, indent=2)
            
            print(f"\n💾 Results saved to: updated_test_results.json")
        else:
            print("❌ No results found")
            
            # Let's try a different movie
            print("\n🔍 Trying with a different movie...")
            test_movie2 = "Avatar"
            results2 = scraper.search_all_sites(test_movie2)
            
            print(f"✅ Found {len(results2)} results for {test_movie2}")
            
            if results2:
                for i, result in enumerate(results2, 1):
                    print(f"\n  {i}. {result['title']}")
                    print(f"     Site: {result['site']}")
                    print(f"     URL: {result['url']}")
                    print(f"     Streaming Links: {len(result['streaming_links'])}")
                    
                    for j, link in enumerate(result['streaming_links'], 1):
                        print(f"       {j}. {link['text']}")
                        print(f"          {link['url']}")
        
    except Exception as e:
        print(f"❌ Error during test: {e}")
        import traceback
        traceback.print_exc()

def test_single_site():
    """Test a single site"""
    print("\n🎬 Testing single site")
    print("=" * 30)
    
    scraper = MovieScraper()
    
    # Test with MoviezWap first (seemed to work better in debug)
    from config import STREAMING_WEBSITES
    
    site_config = STREAMING_WEBSITES[1]  # MoviezWap
    movie_name = "The Matrix"
    
    print(f"🔍 Testing {site_config['name']} for: {movie_name}")
    
    try:
        results = scraper.search_movie_on_site(site_config, movie_name)
        
        print(f"✅ Found {len(results)} results from {site_config['name']}")
        
        for i, result in enumerate(results, 1):
            print(f"\n  {i}. {result['title']}")
            print(f"     URL: {result['url']}")
            print(f"     Streaming Links: {len(result['streaming_links'])}")
            
            for j, link in enumerate(result['streaming_links'], 1):
                print(f"       {j}. {link['text']}")
                print(f"          {link['url']}")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    print("🎬 Movie AI Agent - Updated Scraper Test")
    print("Testing with correct search URLs and parameters")
    print()
    
    # Test single site first
    test_single_site()
    
    print("\n" + "=" * 60)
    
    # Test all sites
    test_updated_scraper()
    
    print("\n✅ Test completed!")