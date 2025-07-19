# Configuration file for Movie AI Agent
# List of streaming websites to scrape for movie URLs

STREAMING_WEBSITES = [
    {
        "name": "5MovieRulz",
        "base_url": "https://www.5movierulz.rich",
        "search_url": "https://www.5movierulz.rich/search/",
        "enabled": True,
        "delay": 2,
        "search_selector": "input[name='s']",
        "results_selector": ".movie-item, .film-item, .search-item",
        "title_selector": "h2, .title, .movie-title",
        "streaming_selectors": [
            "a[href*='watch']",
            "a[href*='stream']", 
            "a[href*='play']",
            ".watch-link",
            ".stream-link"
        ]
    },
    {
        "name": "MoviezWap",
        "base_url": "https://www.moviezwap.pink",
        "search_url": "https://www.moviezwap.pink/search/",
        "enabled": True,
        "delay": 2,
        "search_selector": "input[name='s']",
        "results_selector": ".movie-item, .film-item, .search-item",
        "title_selector": "h2, .title, .movie-title",
        "streaming_selectors": [
            "a[href*='watch']",
            "a[href*='stream']",
            "a[href*='play']", 
            ".watch-link",
            ".stream-link"
        ]
    }
]

# User agents for rotating requests
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:89.0) Gecko/20100101 Firefox/89.0"
]

# Request settings
REQUEST_TIMEOUT = 10
MAX_RETRIES = 3
REQUEST_DELAY = 1

# Output settings
SAVE_RESULTS = True
OUTPUT_FILE = "movie_streaming_urls.json"