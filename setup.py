#!/usr/bin/env python3
"""
Setup script for Movie AI Agent
"""

import subprocess
import sys
import os

def run_command(command, description):
    """Run a command and handle errors"""
    print(f"🔧 {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} completed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed: {e}")
        if e.stdout:
            print(f"   stdout: {e.stdout}")
        if e.stderr:
            print(f"   stderr: {e.stderr}")
        return False

def check_python_version():
    """Check if Python version is compatible"""
    print("🔍 Checking Python version...")
    
    if sys.version_info < (3, 7):
        print(f"❌ Python 3.7 or higher is required. Current version: {sys.version}")
        return False
    
    print(f"✅ Python {sys.version.split()[0]} is compatible")
    return True

def install_dependencies():
    """Install required dependencies"""
    print("\n📦 Installing dependencies...")
    
    # Upgrade pip first
    if not run_command("pip install --upgrade pip", "Upgrading pip"):
        return False
    
    # Install requirements
    if not run_command("pip install -r requirements.txt", "Installing requirements"):
        return False
    
    return True

def check_chrome():
    """Check if Chrome browser is available"""
    print("\n🔍 Checking Chrome browser...")
    
    chrome_paths = [
        "/usr/bin/google-chrome",
        "/usr/bin/chromium-browser",
        "/usr/bin/chromium",
        "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
        "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
        "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
    ]
    
    for path in chrome_paths:
        if os.path.exists(path):
            print(f"✅ Chrome found at: {path}")
            return True
    
    print("⚠️  Chrome browser not found in common locations")
    print("💡 Please install Google Chrome for Selenium WebDriver support")
    print("   Download from: https://www.google.com/chrome/")
    return False

def run_tests():
    """Run installation tests"""
    print("\n🧪 Running installation tests...")
    
    if not run_command("python test_installation.py", "Running tests"):
        return False
    
    return True

def main():
    """Main setup function"""
    print("🎬 Movie AI Agent - Setup Script\n")
    
    # Check Python version
    if not check_python_version():
        print("\n❌ Setup failed: Incompatible Python version")
        return False
    
    # Install dependencies
    if not install_dependencies():
        print("\n❌ Setup failed: Could not install dependencies")
        return False
    
    # Check Chrome
    check_chrome()
    
    # Run tests
    if not run_tests():
        print("\n❌ Setup failed: Tests did not pass")
        return False
    
    print("\n🎉 Setup completed successfully!")
    print("\n🚀 You can now use the Movie AI Agent:")
    print("   python movie_ai_agent.py                    # Interactive mode")
    print("   python movie_ai_agent.py \"The Matrix\"       # Search for specific movie")
    print("   python example_usage.py                     # Run examples")
    
    return True

if __name__ == "__main__":
    try:
        success = main()
        sys.exit(0 if success else 1)
    except KeyboardInterrupt:
        print("\n\n👋 Setup interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Unexpected error during setup: {e}")
        sys.exit(1)