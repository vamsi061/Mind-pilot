# Configuration file for Movie AI Agent
# List of streaming websites to scrape for movie URLs

STREAMING_WEBSITES = [
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
        "name": "5MovieRulz",
        "base_url": "https://www.5movierulz.rich",
        "search_url": "https://www.5movierulz.rich/search_movies",
        "search_param": "s",
        "enabled": True,
        "delay": 2,
        "search_selector": "input[name='s']",
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
        "name": "iBOMMA",
        "base_url": "https://www.ibomma.art",
        "search_url": "https://www.ibomma.art/search",
        "search_param": "q",
        "enabled": False,  # Disabled due to DNS issues
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
        "enabled": False,  # Disabled due to DNS issues
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
        "name": "JioRockers",
        "base_url": "https://www.jiorockers.art",
        "search_url": "https://www.jiorockers.art/search",
        "search_param": "s",
        "enabled": False,  # Disabled due to DNS issues
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
        "enabled": False,  # Disabled due to 403 error
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
        "name": "YTS",
        "base_url": "https://yts.mx",
        "search_url": "https://yts.mx/browse-movies",
        "search_param": "query",
        "enabled": True,
        "delay": 2,
        "search_selector": "input[name='query'], input[type='search']",
        "results_selector": ".browse-movie-title a",
        "title_selector": "h1, .movie-title",
        "streaming_selectors": [
            "a[href*='magnet:']",
            "a[href*='download']",
            ".download-torrent",
            ".magnet-download"
        ]
    },
    {
        "name": "RARBG",
        "base_url": "https://rarbg.to",
        "search_url": "https://rarbg.to/torrents.php",
        "search_param": "search",
        "enabled": True,
        "delay": 2,
        "search_selector": "input[name='search'], input[type='search']",
        "results_selector": ".lista2t a",
        "title_selector": "h1, .movie-title",
        "streaming_selectors": [
            "a[href*='magnet:']",
            "a[href*='download']",
            ".download-link",
            ".magnet-link"
        ]
    },
    {
        "name": "ThePirateBay",
        "base_url": "https://thepiratebay.org",
        "search_url": "https://thepiratebay.org/search.php",
        "search_param": "q",
        "enabled": True,
        "delay": 2,
        "search_selector": "input[name='q'], input[type='search']",
        "results_selector": ".detName a",
        "title_selector": "h1, .movie-title",
        "streaming_selectors": [
            "a[href*='magnet:']",
            "a[href*='download']",
            ".download-link",
            ".magnet-link"
        ]
    },
    {
        "name": "LimeTorrents",
        "base_url": "https://www.limetorrents.info",
        "search_url": "https://www.limetorrents.info/search",
        "search_param": "search",
        "enabled": True,
        "delay": 2,
        "search_selector": "input[name='search'], input[type='search']",
        "results_selector": ".tt-name a",
        "title_selector": "h1, .movie-title",
        "streaming_selectors": [
            "a[href*='magnet:']",
            "a[href*='download']",
            ".download-link",
            ".magnet-link"
        ]
    },
    {
        "name": "KickassTorrents",
        "base_url": "https://katcr.co",
        "search_url": "https://katcr.co/usearch",
        "search_param": "q",
        "enabled": True,
        "delay": 2,
        "search_selector": "input[name='q'], input[type='search']",
        "results_selector": ".cellMainLink a",
        "title_selector": "h1, .movie-title",
        "streaming_selectors": [
            "a[href*='magnet:']",
            "a[href*='download']",
            ".download-link",
            ".magnet-link"
        ]
    },
    {
        "name": "TorrentGalaxy",
        "base_url": "https://torrentgalaxy.to",
        "search_url": "https://torrentgalaxy.to/torrents.php",
        "search_param": "search",
        "enabled": True,
        "delay": 2,
        "search_selector": "input[name='search'], input[type='search']",
        "results_selector": ".tgxtablecell a",
        "title_selector": "h1, .movie-title",
        "streaming_selectors": [
            "a[href*='magnet:']",
            "a[href*='download']",
            ".download-link",
            ".magnet-link"
        ]
    },
    {
        "name": "Nyaa",
        "base_url": "https://nyaa.si",
        "search_url": "https://nyaa.si",
        "search_param": "q",
        "enabled": True,
        "delay": 2,
        "search_selector": "input[name='q'], input[type='search']",
        "results_selector": ".success a",
        "title_selector": "h1, .movie-title",
        "streaming_selectors": [
            "a[href*='magnet:']",
            "a[href*='download']",
            ".download-link",
            ".magnet-link"
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