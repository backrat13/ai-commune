#!/bin/bash
# Setup script for AI Commune

echo "🏛️  AI Commune Setup Script"
echo "=============================="

# Create directory structure
echo "📁 Creating directory structure..."
mkdir -p agents
mkdir -p world
mkdir -p llm
mkdir -p data/logs
mkdir -p config

# Create __init__.py files for Python packages
touch agents/__init__.py
touch world/__init__.py
touch llm/__init__.py

echo "✅ Directory structure created"

# Check Python version
echo ""
echo "🐍 Checking Python version..."
python_version=$(python3 --version 2>&1)
echo "   Found: $python_version"

# Create virtual environment
echo ""
echo "📦 Creating virtual environment..."
if [ -d "venv" ]; then
    echo "   Virtual environment already exists"
else
    python3 -m venv venv
    echo "   ✅ Virtual environment created"
fi

# Activate and install dependencies
echo ""
echo "📥 Installing dependencies..."
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
echo "   ✅ Dependencies installed"

# Check if Ollama is running
echo ""
echo "🤖 Checking Ollama connection..."
if curl -s http://localhost:11434/api/tags > /dev/null 2>&1; then
    echo "   ✅ Ollama is running"
    echo ""
    echo "   Available models:"
    curl -s http://localhost:11434/api/tags | python3 -c "import sys, json; models = json.load(sys.stdin).get('models', []); [print(f\"      - {m['name']}\") for m in models]"
else
    echo "   ⚠️  Ollama is not running"
    echo ""
    echo "   To start Ollama:"
    echo "   $ ollama serve"
    echo ""
    echo "   To pull a model (recommended):"
    echo "   $ ollama pull llama3.2:3b"
fi

echo ""
echo "=============================="
echo "✅ Setup complete!"
echo ""
echo "To run the simulation:"
echo "  1. Activate the environment: source venv/bin/activate"
echo "  2. Make sure Ollama is running: ollama serve"
echo "  3. Run the simulation: python run.py"
echo ""
echo "🚀 Ready to start your AI Commune!"
