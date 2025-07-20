#!/usr/bin/env python3
"""
Test script for the updated Movie AI Agent with specific websites
"""

from scraper import MovieScraper
import json
import time

def test_specific_sites():
    """Test scraping on the specific websites"""
    print("🎬 Testing Movie AI Agent with 5MovieRulz and MoviezWap")
    print("=" * 60)
    
    scraper = MovieScraper()
    
    # Test movies
    test_movies = ["The Matrix", "Inception", "Avatar"]
    
    for movie in test_movies:
        print(f"\n🔍 Testing search for: {movie}")
        print("-" * 40)
        
        try:
            # Search for the movie
            results = scraper.search_all_sites(movie)
            
            print(f"✅ Found {len(results)} results")
            
            for i, result in enumerate(results, 1):
                print(f"\n  {i}. {result['title']}")
                print(f"     Site: {result['site']}")
                print(f"     URL: {result['url']}")
                print(f"     Streaming Links: {len(result['streaming_links'])}")
                
                for j, link in enumerate(result['streaming_links'], 1):
                    print(f"       {j}. {link['text']}")
                    print(f"          {link['url']}")
            
            # Save results to file
            with open(f'test_results_{movie.replace(" ", "_")}.json', 'w') as f:
                json.dump(results, f, indent=2)
            
            print(f"\n💾 Results saved to: test_results_{movie.replace(' ', '_')}.json")
            
        except Exception as e:
            print(f"❌ Error testing {movie}: {e}")
        
        print("\n" + "=" * 60)
        time.sleep(2)  # Be respectful to the websites

def test_single_site():
    """Test a single site"""
    print("🎬 Testing single site scraping")
    print("=" * 40)
    
    scraper = MovieScraper()
    
    # Test with 5MovieRulz
    from config import STREAMING_WEBSITES
    
    site_config = STREAMING_WEBSITES[0]  # 5MovieRulz
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

if __name__ == "__main__":
    print("🎬 Movie AI Agent - Scraping Test")
    print("Testing updated scraper with 5MovieRulz and MoviezWap")
    print()
    
    # Test single site first
    test_single_site()
    
    print("\n" + "=" * 60)
    print("Would you like to test all sites? (y/n): ", end="")
    
    try:
        response = input().strip().lower()
        if response in ['y', 'yes']:
            test_specific_sites()
    except KeyboardInterrupt:
        print("\n👋 Test interrupted")
    
    print("\n✅ Test completed!")