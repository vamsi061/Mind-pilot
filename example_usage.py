#!/usr/bin/env python3
"""
Example usage of the Movie AI Agent
Demonstrates how to use the agent programmatically
"""

from movie_ai_agent import MovieAIAgent
import json

def example_basic_search():
    """Example of basic movie search"""
    print("=== Basic Movie Search Example ===")
    
    # Create agent instance
    agent = MovieAIAgent()
    
    # Search for a movie
    movie_name = "The Matrix"
    results, search_time = agent.search_movie(movie_name)
    
    # Display results
    agent.display_results(results, search_time)
    
    return results

def example_multiple_movies():
    """Example of searching multiple movies"""
    print("\n=== Multiple Movies Search Example ===")
    
    # Create agent instance
    agent = MovieAIAgent()
    
    # List of movies to search
    movies = ["Inception", "The Dark Knight", "Interstellar"]
    
    all_results = {}
    
    for movie in movies:
        print(f"\n🔍 Searching for: {movie}")
        results, search_time = agent.search_movie(movie)
        all_results[movie] = {
            'results': results,
            'search_time': search_time,
            'total_links': sum(len(r['streaming_links']) for r in results)
        }
        
        print(f"✅ Found {len(results)} results with {all_results[movie]['total_links']} streaming links")
    
    # Save all results
    with open('multiple_movies_results.json', 'w') as f:
        json.dump(all_results, f, indent=2)
    
    print(f"\n💾 All results saved to 'multiple_movies_results.json'")
    
    return all_results

def example_custom_configuration():
    """Example of using custom configuration"""
    print("\n=== Custom Configuration Example ===")
    
    # You can modify the config before creating the agent
    from config import STREAMING_WEBSITES
    
    # Disable some sites for faster testing
    for site in STREAMING_WEBSITES:
        if site['name'] in ['123Movies', 'Putlocker']:
            site['enabled'] = False
    
    # Create agent with modified config
    agent = MovieAIAgent()
    
    # Search with limited sites
    movie_name = "Avatar"
    results, search_time = agent.search_movie(movie_name)
    
    print(f"🔍 Searched with limited sites for: {movie_name}")
    print(f"✅ Found {len(results)} results in {search_time:.2f} seconds")
    
    return results

def example_result_analysis():
    """Example of analyzing search results"""
    print("\n=== Result Analysis Example ===")
    
    # Search for a movie
    agent = MovieAIAgent()
    results, _ = agent.search_movie("The Avengers")
    
    if not results:
        print("❌ No results found for analysis")
        return
    
    # Analyze results
    total_streaming_links = sum(len(r['streaming_links']) for r in results)
    sites_used = set(r['site'] for r in results)
    
    print(f"📊 Analysis Results:")
    print(f"   Total movies found: {len(results)}")
    print(f"   Total streaming links: {total_streaming_links}")
    print(f"   Sites searched: {len(sites_used)}")
    print(f"   Sites: {', '.join(sites_used)}")
    
    # Find the site with most links
    site_link_counts = {}
    for result in results:
        site = result['site']
        if site not in site_link_counts:
            site_link_counts[site] = 0
        site_link_counts[site] += len(result['streaming_links'])
    
    best_site = max(site_link_counts.items(), key=lambda x: x[1])
    print(f"   Best performing site: {best_site[0]} ({best_site[1]} links)")

def example_error_handling():
    """Example of error handling"""
    print("\n=== Error Handling Example ===")
    
    agent = MovieAIAgent()
    
    try:
        # Try to search for a movie that might not exist
        results, search_time = agent.search_movie("ThisMovieDoesNotExist12345")
        
        if not results:
            print("✅ Properly handled case with no results")
        else:
            print("⚠️ Unexpected results found")
            
    except Exception as e:
        print(f"❌ Error occurred: {e}")
        print("✅ Error was properly caught and handled")

if __name__ == "__main__":
    print("🎬 Movie AI Agent - Example Usage\n")
    
    # Run examples
    try:
        # Basic search
        example_basic_search()
        
        # Multiple movies (commented out to avoid long execution)
        # example_multiple_movies()
        
        # Custom configuration
        example_custom_configuration()
        
        # Result analysis
        example_result_analysis()
        
        # Error handling
        example_error_handling()
        
    except KeyboardInterrupt:
        print("\n\n👋 Examples interrupted by user")
    except Exception as e:
        print(f"\n❌ Error running examples: {e}")
    
    print("\n✅ All examples completed!")