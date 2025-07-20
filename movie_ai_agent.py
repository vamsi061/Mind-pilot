#!/usr/bin/env python3
"""
Movie AI Agent - Find streaming URLs for movies by scraping multiple websites
"""

import json
import time
import sys
from datetime import datetime
from colorama import init, Fore, Style
from tqdm import tqdm
import argparse
from scraper import MovieScraper
from config import SAVE_RESULTS, OUTPUT_FILE
import logging

# Initialize colorama for colored output
init(autoreset=True)

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class MovieAIAgent:
    def __init__(self):
        self.scraper = MovieScraper()
        self.results = []
    
    def print_banner(self):
        """Print the application banner"""
        banner = f"""
{Fore.CYAN}╔══════════════════════════════════════════════════════════════╗
║                    {Fore.YELLOW}🎬 MOVIE AI AGENT 🎬{Fore.CYAN}                    ║
║                                                                    ║
║  Find streaming URLs for your favorite movies across multiple     ║
║  streaming websites using advanced web scraping technology        ║
╚══════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}
        """
        print(banner)
    
    def search_movie(self, movie_name):
        """Search for a movie and return streaming URLs"""
        print(f"\n{Fore.GREEN}🔍 Searching for: {Fore.WHITE}{movie_name}{Style.RESET_ALL}")
        print(f"{Fore.BLUE}⏳ This may take a few minutes...{Style.RESET_ALL}\n")
        
        start_time = time.time()
        
        try:
            # Search all sites
            results = self.scraper.search_all_sites(movie_name)
            
            # Validate streaming URLs
            print(f"{Fore.YELLOW}🔗 Validating streaming URLs...{Style.RESET_ALL}")
            validated_results = self.scraper.validate_streaming_urls(results)
            
            end_time = time.time()
            search_time = end_time - start_time
            
            return validated_results, search_time
            
        except Exception as e:
            logger.error(f"Error during search: {e}")
            print(f"{Fore.RED}❌ Error occurred during search: {e}{Style.RESET_ALL}")
            return [], 0
    
    def display_results(self, results, search_time):
        """Display search results in a formatted way"""
        if not results:
            print(f"\n{Fore.RED}❌ No streaming URLs found for this movie.{Style.RESET_ALL}")
            print(f"{Fore.YELLOW}💡 Try searching with a different movie title or check spelling.{Style.RESET_ALL}")
            return
        
        print(f"\n{Fore.GREEN}✅ Search completed in {search_time:.2f} seconds{Style.RESET_ALL}")
        print(f"{Fore.CYAN}📊 Found {len(results)} results across {len(set(r['site'] for r in results))} websites{Style.RESET_ALL}\n")
        
        for i, result in enumerate(results, 1):
            print(f"{Fore.YELLOW}🎬 {i}. {result['title']}{Style.RESET_ALL}")
            print(f"   📺 Site: {Fore.CYAN}{result['site']}{Style.RESET_ALL}")
            print(f"   🌐 URL: {Fore.BLUE}{result['url']}{Style.RESET_ALL}")
            print(f"   🔗 Streaming Links ({len(result['streaming_links'])} found):")
            
            for j, link in enumerate(result['streaming_links'], 1):
                print(f"      {j}. {Fore.GREEN}{link['text']}{Style.RESET_ALL}")
                print(f"         {Fore.WHITE}{link['url']}{Style.RESET_ALL}")
            
            print()
        
        # Save results if enabled
        if SAVE_RESULTS:
            self.save_results(results)
    
    def save_results(self, results):
        """Save results to JSON file"""
        try:
            output_data = {
                'timestamp': datetime.now().isoformat(),
                'total_results': len(results),
                'results': results
            }
            
            with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
                json.dump(output_data, f, indent=2, ensure_ascii=False)
            
            print(f"{Fore.GREEN}💾 Results saved to: {OUTPUT_FILE}{Style.RESET_ALL}")
            
        except Exception as e:
            logger.error(f"Error saving results: {e}")
            print(f"{Fore.RED}❌ Error saving results: {e}{Style.RESET_ALL}")
    
    def interactive_mode(self):
        """Run the agent in interactive mode"""
        self.print_banner()
        
        while True:
            try:
                print(f"\n{Fore.CYAN}Enter a movie name to search (or 'quit' to exit):{Style.RESET_ALL}")
                movie_name = input(f"{Fore.GREEN}🎬 Movie: {Style.RESET_ALL}").strip()
                
                if movie_name.lower() in ['quit', 'exit', 'q']:
                    print(f"\n{Fore.YELLOW}👋 Goodbye!{Style.RESET_ALL}")
                    break
                
                if not movie_name:
                    print(f"{Fore.RED}❌ Please enter a movie name.{Style.RESET_ALL}")
                    continue
                
                # Search for the movie
                results, search_time = self.search_movie(movie_name)
                
                # Display results
                self.display_results(results, search_time)
                
                # Ask if user wants to search again
                print(f"\n{Fore.CYAN}Would you like to search for another movie? (y/n):{Style.RESET_ALL}")
                continue_search = input(f"{Fore.GREEN}➤ {Style.RESET_ALL}").strip().lower()
                
                if continue_search not in ['y', 'yes', '']:
                    print(f"\n{Fore.YELLOW}👋 Goodbye!{Style.RESET_ALL}")
                    break
                
            except KeyboardInterrupt:
                print(f"\n\n{Fore.YELLOW}👋 Goodbye!{Style.RESET_ALL}")
                break
            except Exception as e:
                logger.error(f"Unexpected error: {e}")
                print(f"{Fore.RED}❌ An unexpected error occurred: {e}{Style.RESET_ALL}")
    
    def single_search_mode(self, movie_name):
        """Run the agent in single search mode"""
        self.print_banner()
        
        print(f"{Fore.CYAN}Single Search Mode{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}Searching for: {movie_name}{Style.RESET_ALL}\n")
        
        # Search for the movie
        results, search_time = self.search_movie(movie_name)
        
        # Display results
        self.display_results(results, search_time)
        
        return results

def main():
    """Main function to run the Movie AI Agent"""
    parser = argparse.ArgumentParser(
        description='Movie AI Agent - Find streaming URLs for movies',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python movie_ai_agent.py                    # Interactive mode
  python movie_ai_agent.py "The Matrix"       # Search for specific movie
  python movie_ai_agent.py "Inception"        # Search for Inception
        """
    )
    
    parser.add_argument(
        'movie_name',
        nargs='?',
        help='Name of the movie to search for'
    )
    
    parser.add_argument(
        '--version',
        action='version',
        version='Movie AI Agent v1.0.0'
    )
    
    args = parser.parse_args()
    
    # Create agent instance
    agent = MovieAIAgent()
    
    try:
        if args.movie_name:
            # Single search mode
            agent.single_search_mode(args.movie_name)
        else:
            # Interactive mode
            agent.interactive_mode()
    
    except KeyboardInterrupt:
        print(f"\n\n{Fore.YELLOW}👋 Goodbye!{Style.RESET_ALL}")
        sys.exit(0)
    except Exception as e:
        logger.error(f"Fatal error: {e}")
        print(f"{Fore.RED}❌ Fatal error: {e}{Style.RESET_ALL}")
        sys.exit(1)

if __name__ == "__main__":
    main()