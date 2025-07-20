# 🎬 Updated Movie AI Agent Features

## 🎯 **Targeted Websites**

The Movie AI Agent has been updated to specifically search and extract streaming URLs from:

### **Primary Sources:**
1. **5MovieRulz** - https://www.5movierulz.rich
2. **MoviezWap** - https://www.moviezwap.pink

## 🔍 **Enhanced Search Capabilities**

### **Smart Search Implementation:**
- **Form Detection**: Automatically finds search forms on each website
- **Dynamic URL Construction**: Builds proper search URLs using `?s=query` format
- **Multiple Selector Support**: Uses various CSS selectors to find movie links
- **Relative URL Handling**: Properly converts relative links to absolute URLs

### **Advanced Link Extraction:**
- **Search Results Parsing**: Extracts movie links from search result pages
- **Multiple Selector Strategies**: 
  - `article a[href*="/movie/"]`
  - `.movie-item a`
  - `.post a[href*="/movie/"]`
  - `h2 a`, `h3 a`
  - `.title a`

## 🎥 **Enhanced Streaming Link Detection**

### **Comprehensive Link Types:**
1. **Direct Watch Links**: `a[href*="watch"]`
2. **Stream Links**: `a[href*="stream"]`
3. **Play Links**: `a[href*="play"]`
4. **Embed Links**: `a[href*="embed"]`
5. **Player Links**: `a[href*="player"]`

### **Embedded Content Detection:**
- **Iframe Embeds**: Direct embedded players
- **Video Sources**: Direct video file links
- **Multiple Formats**: MP4, M3U8, WebM, AVI, MKV

### **Streaming Domain Recognition:**
- YouTube, Vimeo, Dailymotion
- VidCloud, VidStream, Streamango
- OpenLoad, RapidVideo, StreamCherry

## 🛠️ **Technical Improvements**

### **URL Validation:**
- **Pattern Matching**: Regex patterns for streaming URLs
- **Domain Validation**: Recognizes known streaming domains
- **File Extension Check**: Identifies direct video files
- **Content Type Detection**: Validates streaming content

### **Error Handling:**
- **Graceful Failures**: Continues if one site fails
- **Retry Logic**: Multiple attempts for failed requests
- **Timeout Management**: Configurable request timeouts
- **Rate Limiting**: Respectful delays between requests

## 📊 **Usage Examples**

### **Web Interface:**
1. Visit: https://ivory-cigarettes-comparable-existed.trycloudflare.com
2. Enter movie name (e.g., "The Matrix", "Inception")
3. Get results from both 5MovieRulz and MoviezWap
4. Access direct streaming links

### **Command Line:**
```bash
# Test the scraper
python3 test_scraping.py

# Run the web interface
python3 web_interface.py

# Check status
./status.sh
```

## 🔧 **Configuration**

### **Site Configuration:**
```python
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
    }
]
```

## 🚀 **Performance Features**

- **Parallel Processing**: Searches multiple sites simultaneously
- **Caching**: Stores recent search results
- **Progress Tracking**: Real-time search progress updates
- **Result Validation**: Tests streaming URLs for accessibility
- **Automatic Saving**: Saves results to JSON files

## 🔒 **Legal Notice**

⚠️ **Important**: This tool is for educational purposes only. Please ensure you comply with your local laws and respect website terms of service. The developers are not responsible for any misuse of this software.

---

**Updated: July 19, 2025**
**Version: 2.0 - Targeted Website Support**