#!/usr/bin/env python3
"""
Web Interface for Movie AI Agent
Flask-based web application for remote access
"""

from flask import Flask, render_template, request, jsonify, session
from movie_ai_agent import MovieAIAgent
import threading
import time
import json
from datetime import datetime
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

# Global variables for search status
search_status = {}
search_results = {}

class SearchManager:
    def __init__(self):
        self.agent = MovieAIAgent()
        self.active_searches = {}
    
    def start_search(self, movie_name, search_id):
        """Start a search in a separate thread"""
        def search_worker():
            try:
                search_status[search_id] = {
                    'status': 'searching',
                    'progress': 0,
                    'message': f'Searching for "{movie_name}"...',
                    'start_time': datetime.now().isoformat()
                }
                
                # Perform the search
                results, search_time = self.agent.search_movie(movie_name)
                
                # Store results
                search_results[search_id] = {
                    'movie_name': movie_name,
                    'results': results,
                    'search_time': search_time,
                    'total_results': len(results),
                    'total_links': sum(len(r['streaming_links']) for r in results),
                    'completed_time': datetime.now().isoformat()
                }
                
                # Update status
                search_status[search_id] = {
                    'status': 'completed',
                    'progress': 100,
                    'message': f'Found {len(results)} results with {sum(len(r["streaming_links"]) for r in results)} streaming links',
                    'search_time': search_time
                }
                
            except Exception as e:
                search_status[search_id] = {
                    'status': 'error',
                    'progress': 0,
                    'message': f'Error: {str(e)}',
                    'error': str(e)
                }
        
        # Start the search thread
        thread = threading.Thread(target=search_worker)
        thread.daemon = True
        thread.start()
        
        return search_id

# Initialize search manager
search_manager = SearchManager()

@app.route('/')
def index():
    """Main page"""
    return render_template('index.html')

@app.route('/api/search', methods=['POST'])
def start_search():
    """Start a new search"""
    try:
        data = request.get_json()
        movie_name = data.get('movie_name', '').strip()
        
        if not movie_name:
            return jsonify({'error': 'Movie name is required'}), 400
        
        # Generate unique search ID
        search_id = f"search_{int(time.time())}_{hash(movie_name) % 10000}"
        
        # Start search
        search_manager.start_search(movie_name, search_id)
        
        return jsonify({
            'search_id': search_id,
            'message': f'Search started for "{movie_name}"'
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/status/<search_id>')
def get_status(search_id):
    """Get search status"""
    try:
        status = search_status.get(search_id, {'status': 'not_found'})
        return jsonify(status)
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/results/<search_id>')
def get_results(search_id):
    """Get search results"""
    try:
        results = search_results.get(search_id)
        if not results:
            return jsonify({'error': 'Results not found'}), 404
        
        return jsonify(results)
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/recent')
def get_recent_searches():
    """Get recent searches"""
    try:
        recent = []
        for search_id, results in list(search_results.items())[-10:]:  # Last 10 searches
            recent.append({
                'search_id': search_id,
                'movie_name': results['movie_name'],
                'total_results': results['total_results'],
                'total_links': results['total_links'],
                'completed_time': results['completed_time']
            })
        
        return jsonify({'recent_searches': recent})
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/health')
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat(),
        'active_searches': len(search_status),
        'total_results': len(search_results)
    })

if __name__ == '__main__':
    # Create templates directory if it doesn't exist
    os.makedirs('templates', exist_ok=True)
    
    print("🎬 Movie AI Agent - Web Interface")
    print("🌐 Starting web server on http://localhost:5000")
    print("📡 Ready for Cloudflare Tunnel connection")
    
    app.run(host='0.0.0.0', port=5000, debug=False)