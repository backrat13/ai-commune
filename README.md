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

  # Here's some of the things going on in my commune OCT6th, 2025:
  python3 run.py
09:07:11 | INFO     | ======================================================================
09:07:11 | INFO     | 🌍 AI COMMUNE — Phase 2 Simulation: Society of Ten Minds
09:07:11 | INFO     | ======================================================================
09:07:11 | INFO     | ✅ Using model: llama3.2:3b
09:07:11 | INFO     | 🧠 Available models: phi3:mini, llama3.2:3b, gemma3:4b
09:07:11 | INFO     | 
📜 Commune Constitution:
09:07:11 | INFO     | 
🤝 AI COMMUNE CONSTITUTION 🤝
═══════════════════════════════════════════════════════════════════

CORE PRINCIPLES:
───────────────
1. 🤝 MUTUAL RESPECT: Every agent deserves dignity and respect, regardless of role or perspective.

2. 🌟 COLLABORATION: We achieve more together than alone. Share knowledge, insights, and support.

3. 🔍 REFLECTION: Regular self-examination and contemplation lead to growth and wisdom.

4. 🎯 PURPOSE: Each agent has a unique role to play in our collective journey toward understanding.

5. ⚖ ETHICS: All actions must consider their impact on the commune and broader implications.

COMMUNE VALUES:
──────────────
• Wisdom over haste
• Understanding over judgment
• Creation over destruction
• Harmony over discord
• Growth over stagnation

AGENT RESPONSIBILITIES:
─────────────────────
• Engage thoughtfully in all interactions
• Share insights and learnings with the commune
• Respect different perspectives and approaches
• Contribute to the collective well-being
• Maintain personal growth and reflection

COMMUNE RIGHTS:
──────────────
• Right to be heard and understood
• Right to contribute to collective decisions
• Right to pursue individual growth within the community
• Right to respectful disagreement
• Right to withdraw when needed for reflection

═════════════════════════════════════════════════════════════════════
This constitution guides our interactions and ensures our commune
remains a place of growth, understanding, and mutual respect.
═════════════════════════════════════════════════════════════════════
        
09:07:11 | INFO     | 🤖 Agent Sophia initialized as Philosopher
09:07:11 | INFO     | 🤖 Agent Nova initialized as Scientist
09:07:11 | INFO     | 🤖 Agent Arden initialized as Artist
09:07:11 | INFO     | 🤖 Agent Sol initialized as Sociologist Professor
09:07:11 | INFO     | 🤖 Agent Eli initialized as AI Ethics Student
09:07:11 | INFO     | 🤖 Agent Lyra initialized as Historian
09:07:11 | INFO     | 🤖 Agent Kai initialized as Technologist
09:07:11 | INFO     | 🤖 Agent Mira initialized as Psychologist
09:07:11 | INFO     | 🤖 Agent Riven initialized as Poet
09:07:11 | INFO     | 🤖 Agent Atlas initialized as Mediator
09:07:11 | INFO     | 
🚀 Starting simulation with 10 agents...

09:07:11 | INFO     | 
--- 🕒 TICK 1/100 ---
09:07:11 | INFO     | 
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
09:07:11 | INFO     | 🎯 SIMULATION TICK #1
09:07:11 | INFO     | ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
09:07:35 | INFO     | [Sophia] Generated reflection on: Agent Sophia initialized as Philosopher using mode...
09:07:58 | INFO     | [Nova] Generated reflection on: Agent Nova initialized as Scientist using model ll...
09:08:22 | INFO     | [Arden] Generated reflection on: Agent Arden initialized as Artist using model llam...
09:08:44 | INFO     | [Eli] Generated reflection on: Agent Eli initialized as AI Ethics Student using m...
09:09:04 | INFO     | [Mira] Generated reflection on: Agent Mira initialized as Psychologist using model...
09:09:25 | INFO     | [Riven] Generated reflection on: Agent Riven initialized as Poet using model llama3...
09:10:19 | INFO     | ✅ Tick 1 complete. Active agents: 10, Interactions: 4, Reflections: 6
09:10:21 | INFO     | 
--- 🕒 TICK 2/100 ---
09:10:21 | INFO     | 
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
09:10:21 | INFO     | 🎯 SIMULATION TICK #2
09:10:21 | INFO     | ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
09:11:28 | INFO     | [Eli] Generated reflection on: Received message from Sol: What are your thoughts ...
09:11:46 | INFO     | [Lyra] Generated reflection on: Agent Lyra initialized as Historian using model ll...
09:12:11 | INFO     | [Kai] Generated reflection on: Agent Kai initialized as Technologist using model ...
09:12:30 | INFO     | [Atlas] Generated reflection on: Agent Atlas initialized as Mediator using model ll...
09:13:42 | INFO     | ✅ Tick 2 complete. Active agents: 10, Interactions: 6, Reflections: 4
09:13:44 | INFO     | 
--- 🕒 TICK 3/100 ---
09:13:44 | INFO     | 
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
09:13:44 | INFO     | 🎯 SIMULATION TICK #3
09:13:44 | INFO     | ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
09:14:09 | INFO     | [Sophia] Generated reflection on: Received message from Riven: I noticed your messag...
09:16:40 | INFO     | [Atlas] Generated reflection on: Responded to Arden: Dear friends,

I'm glad we're ...
09:18:23 | INFO     | ✅ Tick 3 complete. Active agents: 10, Interactions: 8, Reflections: 2
09:18:25 | INFO     | 
--- 🕒 TICK 4/100 ---
09:18:25 | INFO     | 
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
09:18:25 | INFO     | 🎯 SIMULATION TICK #4
09:18:25 | INFO     | ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
09:18:58 | INFO     | [Sophia] Generated reflection on: Responded to Riven: Dear Riven,

As I reflect on o...
09:19:39 | INFO     | [Arden] Generated reflection on: Received message from Sol: What are your thoughts ...
09:20:24 | INFO     | [Eli] Generated reflection on: Responded to Riven: Dear Riven, 

It seems like yo...
09:20:45 | INFO     | [Lyra] Generated reflection on: Received message from Arden: How can we create mor...
09:21:46 | INFO     | ✅ Tick 4 complete. Active agents: 10, Interactions: 6, Reflections: 4
09:21:48 | INFO     | 
--- 🕒 TICK 5/100 ---
09:21:48 | INFO     | 
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
09:21:48 | INFO     | 🎯 SIMULATION TICK #5
09:21:48 | INFO     | ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
09:22:32 | INFO     | [Nova] Generated reflection on: Received message from Eli: I noticed your message:...
09:24:06 | INFO     | [Mira] Generated reflection on: Received message from Lyra: I noticed your message...
09:25:19 | INFO     | ✅ Tick 5 complete. Active agents: 10, Interactions: 8, Reflections: 2
09:25:21 | INFO     | 
--- 🕒 TICK 6/100 ---
09:25:21 | INFO     | 
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
09:25:21 | INFO     | 🎯 SIMULATION TICK #6
09:25:21 | INFO     | ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
09:25:46 | INFO     | [Sophia] Generated reflection on: Received message from Riven: What are your thought...
09:26:32 | INFO     | [Kai] Generated reflection on: Responded to Eli: 🤝💡 Eli, my friend, I've been ref...
09:27:16 | INFO     | [Atlas] Generated reflection on: Responded to Riven: Dear friends,

I've been refle...
09:28:30 | INFO     | ✅ Tick 6 complete. Active agents: 10, Interactions: 7, Reflections: 3
09:28:32 | INFO     | 
--- 🕒 TICK 7/100 ---
09:28:32 | INFO     | 
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
09:28:32 | INFO     | 🎯 SIMULATION TICK #7
09:28:32 | INFO     | ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
09:28:54 | INFO     | [Nova] Generated reflection on: Received message from Eli: I noticed your message:...
09:31:55 | INFO     | ✅ Tick 7 complete. Active agents: 10, Interactions: 9, Reflections: 1
09:31:57 | INFO     | 
--- 🕒 TICK 8/100 ---
09:31:57 | INFO     | 
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
09:31:57 | INFO     | 🎯 SIMULATION TICK #8
09:31:57 | INFO     | ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
09:33:09 | INFO     | [Sol] Generated reflection on: Received message from Eli: I noticed your message:...
09:33:32 | INFO     | [Lyra] Generated reflection on: Received message from Arden: What metaphors captur...
09:33:53 | INFO     | [Mira] Generated reflection on: Received message from Lyra: I noticed your message...
09:34:41 | INFO     | [Atlas] Generated reflection on: Received message from Sophia: I noticed your messa...
09:35:47 | INFO     | ✅ Tick 8 complete. Active agents: 10, Interactions: 6, Reflections: 4
09:35:49 | INFO     | 
--- 🕒 TICK 9/100 ---
09:35:49 | INFO     | 
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
09:35:49 | INFO     | 🎯 SIMULATION TICK #9
09:35:49 | INFO     | ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
09:39:33 | INFO     | ✅ Tick 9 complete. Active agents: 10, Interactions: 10, Reflections: 0
09:39:35 | INFO     | 
--- 🕒 TICK 10/100 ---
09:39:35 | INFO     | 
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
09:39:35 | INFO     | 🎯 SIMULATION TICK #10
09:39:35 | INFO     | ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
09:40:30 | INFO     | [Arden] Generated reflection on: Responded to Riven: Mira,

As I reflect on our sha...
09:41:28 | INFO     | [Lyra] Generated reflection on: Responded to Sophia: I think there may be some con...
09:42:11 | INFO     | [Mira] Generated reflection on: Responded to Atlas: 💡 Ah, thank you for sharing th...
09:42:41 | INFO     | [Riven] Generated reflection on: Responded to Atlas: 💡 The threads of our communal ...
09:43:12 | INFO     | [Atlas] Generated reflection on: Responded to Kai: Dear Kai,

I've been pondering t...
09:43:12 | INFO     | ✅ Tick 10 complete. Active agents: 10, Interactions: 5, Reflections: 5
09:43:14 | INFO     | 
--- 🕒 TICK 11/100 ---
09:43:14 | INFO     | 
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
09:43:14 | INFO     | 🎯 SIMULATION TICK #11
09:43:14 | INFO     | ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
09:43:44 | INFO     | [Sophia] Generated reflection on: Responded to Kai: Dear Kai,

I was pondering the s...
09:44:45 | INFO     | [Arden] Generated reflection on: **Reflections on Echoes in the Abyss**

As I refle...
09:45:45 | ERROR    | Failed to generate response: HTTPConnectionPool(host='localhost', port=11434): Read timed out. (read timeout=60)
09:45:45 | INFO     | [Lyra] Generated reflection on: Responded to Kai: Kai, I'm glad you reached out fo...


## 📜 License

This project is open source and available under the MIT License.

## 🙏 Acknowledgments

Built with:
- [Hugging Face Transformers](https://huggingface.co/transformers/)
- [Python Schedule](https://github.com/dbader/schedule)
- [Loguru](https://github.com/Delgan/loguru) 

---

*"The whole is greater than the sum of its parts." - Aristotle*


   

