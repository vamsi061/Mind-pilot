# Configuration file for Movie AI Agent
# List of streaming websites to scrape for movie URLs

STREAMING_WEBSITES = [
    {
        "name": "iBOMMA",
        "base_url": "https://www.ibomma.art",
        "search_url": "https://www.ibomma.art/search",
        "search_param": "q",
        "enabled": True,
        "delay": 2,
        "search_selector": "input[name='q'], input[type='search']",
        "results_selector": "a[href*='/movie/'], .movie-item a, .search-item a",
        "title_selector": "h2, .title, .movie-title",
        "streaming_selectors": [
            "a[href*='watch']",
            "a[href*='stream']", 
            "a[href*='play']",
            "a[href*='download']",
            ".watch-link",
            ".stream-link",
            ".download-link"
        ]
    },
    {
        "name": "MovieRulz",
        "base_url": "https://www.movierulz.art",
        "search_url": "https://www.movierulz.art/search",
        "search_param": "s",
        "enabled": True,
        "delay": 2,
        "search_selector": "input[name='s'], input[type='search']",
        "results_selector": "a[href*='/movie/'], .movie-item a, .search-item a",
        "title_selector": "h2, .title, .movie-title",
        "streaming_selectors": [
            "a[href*='watch']",
            "a[href*='stream']", 
            "a[href*='play']",
            "a[href*='download']",
            ".watch-link",
            ".stream-link",
            ".download-link"
        ]
    },
    {
        "name": "Cinevez",
        "base_url": "https://www.cinevez.art",
        "search_url": "https://www.cinevez.art/search",
        "search_param": "q",
        "enabled": True,
        "delay": 2,
        "search_selector": "input[name='q'], input[type='search']",
        "results_selector": "a[href*='/movie/'], .movie-item a, .search-item a",
        "title_selector": "h2, .title, .movie-title",
        "streaming_selectors": [
            "a[href*='watch']",
            "a[href*='stream']", 
            "a[href*='play']",
            "a[href*='download']",
            ".watch-link",
            ".stream-link",
            ".download-link"
        ]
    },
    {
        "name": "MoviezWap",
        "base_url": "https://www.moviezwap.pink",
        "search_url": "https://www.moviezwap.pink/search.php",
        "search_param": "q",
        "enabled": True,
        "delay": 2,
        "search_selector": "input[name='q']",
        "results_selector": "a[href*='/movie/']",
        "title_selector": "h2, .title, .movie-title",
        "streaming_selectors": [
            "a[href*='watch']",
            "a[href*='stream']",
            "a[href*='play']",
            "a[href*='download']",
            ".watch-link",
            ".stream-link",
            ".download-link"
        ]
    },
    {
        "name": "TeluguPalaka",
        "base_url": "https://www.telugupalaka.com",
        "search_url": "https://www.telugupalaka.com/search",
        "search_param": "q",
        "enabled": True,
        "delay": 2,
        "search_selector": "input[name='q'], input[type='search']",
        "results_selector": "a[href*='/movie/'], .movie-item a, .search-item a",
        "title_selector": "h2, .title, .movie-title",
        "streaming_selectors": [
            "a[href*='watch']",
            "a[href*='stream']", 
            "a[href*='play']",
            "a[href*='download']",
            ".watch-link",
            ".stream-link",
            ".download-link"
        ]
    },
    {
        "name": "JioRockers",
        "base_url": "https://www.jiorockers.art",
        "search_url": "https://www.jiorockers.art/search",
        "search_param": "s",
        "enabled": True,
        "delay": 2,
        "search_selector": "input[name='s'], input[type='search']",
        "results_selector": "a[href*='/movie/'], .movie-item a, .search-item a",
        "title_selector": "h2, .title, .movie-title",
        "streaming_selectors": [
            "a[href*='watch']",
            "a[href*='stream']", 
            "a[href*='play']",
            "a[href*='download']",
            ".watch-link",
            ".stream-link",
            ".download-link"
        ]
    },
    {
        "name": "Cinevood",
        "base_url": "https://www.cinevood.art",
        "search_url": "https://www.cinevood.art/search",
        "search_param": "q",
        "enabled": True,
        "delay": 2,
        "search_selector": "input[name='q'], input[type='search']",
        "results_selector": "a[href*='/movie/'], .movie-item a, .search-item a",
        "title_selector": "h2, .title, .movie-title",
        "streaming_selectors": [
            "a[href*='watch']",
            "a[href*='stream']", 
            "a[href*='play']",
            "a[href*='download']",
            ".watch-link",
            ".stream-link",
            ".download-link"
        ]
    },
    {
        "name": "Gadg8",
        "base_url": "https://www.gadg8.art",
        "search_url": "https://www.gadg8.art/search",
        "search_param": "s",
        "enabled": True,
        "delay": 2,
        "search_selector": "input[name='s'], input[type='search']",
        "results_selector": "a[href*='/movie/'], .movie-item a, .search-item a",
        "title_selector": "h2, .title, .movie-title",
        "streaming_selectors": [
            "a[href*='watch']",
            "a[href*='stream']", 
            "a[href*='play']",
            "a[href*='download']",
            ".watch-link",
            ".stream-link",
            ".download-link"
        ]
    },
    {
        "name": "1337x",
        "base_url": "https://www.1337x.to",
        "search_url": "https://www.1337x.to/search",
        "search_param": "q",
        "enabled": True,
        "delay": 2,
        "search_selector": "input[name='q'], input[type='search']",
        "results_selector": "a[href*='/torrent/'], .name a",
        "title_selector": "h2, .title, .movie-title",
        "streaming_selectors": [
            "a[href*='magnet:']",
            "a[href*='download']",
            ".download-link",
            ".magnet-link"
        ]
    },
    {
        "name": "NetMirror",
        "base_url": "https://www.netmirror.org",
        "search_url": "https://www.netmirror.org/search",
        "search_param": "q",
        "enabled": True,
        "delay": 2,
        "search_selector": "input[name='q'], input[type='search']",
        "results_selector": "a[href*='/movie/'], .movie-item a, .search-item a",
        "title_selector": "h2, .title, .movie-title",
        "streaming_selectors": [
            "a[href*='watch']",
            "a[href*='stream']", 
            "a[href*='play']",
            "a[href*='download']",
            ".watch-link",
            ".stream-link",
            ".download-link"
        ]
    },
    {
        "name": "UFlix",
        "base_url": "https://www.uflix.art",
        "search_url": "https://www.uflix.art/search",
        "search_param": "q",
        "enabled": True,
        "delay": 2,
        "search_selector": "input[name='q'], input[type='search']",
        "results_selector": "a[href*='/movie/'], .movie-item a, .search-item a",
        "title_selector": "h2, .title, .movie-title",
        "streaming_selectors": [
            "a[href*='watch']",
            "a[href*='stream']", 
            "a[href*='play']",
            "a[href*='download']",
            ".watch-link",
            ".stream-link",
            ".download-link"
        ]
    },
    {
        "name": "MultiMovies",
        "base_url": "https://www.multimovies.art",
        "search_url": "https://www.multimovies.art/search",
        "search_param": "s",
        "enabled": True,
        "delay": 2,
        "search_selector": "input[name='s'], input[type='search']",
        "results_selector": "a[href*='/movie/'], .movie-item a, .search-item a",
        "title_selector": "h2, .title, .movie-title",
        "streaming_selectors": [
            "a[href*='watch']",
            "a[href*='stream']", 
            "a[href*='play']",
            "a[href*='download']",
            ".watch-link",
            ".stream-link",
            ".download-link"
        ]
    },
    {
        "name": "Flixer",
        "base_url": "https://www.flixer.art",
        "search_url": "https://www.flixer.art/search",
        "search_param": "q",
        "enabled": True,
        "delay": 2,
        "search_selector": "input[name='q'], input[type='search']",
        "results_selector": "a[href*='/movie/'], .movie-item a, .search-item a",
        "title_selector": "h2, .title, .movie-title",
        "streaming_selectors": [
            "a[href*='watch']",
            "a[href*='stream']", 
            "a[href*='play']",
            "a[href*='download']",
            ".watch-link",
            ".stream-link",
            ".download-link"
        ]
    },
    {
        "name": "DownloadHub",
        "base_url": "https://www.downloadhub.art",
        "search_url": "https://www.downloadhub.art/search",
        "search_param": "s",
        "enabled": True,
        "delay": 2,
        "search_selector": "input[name='s'], input[type='search']",
        "results_selector": "a[href*='/movie/'], .movie-item a, .search-item a",
        "title_selector": "h2, .title, .movie-title",
        "streaming_selectors": [
            "a[href*='watch']",
            "a[href*='stream']", 
            "a[href*='play']",
            "a[href*='download']",
            ".watch-link",
            ".stream-link",
            ".download-link"
        ]
    },
    {
        "name": "UHDMovies",
        "base_url": "https://www.uhdmovies.art",
        "search_url": "https://www.uhdmovies.art/search",
        "search_param": "q",
        "enabled": True,
        "delay": 2,
        "search_selector": "input[name='q'], input[type='search']",
        "results_selector": "a[href*='/movie/'], .movie-item a, .search-item a",
        "title_selector": "h2, .title, .movie-title",
        "streaming_selectors": [
            "a[href*='watch']",
            "a[href*='stream']", 
            "a[href*='play']",
            "a[href*='download']",
            ".watch-link",
            ".stream-link",
            ".download-link"
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