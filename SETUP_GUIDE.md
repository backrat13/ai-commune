# 🏛️ AI Commune - Complete Setup Guide

**Everything you need to get your AI commune running in 10 minutes.**

---

## 📋 What You'll Get

Two fully functional AI commune implementations:
1. **Ollama Version** - Real LLM-powered agents with creative responses
2. **PettingZoo Version** - Fast, deterministic multi-agent simulation

---

## 🗂️ Complete File Structure

Here's what your project should look like after setup:

```
commune/
│
├── 📄 Core Files
│   ├── run.py                      # Ollama version entry point
│   ├── commune_pettingzoo.py       # PettingZoo version entry point
│   ├── commune_cli.py              # CLI management tool
│   └── setup.sh                    # Automated setup script
│
├── 📦 Agent System (for Ollama version)
│   └── agents/
│       ├── __init__.py
│       ├── agent.py                # Core agent class
│       ├── memory.py               # Memory management
│       ├── reflection.py           # LLM-powered reflection
│       └── constitution.py         # Ethical framework
│
├── 🌍 World System (for Ollama version)
│   └── world/
│       ├── __init__.py
│       ├── message_bus.py          # Communication layer
│       └── scheduler.py            # Simulation orchestrator
│
├── 🤖 LLM Client (for Ollama version)
│   └── llm/
│       ├── __init__.py
│       └── ollama_client.py        # Ollama API interface
│
├── 📊 Data & Output
│   └── data/
│       ├── logs/                   # Agent memories & logs
│       │   ├── .gitkeep
│       │   ├── Aria_memory.jsonl   # (generated)
│       │   ├── Nox_memory.jsonl    # (generated)
│       │   └── commune_*.log       # (generated)
│       ├── pettingzoo_reports/     # PettingZoo output
│       │   └── commune_report_*.json
│       └── communal_laws.json      # (generated)
│
├── 📚 Documentation
│   ├── README.md                   # Main overview
│   ├── README_PETTINGZOO.md        # PettingZoo guide
│   ├── QUICKSTART.md               # Quick start guide
│   ├── COMPARISON.md               # Version comparison
│   └── SETUP_GUIDE.md              # This file
│
├── ⚙️ Configuration
│   ├── requirements.txt            # Ollama dependencies
│   ├── requirements_pettingzoo.txt # PettingZoo dependencies
│   └── .gitignore                  # Git ignore rules
│
└── 🐍 Python Environment
    └── venv/                       # Virtual environment
```

---

## 🚀 Installation

### Option 1: Automated Setup (Recommended)

```bash
# 1. Navigate to commune directory
cd commune

# 2. Make setup script executable
chmod +x setup.sh

# 3. Run setup
./setup.sh

# This will:
# ✓ Create directory structure
# ✓ Set up virtual environment
# ✓ Install dependencies
# ✓ Check Ollama connection
```

### Option 2: Manual Setup

```bash
# 1. Create directory structure
mkdir -p agents world llm data/logs data/pettingzoo_reports config

# 2. Create __init__.py files
touch agents/__init__.py world/__init__.py llm/__init__.py

# 3. Create virtual environment
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 4. Install dependencies for Ollama version
pip install -r requirements.txt

# 5. Install dependencies for PettingZoo version
pip install -r requirements_pettingzoo.txt
```

---

## 🤖 Ollama Setup (For Ollama Version Only)

### Step 1: Install Ollama

**macOS / Linux:**
```bash
curl -fsSL https://ollama.ai/install.sh | sh
```

**Windows:**
Download from https://ollama.ai/download

### Step 2: Pull a Model

```bash
# Recommended: Fast and good quality (3GB)
ollama pull llama3.2:3b

# Alternative: Very fast, smaller (1.5GB)
ollama pull gemma2:2b

# Alternative: Better quality, slower (5GB)
ollama pull llama3.1:8b
```

### Step 3: Start Ollama Server

```bash
# Keep this running in a separate terminal
ollama serve
```

### Step 4: Test Connection

```bash
# Should return JSON with available models
curl http://localhost:11434/api/tags
```

---

## ✅ Verification

### Test PettingZoo Version (No Ollama Needed)

```bash
# Activate environment
source venv/bin/activate

# Run PettingZoo version (should work immediately)
python commune_pettingzoo.py
```

**Expected output:**
```
18:42:15 | 🏛️  Commune initialized with 4 agents
18:42:15 | ✨ Initialized sociologist: agent_0
18:42:15 | ✨ Initialized programmer: agent_1
18:42:15 | ✨ Initialized philosopher: agent_2
18:42:15 | ✨ Initialized secretary: agent_3
...
```

### Test Ollama Version

```bash
# Make sure Ollama is running first!
ollama serve  # In another terminal

# Activate environment
source venv/bin/activate

# Run Ollama version
python run.py
```

**Expected output:**
```
16:42:15 | INFO     | AI COMMUNE - Starting Simulation
16:42:15 | INFO     | Connected to Ollama at http://localhost:11434
16:42:15 | INFO     | Using model: llama3.2:3b
16:42:16 | INFO     | Agent Aria (Philosopher) initialized.
...
```

---

## 🎯 First Run Checklist

### Before Running Ollama Version:
- [ ] Ollama is installed
- [ ] Model is downloaded (`ollama pull llama3.2:3b`)
- [ ] Ollama server is running (`ollama serve`)
- [ ] Virtual environment is activated
- [ ] Dependencies are installed

### Before Running PettingZoo Version:
- [ ] Virtual environment is activated
- [ ] PettingZoo dependencies are installed
- [ ] That's it! No Ollama needed

---

## 📊 Understanding the Outputs

### Ollama Version Output

**Console:**
```
16:42:18 | INFO | TICK 1 - 16:42:18
16:42:20 | INFO | [Aria] ✓ Action: I will introduce myself and share...
16:42:22 | INFO | [Aria] Reflection stored
```

**Files Created:**
- `data/logs/Aria_memory.jsonl` - Aria's experiences
- `data/logs/Nox_memory.jsonl` - Nox's experiences  
- `data/logs/Kairo_memory.jsonl` - Kairo's experiences
- `data/logs/commune_*.log` - Full simulation log
- `data/communal_laws.json` - Constitution and laws

### PettingZoo Version Output

**Console:**
```
18:42:16 | 🎯 [sociologist] Observing agent clustering patterns...
18:42:17 | 🎯 [secretary] Recording agent movement patterns...
```

**Files Created:**
- `data/pettingzoo_reports/commune_report_*.json` - Complete reports

---

## 🔧 Using the CLI Tool

```bash
# View all available commands
python commune_cli.py help

# Show simulation statistics
python commune_cli.py stats

# View specific agent's memories
python commune_cli.py memories Aria

# Display the constitution
python commune_cli.py constitution

# Add a new communal law
python commune_cli.py add-law "Seek consensus on major decisions"

# List all agents
python commune_cli.py list-agents

# Export agent memory to JSON
python commune_cli.py export Aria

# Clean all data (⚠️ destructive!)
python commune_cli.py clean
```

---

## 🐛 Troubleshooting

### Problem: "Cannot connect to Ollama"

**Solution:**
```bash
# Start Ollama in a separate terminal
ollama serve
```

### Problem: "Model not found"

**Solution:**
```bash
# Pull the model
ollama pull llama3.2:3b

# Verify it's available
ollama list
```

### Problem: "ModuleNotFoundError"

**Solution:**
```bash
# Make sure virtual environment is activated
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Reinstall dependencies
pip install -r requirements.txt
pip install -r requirements_pettingzoo.txt
```

### Problem: "ImportError: No module named 'agents'"

**Solution:**
```bash
# Make sure __init__.py files exist
touch agents/__init__.py world/__init__.py llm/__init__.py

# Run from the commune directory (not subdirectories)
cd /path/to/commune
python run.py
```

### Problem: PettingZoo version crashes

**Solution:**
```bash
# Reinstall PettingZoo and gymnasium
pip install --upgrade pettingzoo gymnasium
```

### Problem: Ollama responses are slow

**Solutions:**
1. Use a smaller model: `ollama pull gemma2:2b`
2. Reduce number of agents (edit `run.py`)
3. Increase timeout in `ollama_client.py`

### Problem: Out of memory

**Solutions:**
1. Use smaller model: `gemma2:2b` instead of `llama3.2:3b`
2. Close other applications
3. Restart your computer
4. Use PettingZoo version (much lower memory)

---

## 📚 Next Steps

### 1. Run Both Versions

```bash
# Terminal 1: PettingZoo (fast)
python commune_pettingzoo.py

# Terminal 2: Ollama (creative)  
python run.py
```

Compare the outputs!

### 2. Customize Agents

**PettingZoo:** Edit role behaviors in `commune_pettingzoo.py`
```python
def _sociologist_plan(self, ...):
    # Add your custom logic here
```

**Ollama:** Modify prompts in `agents/agent.py` and `agents/reflection.py`
```python
prompt = f"""You are {self.name}, a {self.role} who loves art.
Your current plan: {self.plan}
What do you do next?"""
```

### 3. Experiment with Models

```bash
# Try different Ollama models
ollama pull mistral:7b
ollama pull phi3:mini

# Edit run.py to use new model
llm_client = OllamaClient(model="mistral:7b")
```

### 4. Extend Functionality

- Add new agent roles
- Create custom projects
- Implement voting systems
- Add visualization
- Export to different formats

---

## 🎓 Learning Path

### Day 1: Basics
- Run PettingZoo version
- Read through the code
- Understand agent roles
- Watch secretary reports

### Day 2: Ollama
- Install Ollama
- Run Ollama version
- Compare outputs
- Experiment with prompts

### Day 3: Customization
- Add a new agent role
- Modify agent behaviors
- Create custom projects
- Try different LLM models

### Week 2: Advanced
- Integrate visualization
- Add database storage
- Implement voting
- Create web dashboard

---

## 📖 Documentation Reference

| File | Purpose |
|------|---------|
| `README.md` | Overview and architecture |
| `README_PETTINGZOO.md` | PettingZoo specifics |
| `QUICKSTART.md` | Quick start (5 min) |
| `COMPARISON.md` | Version comparison |
| `SETUP_GUIDE.md` | Complete setup (this file) |

---

## 💡 Pro Tips

1. **Start with PettingZoo** - Faster to test, easier to debug
2. **Use CLI tool** - Great for inspecting agent memories
3. **Keep Ollama running** - Faster startup times
4. **Watch the logs** - Use `tail -f data/logs/*.log`
5. **Experiment freely** - Memory files are small, easy to reset
6. **Read the code** - It's well-commented and educational
7. **Join discussions** - Share your findings!

---

## 🆘 Getting Help

### Check the Docs First
- Review README files
- Check troubleshooting sections
- Read code comments

### Common Issues
- 90% of problems are environment/dependencies
- Always activate virtual environment
- Check Ollama is running (for Ollama version)

### Debug Mode
```bash
# Enable detailed logging
export LOG_LEVEL=DEBUG
python run.py
```

---

## ✨ You're Ready!

Your AI commune is set up and ready to run. Start with:

```bash
# Quick test (30 seconds)
python commune_pettingzoo.py

# Full experience (3-5 minutes)
python run.py
```

**Happy experimenting! 🚀**
