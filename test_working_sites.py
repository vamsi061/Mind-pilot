#!/usr/bin/env python3
"""
Test script for the working sites in the updated Movie AI Agent
"""

from scraper import MovieScraper
from config import STREAMING_WEBSITES
import json
import time

def test_working_sites():
    """Test the sites that are enabled and should work"""
    print("🎬 Testing Working Sites")
    print("=" * 40)
    
    scraper = MovieScraper()
    
    # Get only enabled sites
    enabled_sites = [site for site in STREAMING_WEBSITES if site.get('enabled', True)]
    
    print(f"🔍 Testing {len(enabled_sites)} enabled sites")
    print()
    
    test_movie = "The Matrix"
    all_results = []
    
    for site_config in enabled_sites:
        site_name = site_config['name']
        print(f"🔍 Testing {site_name}...", end=" ")
        
        try:
            results = scraper.search_movie_on_site(site_config, test_movie)
            
            if results:
                print(f"✅ Found {len(results)} results")
                all_results.extend(results)
                
                # Show first result details
                if results:
                    first_result = results[0]
                    print(f"     📺 {first_result['title']}")
                    print(f"     🔗 {first_result['url']}")
                    print(f"     🎥 {len(first_result['streaming_links'])} streaming links")
                    
                    # Show first few streaming links
                    for i, link in enumerate(first_result['streaming_links'][:3], 1):
                        print(f"       {i}. {link['text']}")
                        print(f"          {link['url']}")
            else:
                print("❌ No results")
                
        except Exception as e:
            print(f"❌ Error: {str(e)[:50]}...")
        
        print()
        time.sleep(site_config.get('delay', 2))  # Be respectful
    
    # Save results
    with open('working_sites_test_results.json', 'w') as f:
        json.dump(all_results, f, indent=2)
    
    print("📊 Summary")
    print("=" * 20)
    print(f"Total results found: {len(all_results)}")
    print(f"Results saved to: working_sites_test_results.json")
    
    # Show results by site
    site_counts = {}
    for result in all_results:
        site = result['site']
        site_counts[site] = site_counts.get(site, 0) + 1
    
    print("\nResults by site:")
    for site, count in sorted(site_counts.items(), key=lambda x: x[1], reverse=True):
        print(f"  {site}: {count} results")
    
    return all_results

def show_enabled_sites():
    """Show which sites are enabled"""
    print("📋 Enabled Sites")
    print("=" * 20)
    
    enabled_sites = [site for site in STREAMING_WEBSITES if site.get('enabled', True)]
    disabled_sites = [site for site in STREAMING_WEBSITES if not site.get('enabled', True)]
    
    print(f"✅ Enabled ({len(enabled_sites)}):")
    for site in enabled_sites:
        print(f"  - {site['name']} ({site['base_url']})")
    
    print(f"\n❌ Disabled ({len(disabled_sites)}):")
    for site in disabled_sites:
        reason = "DNS issues" if "ibomma" in site['base_url'] or "movierulz" in site['base_url'] or "jiorockers" in site['base_url'] else "403 error" if "1337x" in site['base_url'] else "Unknown"
        print(f"  - {site['name']} ({site['base_url']}) - {reason}")

if __name__ == "__main__":
    print("🎬 Movie AI Agent - Working Sites Test")
    print("Testing the sites that are currently enabled and accessible")
    print()
    
    show_enabled_sites()
    print()
    
    results = test_working_sites()
    
    print("\n✅ Test completed!")
    print("🌐 The Movie AI Agent is now configured with working sites.")
    print("🎯 Try searching for movies on the web interface!")