# Configuration file for Movie AI Agent
# List of streaming websites to scrape for movie URLs

STREAMING_WEBSITES = [
    {
        "name": "123Movies",
        "base_url": "https://123movies.com",
        "search_url": "https://123movies.com/search/",
        "enabled": True,
        "delay": 2
    },
    {
        "name": "Putlocker",
        "base_url": "https://putlocker.com",
        "search_url": "https://putlocker.com/search/",
        "enabled": True,
        "delay": 2
    },
    {
        "name": "Fmovies",
        "base_url": "https://fmovies.to",
        "search_url": "https://fmovies.to/search/",
        "enabled": True,
        "delay": 2
    },
    {
        "name": "SolarMovie",
        "base_url": "https://solarmovie.com",
        "search_url": "https://solarmovie.com/search/",
        "enabled": True,
        "delay": 2
    },
    {
        "name": "WatchSeries",
        "base_url": "https://watchseries.com",
        "search_url": "https://watchseries.com/search/",
        "enabled": True,
        "delay": 2
    },
    {
        "name": "GoMovies",
        "base_url": "https://gomovies.com",
        "search_url": "https://gomovies.com/search/",
        "enabled": True,
        "delay": 2
    },
    {
        "name": "Movie4k",
        "base_url": "https://movie4k.com",
        "search_url": "https://movie4k.com/search/",
        "enabled": True,
        "delay": 2
    },
    {
        "name": "CineBloom",
        "base_url": "https://cinebloom.com",
        "search_url": "https://cinebloom.com/search/",
        "enabled": True,
        "delay": 2
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