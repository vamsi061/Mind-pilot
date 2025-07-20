#!/bin/bash

echo "🎬 Movie AI Agent - Status Check"
echo "================================"

# Check if web interface is running
if pgrep -f "python3 web_interface.py" > /dev/null; then
    echo "✅ Web Interface: Running"
    echo "   Local URL: http://localhost:5000"
else
    echo "❌ Web Interface: Not running"
fi

# Check if cloudflared tunnel is running
if pgrep -f "cloudflared tunnel" > /dev/null; then
    echo "✅ Cloudflare Tunnel: Running"
    TUNNEL_URL=$(cat tunnel.log 2>/dev/null | grep "trycloudflare.com" | tail -1 | sed 's/.*https:\/\/\([^ ]*\).*/\1/')
    if [ ! -z "$TUNNEL_URL" ]; then
        echo "   Public URL: https://$TUNNEL_URL"
    else
        echo "   Public URL: Checking..."
    fi
else
    echo "❌ Cloudflare Tunnel: Not running"
fi

# Check web interface health
echo ""
echo "🔍 Health Check:"
if curl -s http://localhost:5000/health > /dev/null; then
    echo "✅ Web interface is responding"
    HEALTH=$(curl -s http://localhost:5000/health | python3 -m json.tool 2>/dev/null | grep "status" | cut -d'"' -f4)
    echo "   Status: $HEALTH"
else
    echo "❌ Web interface is not responding"
fi

echo ""
echo "📊 Usage:"
echo "   - Visit the public URL above to access the Movie AI Agent"
echo "   - Search for movies and get streaming URLs from 5MovieRulz and MoviezWap"
echo "   - All results are saved automatically"
echo "   - Direct streaming links are extracted and validated"
echo ""
echo "🛠️  Management:"
echo "   - Stop services: pkill -f 'python3 web_interface.py' && pkill -f cloudflared"
echo "   - View logs: tail -f tunnel.log"
echo "   - Restart web interface: python3 web_interface.py &"