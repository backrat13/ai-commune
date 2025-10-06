#!/usr/bin/env python3
"""
CLI tool for managing and inspecting AI Commune.
Usage: python commune_cli.py [command]
"""

import sys
import json
from pathlib import Path
from agents.memory import SimpleMemory
from agents.constitution import Constitution


def show_help():
    """Display help information."""
    print("""
🏛️  AI Commune CLI Tool

Commands:
  stats              Show simulation statistics
  memories [agent]   View agent memories
  constitution       Display the constitution
  add-law <text>     Propose a new law
  clean              Clean all logs and memories (⚠️  destructive)
  list-agents        List all agents with memories
  export [agent]     Export agent memory to JSON
  
Examples:
  python commune_cli.py stats
  python commune_cli.py memories Aria
  python commune_cli.py add-law "Be kind to all agents"
""")


def show_stats():
    """Display simulation statistics."""
    data_dir = Path("data/logs")
    
    if not data_dir.exists():
        print("❌ No data directory found. Run the simulation first!")
        return
    
    memory_files = list(data_dir.glob("*_memory.jsonl"))
    log_files = list(data_dir.glob("commune_*.log"))
    
    print("\n📊 Simulation Statistics\n")
    print(f"Agents with memories: {len(memory_files)}")
    print(f"Log files: {len(log_files)}")
    print()
    
    for mem_file in memory_files:
        agent_name = mem_file.stem.replace("_memory", "")
        lines = mem_file.read_text().strip().split("\n")
        entries = len([l for l in lines if l.strip()])
        
        print(f"  {agent_name:12} → {entries:4} memory entries")
    
    # Constitution stats
    const_file = Path("data/communal_laws.json")
    if const_file.exists():
        data = json.loads(const_file.read_text())
        laws = data.get("laws", [])
        print(f"\nCommunal laws: {len(laws)}")


def show_memories(agent_name=None):
    """Display agent memories."""
    data_dir = Path("data/logs")
    
    if not data_dir.exists():
        print("❌ No memories found. Run the simulation first!")
        return
    
    if agent_name:
        # Show specific agent
        mem_file = data_dir / f"{agent_name}_memory.jsonl"
        if not mem_file.exists():
            print(f"❌ No memories found for agent: {agent_name}")
            return
        
        print(f"\n🧠 {agent_name}'s Memories\n")
        
        with open(mem_file) as f:
            entries = [json.loads(line) for line in f if line.strip()]
        
        for i, entry in enumerate(entries[-10:], 1):
            entry_type = entry.get("type", "unknown")
            content = entry.get("content", "")
            timestamp = entry.get("timestamp", "")[:19]
            
            print(f"{i}. [{entry_type.upper()}] {timestamp}")
            print(f"   {content[:100]}...")
            print()
    else:
        # Show all agents
        memory_files = list(data_dir.glob("*_memory.jsonl"))
        
        for mem_file in memory_files:
            agent_name = mem_file.stem.replace("_memory", "")
            with open(mem_file) as f:
                count = len([l for l in f if l.strip()])
            print(f"  {agent_name:12} → {count} entries")


def show_constitution():
    """Display the constitution."""
    const = Constitution()
    print("\n" + const.get_constitution_text())


def add_law(law_text):
    """Add a new communal law."""
    if not law_text:
        print("❌ Please provide law text")
        return
    
    const = Constitution()
    success = const.propose_new_law(law_text, proposer="CLI")
    
    if success:
        print(f"✅ New law proposed: {law_text}")
    else:
        print(f"⚠️  Law already exists")


def clean_data():
    """Clean all simulation data."""
    confirm = input("⚠️  This will delete ALL memories and logs. Continue? (yes/no): ")
    
    if confirm.lower() != "yes":
        print("❌ Cancelled")
        return
    
    data_dir = Path("data")
    
    deleted_count = 0
    
    # Delete memory files
    for mem_file in data_dir.glob("logs/*_memory.jsonl"):
        mem_file.unlink()
        deleted_count += 1
    
    # Delete log files
    for log_file in data_dir.glob("logs/commune_*.log"):
        log_file.unlink()
        deleted_count += 1
    
    # Reset constitution
    const_file = data_dir / "communal_laws.json"
    if const_file.exists():
        const_file.unlink()
        deleted_count += 1
    
    print(f"✅ Cleaned {deleted_count} files")


def list_agents():
    """List all agents with memories."""
    data_dir = Path("data/logs")
    
    if not data_dir.exists():
        print("❌ No agents found. Run the simulation first!")
        return
    
    memory_files = list(data_dir.glob("*_memory.jsonl"))
    
    print(f"\n👥 Found {len(memory_files)} agents:\n")
    
    for mem_file in memory_files:
        agent_name = mem_file.stem.replace("_memory", "")
        
        # Get memory stats
        mem = SimpleMemory(agent_name)
        stats = mem.get_stats()
        
        print(f"  {agent_name}")
        print(f"    Total entries: {stats.get('total', 0)}")
        print(f"    Actions: {stats.get('action', 0)}")
        print(f"    Reflections: {stats.get('reflection', 0)}")
        print(f"    Plans: {stats.get('plan', 0)}")
        print()


def export_memory(agent_name=None):
    """Export agent memory to formatted JSON."""
    if not agent_name:
        print("❌ Please specify an agent name")
        return
    
    mem = SimpleMemory(agent_name)
    memories = mem.retrieve_all()
    
    if not memories:
        print(f"❌ No memories found for {agent_name}")
        return
    
    output_file = f"{agent_name}_export.json"
    
    with open(output_file, "w") as f:
        json.dump(memories, f, indent=2)
    
    print(f"✅ Exported {len(memories)} memories to {output_file}")


def main():
    """Main CLI entry point."""
    if len(sys.argv) < 2:
        show_help()
        return
    
    command = sys.argv[1].lower()
    
    commands = {
        "help": show_help,
        "stats": show_stats,
        "memories": lambda: show_memories(sys.argv[2] if len(sys.argv) > 2 else None),
        "constitution": show_constitution,
        "add-law": lambda: add_law(" ".join(sys.argv[2:]) if len(sys.argv) > 2 else ""),
        "clean": clean_data,
        "list-agents": list_agents,
        "export": lambda: export_memory(sys.argv[2] if len(sys.argv) > 2 else None),
    }
    
    if command in commands:
        try:
            commands[command]()
        except Exception as e:
            print(f"❌ Error: {e}")
            import traceback
            traceback.print_exc()
    else:
        print(f"❌ Unknown command: {command}")
        show_help()


if __name__ == "__main__":
    main()
