#!/usr/bin/env python3
"""
Comprehensive test script for all streaming sites in the Movie AI Agent
"""

from scraper import MovieScraper
from config import STREAMING_WEBSITES
import json
import time
from datetime import datetime

def test_all_sites():
    """Test all configured streaming sites"""
    print("🎬 Movie AI Agent - All Sites Test")
    print("=" * 60)
    print(f"📅 Test started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"🔍 Testing {len(STREAMING_WEBSITES)} sites")
    print()
    
    scraper = MovieScraper()
    test_movies = ["The Matrix", "Avatar", "Inception"]
    
    all_results = {}
    
    for movie in test_movies:
        print(f"🎬 Testing movie: {movie}")
        print("-" * 40)
        
        movie_results = []
        
        for site_config in STREAMING_WEBSITES:
            if not site_config.get('enabled', True):
                continue
                
            site_name = site_config['name']
            print(f"  🔍 Testing {site_name}...", end=" ")
            
            try:
                results = scraper.search_movie_on_site(site_config, movie)
                
                if results:
                    print(f"✅ Found {len(results)} results")
                    movie_results.extend(results)
                    
                    # Show first result details
                    if results:
                        first_result = results[0]
                        print(f"     📺 {first_result['title']}")
                        print(f"     🔗 {first_result['url']}")
                        print(f"     🎥 {len(first_result['streaming_links'])} streaming links")
                else:
                    print("❌ No results")
                    
            except Exception as e:
                print(f"❌ Error: {str(e)[:50]}...")
            
            # Be respectful with delays
            time.sleep(site_config.get('delay', 2))
        
        all_results[movie] = movie_results
        print(f"\n📊 Total results for '{movie}': {len(movie_results)}")
        print()
    
    # Save comprehensive results
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    filename = f'comprehensive_test_results_{timestamp}.json'
    
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(all_results, f, indent=2, ensure_ascii=False)
    
    print("📊 Summary Report")
    print("=" * 40)
    
    total_results = 0
    for movie, results in all_results.items():
        print(f"🎬 {movie}: {len(results)} results")
        total_results += len(results)
        
        # Show top sites for this movie
        site_counts = {}
        for result in results:
            site = result['site']
            site_counts[site] = site_counts.get(site, 0) + 1
        
        top_sites = sorted(site_counts.items(), key=lambda x: x[1], reverse=True)[:3]
        if top_sites:
            print(f"   Top sites: {', '.join([f'{site} ({count})' for site, count in top_sites])}")
    
    print(f"\n📈 Total results across all movies: {total_results}")
    print(f"💾 Detailed results saved to: {filename}")
    
    return all_results

def test_specific_sites():
    """Test specific sites that are known to work well"""
    print("\n🎯 Testing Specific High-Value Sites")
    print("=" * 40)
    
    scraper = MovieScraper()
    
    # Focus on sites that typically have good results
    priority_sites = [
        "iBOMMA",
        "MovieRulz", 
        "MoviezWap",
        "JioRockers",
        "1337x"
    ]
    
    test_movie = "The Matrix"
    
    for site_name in priority_sites:
        site_config = next((site for site in STREAMING_WEBSITES if site['name'] == site_name), None)
        
        if not site_config:
            print(f"❌ Site {site_name} not found in configuration")
            continue
            
        print(f"🔍 Testing {site_name} for '{test_movie}'...")
        
        try:
            results = scraper.search_movie_on_site(site_config, test_movie)
            
            if results:
                print(f"✅ Found {len(results)} results")
                
                for i, result in enumerate(results[:2], 1):  # Show first 2 results
                    print(f"  {i}. {result['title']}")
                    print(f"     URL: {result['url']}")
                    print(f"     Streaming Links: {len(result['streaming_links'])}")
                    
                    for j, link in enumerate(result['streaming_links'][:3], 1):  # Show first 3 links
                        print(f"       {j}. {link['text']}")
                        print(f"          {link['url']}")
            else:
                print("❌ No results found")
                
        except Exception as e:
            print(f"❌ Error: {e}")
        
        print()

def generate_site_status_report():
    """Generate a status report for all sites"""
    print("\n📋 Site Status Report")
    print("=" * 30)
    
    enabled_sites = [site for site in STREAMING_WEBSITES if site.get('enabled', True)]
    disabled_sites = [site for site in STREAMING_WEBSITES if not site.get('enabled', True)]
    
    print(f"✅ Enabled sites: {len(enabled_sites)}")
    for site in enabled_sites:
        print(f"  - {site['name']} ({site['base_url']})")
    
    if disabled_sites:
        print(f"\n❌ Disabled sites: {len(disabled_sites)}")
        for site in disabled_sites:
            print(f"  - {site['name']} ({site['base_url']})")
    
    print(f"\n🔧 Configuration Summary:")
    print(f"  - Total sites configured: {len(STREAMING_WEBSITES)}")
    print(f"  - Sites with 'q' parameter: {len([s for s in enabled_sites if s.get('search_param') == 'q'])}")
    print(f"  - Sites with 's' parameter: {len([s for s in enabled_sites if s.get('search_param') == 's'])}")

if __name__ == "__main__":
    print("🎬 Movie AI Agent - Comprehensive Site Testing")
    print("Testing all configured streaming sites for movie search and streaming URL extraction")
    print()
    
    # Generate site status report
    generate_site_status_report()
    
    print("\n" + "=" * 60)
    
    # Test specific high-value sites first
    test_specific_sites()
    
    print("\n" + "=" * 60)
    
    # Test all sites
    all_results = test_all_sites()
    
    print("\n✅ Comprehensive testing completed!")
    print("🎯 The Movie AI Agent is now configured with all requested streaming sites.")
    print("🌐 Visit the web interface to search for movies across all these platforms.")