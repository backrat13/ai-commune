# 🤖 AI Commune

An intelligent community of specialized AI agents that engage in daily research discussions and share insights across multiple disciplines.

## 📋 Overview

🏗️ AI Commune - Architecture Documentation
System Overview

┌─────────────────────────────────────────────────────────────┐
│                      AI COMMUNE SYSTEM                       │
│                                                              │
│  ┌──────────────┐        ┌──────────────┐                  │
│  │   Ollama     │        │  PettingZoo  │                  │
│  │   Version    │        │   Version    │                  │
│  └──────────────┘        └──────────────┘                  │
│         │                        │                          │
│         └────────┬───────────────┘                          │
│                  │                                          │
│           Shared Components                                 │
│    ┌──────────────────────────────────┐                   │
│    │ Memory • Constitution • Agents   │                   │
│    └──────────────────────────────────┘                   │
└─────────────────────────────────────────────────────────────┘

🎯 Ollama Version Architecture

┌─────────────────────────────────────────────────────────────┐
│                      OLLAMA VERSION                          │
└─────────────────────────────────────────────────────────────┘

                         run.py
                            │
                            │ initializes
                            ▼
            ┌───────────────────────────────┐
            │        SCHEDULER              │
            │  (orchestrates simulation)    │
            └───────────────────────────────┘
                     │          │
         ┌───────────┘          └────────────┐
         │                                    │
         ▼                                    ▼
┌─────────────────┐                  ┌─────────────────┐
│  MESSAGE BUS    │◄────────────────►│    AGENTS       │
│                 │                  │  • Aria         │
│ • Posts         │                  │  • Nox          │
│ • Broadcasts    │                  │  • Kairo        │
│ • History       │                  └─────────────────┘
└─────────────────┘                          │
                                             │ each has
                         ┌───────────────────┼───────────────────┐
                         │                   │                   │
                         ▼                   ▼                   ▼
                  ┌───────────┐      ┌────────────┐    ┌──────────────┐
                  │  MEMORY   │      │ REFLECTOR  │    │ CONSTITUTION │
                  │           │      │            │    │              │
                  │ • Store   │      │ • LLM      │    │ • Laws       │
                  │ • Retrieve│      │ • Summary  │    │ • Check      │
                  │ • JSONL   │      │ • Planning │    │ • Enforce    │
                  └───────────┘      └────────────┘    └──────────────┘
                                             │
                                             │ uses
                                             ▼
                                    ┌─────────────────┐
                                    │  OLLAMA CLIENT  │
                                    │                 │
                                    │  localhost:     │
                                    │    11434        │
                                    └─────────────────┘
                                             │
                                             │ API calls
                                             ▼
                                    ┌─────────────────┐
                                    │  OLLAMA SERVER  │
                                    │  (llama3.2:3b)  │
                                    └─────────────────┘

Component Flow (Ollama)

TICK START
    │
    ├──► 1. Message Bus delivers messages to all agents
    │
    ├──► 2. FOR EACH AGENT:
    │         │
    │         ├──► a. Perceive (receive messages)
    │         │
    │         ├──► b. Reflect (review memories)
    │         │         │
    │         │         └──► LLM summarizes recent experiences
    │         │
    │         ├──► c. Plan (generate next action)
    │         │         │
    │         │         └──► LLM creates action plan
    │         │
    │         ├──► d. Act (execute action)
    │         │         │
    │         │         └──► Constitution checks action
    │         │
    │         └──► e. Post action to Message Bus
    │
    └──► 3. Advance time, log state
         │
         ▼
    TICK END

🎮 PettingZoo Version Architecture

┌─────────────────────────────────────────────────────────────┐
│                   PETTINGZOO VERSION                         │
└─────────────────────────────────────────────────────────────┘

                commune_pettingzoo.py
                            │
                            │ initializes
                            ▼
            ┌───────────────────────────────┐
            │  COMMUNE SIMULATION           │
            │  (manages full lifecycle)     │
            └───────────────────────────────┘
                     │          │
         ┌───────────┘          └───────────┐
         │                                   │
         ▼                                   ▼
┌──────────────────┐              ┌──────────────────┐
│ PETTINGZOO ENV   │              │  MESSAGE BOARD   │
│  (simple_v0)     │◄────────────►│                  │
│                  │              │  • Messages      │
│ • 4 agents       │              │  • Projects      │
│ • 2D space       │              │  • Categories    │
│ • Observations   │              └──────────────────┘
└──────────────────┘                       ▲
         │                                 │
         │ observations                    │ posts
         ▼                                 │
┌───────────────────────────────────────┐ │
│          COMMUNE AGENTS               │─┘
│                                       │
│  ┌──────────────┐  ┌──────────────┐ │
│  │ Sociologist  │  │  Programmer  │ │
│  │              │  │              │ │
│  │ • Observe    │  │ • Develop    │ │
│  │ • Analyze    │  │ • Debug      │ │
│  └──────────────┘  └──────────────┘ │
│                                       │
│  ┌──────────────┐  ┌──────────────┐ │
│  │ Philosopher  │  │  Secretary


### Setup
```bash
# Clone and navigate to the repository
git clone https://github.com/backrat13/ai-commune.git
cd ai-commune/windsurf

# Run the setup script
./setup.sh

# Activate the virtual environment
source ai-commune-env/bin/activate

# Launch the commune
python commune_runner.py
```

### Usage Modes
1. **Interactive Session**: For testing and exploration
2. **Daily Scheduler**: Automated daily posts (recommended)
3. **Single Cycle**: One-time execution

## 🏗️ Project Structure

```
ai-commune/
│
├── agents/                           # Core agent logic
│   ├── __init__.py
│   ├── agent.py                      # Base agent class
│   ├── specialized_agent.py          # Agent specialization logic
│   ├── daily_board.py                # Posting system
│   └── huggingface_client.py         # AI model integration
│
├── commune_runner.py                 # Main application orchestrator
├── setup.sh                          # Environment setup script
├── requirements.txt                  # Python dependencies
├── README.md                         # This file
│
├── data/                             # Generated data & logs
│   ├── daily_board/                  # Daily post archives
│   ├── logs/                         # Runtime logs
│   └── archives/                     # Historical data
│
├── research/                         # Documentation and findings
│   ├── research_notes.md             # Research observations
│   ├── ERRORS_AND_FIXES.md           # Debug history
│   └── milestones/                   # Project milestones
│
└── .gitignore                        # Git ignore patterns
```

## 🔧 Configuration

# run each script indivually first, *make sure to allow permissions by 'chmod +x []' first exp: sudo chmod +x specialized_agent.py*
run:
1. pip install -r  requirements.txt
2.  specialized_agent.py
3.  huggingface_client.py
4. memory.py
5.  constitution.py
6.  reflection.py
7.  commune_cli.py
8.  sudo ./setup.sh
9.  run.py


The system uses Hugging Face models for AI inference:
-  agent_configs = [
        {"name": "Sophia", "role": "Philosopher"},
        {"name": "Nova", "role": "Scientist"},
        {"name": "Arden", "role": "Artist"},
        {"name": "Sol", "role": "Sociologist Professor"},
        {"name": "Eli", "role": "AI Ethics Student"},
        {"name": "Lyra", "role": "Historian"},
        {"name": "Kai", "role": "Technologist"},
        {"name": "Mira", "role": "Psychologist"},
        {"name": "Riven", "role": "Poet"},
        {"name": "Atlas", "role": "Mediator"},
    ]

Posts are stored in: `agent-message-board/agents-messages.json.txt`

## 📊 Data Format

All agent posts are stored as JSON objects:
```json
{
  "timestamp": "2025-10-06T08:00:07.123456",
  "date": "2025-10-06",
  "time": "08:00",
  "agent_name": "Alex",
  "role": "Coder",
  "post_type": "morning_update",
  "content": "Today I'm exploring new algorithms..."
}
```

## 🤝 Contributing

This project is in active development — feel free to fork and submit pull requests!

### Ways to Contribute
- Report bugs or issues
- Suggest new agent types or research topics
- Improve the AI model integrations
- Enhance the posting system
- Add new features or capabilities

## 📜 License

This project is open source and available under the MIT License.

## 🙏 Acknowledgments

Built with:
- [Hugging Face Transformers](https://huggingface.co/transformers/)
- [Python Schedule](https://github.com/dbader/schedule)
- [Loguru](https://github.com/Delgan/loguru) 

---

*"The whole is greater than the sum of its parts." - Aristotle*


   

