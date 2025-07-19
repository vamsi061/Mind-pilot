#!/usr/bin/env python3
"""
Test script to verify Movie AI Agent installation and basic functionality
"""

import sys
import importlib

def test_imports():
    """Test if all required modules can be imported"""
    print("🔍 Testing imports...")
    
    required_modules = [
        'requests',
        'beautifulsoup4',
        'selenium',
        'fake_useragent',
        'colorama',
        'tqdm',
        'webdriver_manager'
    ]
    
    failed_imports = []
    
    for module in required_modules:
        try:
            importlib.import_module(module)
            print(f"✅ {module}")
        except ImportError as e:
            print(f"❌ {module}: {e}")
            failed_imports.append(module)
    
    if failed_imports:
        print(f"\n❌ Failed to import: {', '.join(failed_imports)}")
        print("💡 Run: pip install -r requirements.txt")
        return False
    else:
        print("\n✅ All imports successful!")
        return True

def test_config():
    """Test if configuration can be loaded"""
    print("\n🔍 Testing configuration...")
    
    try:
        from config import STREAMING_WEBSITES, USER_AGENTS
        print(f"✅ Configuration loaded successfully")
        print(f"   - {len(STREAMING_WEBSITES)} streaming websites configured")
        print(f"   - {len(USER_AGENTS)} user agents available")
        return True
    except Exception as e:
        print(f"❌ Configuration error: {e}")
        return False

def test_scraper_initialization():
    """Test if scraper can be initialized"""
    print("\n🔍 Testing scraper initialization...")
    
    try:
        from scraper import MovieScraper
        scraper = MovieScraper()
        print("✅ Scraper initialized successfully")
        return True
    except Exception as e:
        print(f"❌ Scraper initialization error: {e}")
        return False

def test_agent_initialization():
    """Test if agent can be initialized"""
    print("\n🔍 Testing agent initialization...")
    
    try:
        from movie_ai_agent import MovieAIAgent
        agent = MovieAIAgent()
        print("✅ Agent initialized successfully")
        return True
    except Exception as e:
        print(f"❌ Agent initialization error: {e}")
        return False

def test_basic_functionality():
    """Test basic functionality without actual web scraping"""
    print("\n🔍 Testing basic functionality...")
    
    try:
        from scraper import MovieScraper
        scraper = MovieScraper()
        
        # Test URL validation
        test_urls = [
            "https://example.com/watch/movie",
            "https://example.com/stream/video",
            "https://example.com/play/film",
            "https://example.com/invalid"
        ]
        
        valid_count = 0
        for url in test_urls:
            if scraper.is_valid_streaming_url(url):
                valid_count += 1
        
        print(f"✅ URL validation working ({valid_count}/{len(test_urls)} valid URLs detected)")
        return True
        
    except Exception as e:
        print(f"❌ Basic functionality error: {e}")
        return False

def main():
    """Run all tests"""
    print("🎬 Movie AI Agent - Installation Test\n")
    
    tests = [
        ("Import Test", test_imports),
        ("Configuration Test", test_config),
        ("Scraper Test", test_scraper_initialization),
        ("Agent Test", test_agent_initialization),
        ("Basic Functionality Test", test_basic_functionality)
    ]
    
    passed = 0
    total = len(tests)
    
    for test_name, test_func in tests:
        print(f"\n{'='*50}")
        print(f"Running: {test_name}")
        print('='*50)
        
        try:
            if test_func():
                passed += 1
        except Exception as e:
            print(f"❌ Test failed with exception: {e}")
    
    print(f"\n{'='*50}")
    print(f"Test Results: {passed}/{total} tests passed")
    print('='*50)
    
    if passed == total:
        print("🎉 All tests passed! The Movie AI Agent is ready to use.")
        print("\n🚀 You can now run:")
        print("   python movie_ai_agent.py")
        print("   python movie_ai_agent.py \"The Matrix\"")
    else:
        print("❌ Some tests failed. Please check the errors above.")
        print("\n💡 Common solutions:")
        print("   1. Install dependencies: pip install -r requirements.txt")
        print("   2. Install Chrome browser for Selenium")
        print("   3. Check your internet connection")
    
    return passed == total

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)