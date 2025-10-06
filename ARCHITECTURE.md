# 🏗️ AI Commune - Architecture Documentation

## System Overview

```
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
```

---

## 🎯 Ollama Version Architecture

```
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
```

### Component Flow (Ollama)

```
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
```

---

## 🎮 PettingZoo Version Architecture

```
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
