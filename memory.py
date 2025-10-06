"""
Simple Memory System for AI Agents
Provides basic memory storage and retrieval for agent reflections and interactions.
"""

from typing import Dict, List, Any
from datetime import datetime
from loguru import logger


class SimpleMemory:
    """Simple memory system for storing agent experiences and reflections."""

    def __init__(self, agent_name: str, max_entries: int = 100):
        """Initialize memory for an agent.

        Args:
            agent_name: Name of the agent this memory belongs to
            max_entries: Maximum number of memory entries to keep (default: 100)
        """
        self.agent_name = agent_name
        self.max_entries = max_entries
        self.memories: List[Dict[str, Any]] = []

    def add_memory(self, memory_type: str, content: str, metadata: Dict[str, Any] = None) -> None:
        """Add a new memory entry.

        Args:
            memory_type: Type of memory (e.g., 'reflection', 'interaction', 'observation')
            content: The memory content
            metadata: Additional metadata for the memory
        """
        memory_entry = {
            'timestamp': datetime.now().isoformat(),
            'type': memory_type,
            'content': content,
            'metadata': metadata or {}
        }

        self.memories.append(memory_entry)

        # Keep only the most recent entries
        if len(self.memories) > self.max_entries:
            self.memories = self.memories[-self.max_entries:]

        logger.debug(f"[{self.agent_name}] Added {memory_type} memory: {content[:50]}...")

    def get_recent_memories(self, n: int = 5, memory_type: str = None) -> List[Dict[str, Any]]:
        """Get recent memories, optionally filtered by type.

        Args:
            n: Number of memories to retrieve
            memory_type: Optional filter for memory type

        Returns:
            List of recent memory entries
        """
        if memory_type:
            filtered = [m for m in self.memories if m['type'] == memory_type]
            return filtered[-n:]
        return self.memories[-n:]

    def get_memories_by_type(self, memory_type: str) -> List[Dict[str, Any]]:
        """Get all memories of a specific type.

        Args:
            memory_type: Type of memories to retrieve

        Returns:
            List of memories of the specified type
        """
        return [m for m in self.memories if m['type'] == memory_type]

    def get_stats(self) -> Dict[str, Any]:
        """Get memory statistics.

        Returns:
            Dictionary with memory statistics
        """
        if not self.memories:
            return {'total_memories': 0, 'types': {}}

        type_counts = {}
        for memory in self.memories:
            mem_type = memory['type']
            type_counts[mem_type] = type_counts.get(mem_type, 0) + 1

        return {
            'total_memories': len(self.memories),
            'types': type_counts,
            'oldest_memory': self.memories[0]['timestamp'] if self.memories else None,
            'newest_memory': self.memories[-1]['timestamp'] if self.memories else None
        }

    def clear_memory(self, memory_type: str = None) -> None:
        """Clear memories, optionally filtered by type.

        Args:
            memory_type: Optional filter for memory type to clear
        """
        if memory_type:
            self.memories = [m for m in self.memories if m['type'] != memory_type]
            logger.info(f"[{self.agent_name}] Cleared {memory_type} memories")
        else:
            self.memories.clear()
            logger.info(f"[{self.agent_name}] Cleared all memories")

    def __len__(self) -> int:
        """Return the number of memories stored."""
        return len(self.memories)
