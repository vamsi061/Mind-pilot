# 🎬 Movie AI Agent

A powerful Python-based AI agent that automatically finds streaming URLs for movies by scraping multiple streaming websites. The agent uses advanced web scraping techniques to search across various platforms and return working streaming links.

## ✨ Features

- **Multi-Site Search**: Searches across 8+ popular streaming websites simultaneously
- **Smart URL Validation**: Automatically tests and validates streaming URLs
- **Beautiful CLI Interface**: Colorful, user-friendly command-line interface
- **Flexible Usage**: Both interactive and single-search modes
- **Result Export**: Saves search results to JSON file
- **Robust Error Handling**: Graceful handling of network issues and site changes
- **Rate Limiting**: Respectful scraping with configurable delays
- **Selenium Support**: Handles JavaScript-heavy websites

## 🚀 Quick Start

### Prerequisites

- Python 3.7 or higher
- Chrome browser (for Selenium WebDriver)
- Internet connection

### Installation

1. **Clone or download the project files**

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Movie AI Agent**:
   ```bash
   # Interactive mode
   python movie_ai_agent.py
   
   # Search for a specific movie
   python movie_ai_agent.py "The Matrix"
   ```

## 📖 Usage

### Interactive Mode
Run the agent without arguments to enter interactive mode:
```bash
python movie_ai_agent.py
```

The agent will prompt you to enter movie names and display results in real-time.

### Single Search Mode
Search for a specific movie directly:
```bash
python movie_ai_agent.py "Inception"
python movie_ai_agent.py "The Dark Knight"
python movie_ai_agent.py "Interstellar"
```

### Command Line Options
```bash
python movie_ai_agent.py --help
```

## 🔧 Configuration

### Streaming Websites
Edit `config.py` to add, remove, or modify streaming websites:

```python
STREAMING_WEBSITES = [
    {
        "name": "123Movies",
        "base_url": "https://123movies.com",
        "search_url": "https://123movies.com/search/",
        "enabled": True,
        "delay": 2
    },
    # Add more websites here...
]
```

### Settings
Modify these settings in `config.py`:

- `REQUEST_TIMEOUT`: HTTP request timeout (default: 10 seconds)
- `MAX_RETRIES`: Maximum retry attempts (default: 3)
- `REQUEST_DELAY`: Delay between requests (default: 1 second)
- `SAVE_RESULTS`: Whether to save results to file (default: True)
- `OUTPUT_FILE`: Output file name (default: "movie_streaming_urls.json")

## 📁 Project Structure

```
movie-ai-agent/
├── movie_ai_agent.py    # Main application script
├── scraper.py           # Web scraping functionality
├── config.py            # Configuration and settings
├── requirements.txt     # Python dependencies
├── README.md           # This file
└── movie_streaming_urls.json  # Output file (generated)
```

## 🎯 How It Works

1. **Input**: User provides a movie name
2. **Search**: Agent searches across multiple streaming websites
3. **Scraping**: Uses BeautifulSoup and Selenium to extract movie information
4. **Validation**: Tests streaming URLs for accessibility
5. **Output**: Displays formatted results with working streaming links

### Supported Websites

The agent is configured to search these streaming platforms:
- 123Movies
- Putlocker
- Fmovies
- SolarMovie
- WatchSeries
- GoMovies
- Movie4k
- CineBloom

## 🔒 Legal Notice

⚠️ **Important**: This tool is for educational purposes only. Please ensure you comply with your local laws and respect website terms of service. The developers are not responsible for any misuse of this software.

## 🛠️ Technical Details

### Dependencies
- **requests**: HTTP requests
- **beautifulsoup4**: HTML parsing
- **selenium**: JavaScript rendering
- **fake-useragent**: User agent rotation
- **colorama**: Colored terminal output
- **tqdm**: Progress bars
- **webdriver-manager**: Chrome driver management

### Architecture
- **Modular Design**: Separate modules for scraping, configuration, and UI
- **Error Handling**: Comprehensive exception handling and logging
- **Rate Limiting**: Configurable delays to be respectful to websites
- **URL Validation**: Automatic testing of streaming URLs
- **Session Management**: Persistent HTTP sessions with rotating user agents

## 🐛 Troubleshooting

### Common Issues

1. **Chrome Driver Issues**:
   ```bash
   # Install Chrome browser if not already installed
   # The webdriver-manager will automatically download the correct driver
   ```

2. **Permission Errors**:
   ```bash
   # Make the script executable
   chmod +x movie_ai_agent.py
   ```

3. **Import Errors**:
   ```bash
   # Ensure all dependencies are installed
   pip install -r requirements.txt
   ```

4. **No Results Found**:
   - Check your internet connection
   - Try different movie titles
   - Some websites may be temporarily unavailable

### Debug Mode
Enable debug logging by modifying the logging level in the scripts:
```python
logging.basicConfig(level=logging.DEBUG)
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for:
- Bug fixes
- New features
- Website configurations
- Performance improvements

## 📄 License

This project is for educational purposes. Please use responsibly and in compliance with applicable laws.

## ⚠️ Disclaimer

This software is provided "as is" without warranty. Users are responsible for ensuring compliance with local laws and website terms of service. The developers are not liable for any misuse or legal issues arising from the use of this software.

---

**Happy Movie Hunting! 🎬🍿**