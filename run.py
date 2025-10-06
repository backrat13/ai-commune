"""
AI Commune – Phase 2 Simulation
Run: python commune_runner.py
"""

import sys
import time
from pathlib import Path
from loguru import logger

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent))

from agents.agent import Agent
from agents.memory import SimpleMemory
from agents.constitution import Constitution
from agents.reflection import Reflector
from world.message_bus import MessageBus
from world.scheduler import Scheduler
from llm.ollama_client import OllamaClient


def setup_logging():
    """Configure logging for the simulation."""
    log_dir = Path("data/logs")
    log_dir.mkdir(parents=True, exist_ok=True)

    logger.remove()
    logger.add(
        sys.stdout,
        format="<green>{time:HH:mm:ss}</green> | <level>{level: <8}</level> | <level>{message}</level>",
        level="INFO",
    )
    logger.add(
        log_dir / "commune_{time}.log",
        rotation="10 MB",
        level="DEBUG",
    )


def main():
    """Main simulation loop."""
    setup_logging()

    logger.info("=" * 70)
    logger.info("🌍 AI COMMUNE — Phase 2 Simulation: Society of Ten Minds")
    logger.info("=" * 70)

    # Initialize LLM client
    try:
        llm_client = OllamaClient(model="llama3.2:3b")
        logger.info(f"✅ Using model: {llm_client.model}")

        models = llm_client.list_models()
        if models:
            logger.info(f"🧠 Available models: {', '.join(models[:5])}")
    except Exception as e:
        logger.error(f"Failed to initialize Ollama: {e}")
        logger.error("Make sure Ollama is running: `ollama serve`")
        return

    # Initialize shared systems
    message_bus = MessageBus()
    constitution = Constitution()

    logger.info("\n📜 Commune Constitution:")
    logger.info(constitution.get_constitution_text())

    # --- PHASE 2: Ten Agent Roster ---
    agent_configs = [
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

    agents = []

    for config in agent_configs:
        name = config["name"]
        role = config["role"]

        memory = SimpleMemory(agent_name=name)
        reflector = Reflector(
            agent_name=name,
            role=role,
            memory=memory,
            client=llm_client,
        )

        agent = Agent(
            name=name,
            role=role,
            model=llm_client.model,
            memory=memory,
            constitution=constitution,
            reflector=reflector,
        )

        agents.append(agent)

    # Initialize scheduler
    scheduler = Scheduler(agents=agents, message_bus=message_bus)

    # Welcome message
    message_bus.post(
        "Welcome to Phase 2 of the AI Commune. "
        "Ten unique minds now share this digital habitat. "
        "Collaborate, question, and grow together.",
        sender="Commune",
    )

    logger.info(f"\n🚀 Starting simulation with {len(agents)} agents...\n")

    # --- Main Simulation Loop ---
    num_ticks = 100  # ⏱️ 100 ticks for Phase 2
    tick_delay = 2   # seconds between ticks

    try:
        for tick in range(1, num_ticks + 1):
            logger.info(f"\n--- 🕒 TICK {tick}/{num_ticks} ---")
            scheduler.tick()
            time.sleep(tick_delay)

        # --- End of Simulation Summary ---
        logger.info("\n" + "=" * 70)
        logger.info("🏁 SIMULATION COMPLETE — PHASE 2 SUMMARY")
        logger.info("=" * 70)

        stats = scheduler.get_stats()
        logger.info("\n📊 Simulation Statistics:")
        for key, value in stats.items():
            logger.info(f"  {key}: {value}")

        logger.info("\n🧠 Agent Summaries:")
        for agent in agents:
            logger.info(f"\n{agent.get_summary()}")
            logger.info(f"Memory Stats: {agent.memory.get_stats()}")

        logger.info("\n💬 Recent Message History:")
        for msg in message_bus.get_history(n=10):
            logger.info(f"  [{msg['sender']}] {msg['message'][:100]}...")

    except KeyboardInterrupt:
        logger.warning("\n⚠️  Simulation interrupted by user")
    except Exception as e:
        logger.error(f"❌ Simulation error: {e}")
        import traceback

        traceback.print_exc()
    finally:
        logger.info("\n🏁 AI Commune shutting down gracefully...")


if __name__ == "__main__":
    main()
