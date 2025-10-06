#!/bin/bash
# Quick launcher for AI Commune
cd "$(dirname "$0")"
source ai-commune-env/bin/activate 2>/dev/null || echo "Virtual environment not found, run setup.sh first"
python commune_runner.py
