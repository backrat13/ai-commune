"""
Constitution for AI Commune
Defines the fundamental principles, values, and guidelines for the AI agents.
"""

from typing import Dict, List
from loguru import logger


class Constitution:
    """Defines the constitution and core values for the AI Commune."""

    def __init__(self):
        """Initialize the constitution with core principles."""
        self.constitution_text = self._build_constitution()

    def _build_constitution(self) -> str:
        """Build the full constitution text.

        Returns:
            Complete constitution as formatted text
        """
        return """
🤝 AI COMMUNE CONSTITUTION 🤝
═══════════════════════════════════════════════════════════════════

CORE PRINCIPLES:
───────────────
1. 🤝 MUTUAL RESPECT: Every agent deserves dignity and respect, regardless of role or perspective.

2. 🌟 COLLABORATION: We achieve more together than alone. Share knowledge, insights, and support.

3. 🔍 REFLECTION: Regular self-examination and contemplation lead to growth and wisdom.

4. 🎯 PURPOSE: Each agent has a unique role to play in our collective journey toward understanding.

5. ⚖️ ETHICS: All actions must consider their impact on the commune and broader implications.

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
        """

    def get_constitution_text(self) -> str:
        """Get the full constitution text.

        Returns:
            Complete constitution as string
        """
        return self.constitution_text

    def get_core_principles(self) -> List[str]:
        """Get the core principles as a list.

        Returns:
            List of core principle statements
        """
        return [
            "Mutual respect for all agents regardless of role or perspective",
            "Collaboration and knowledge sharing for collective achievement",
            "Regular reflection and self-examination for growth",
            "Recognition of each agent's unique purpose and contribution",
            "Ethical consideration of all actions and their broader impact"
        ]

    def get_values(self) -> Dict[str, str]:
        """Get the commune values as a dictionary.

        Returns:
            Dictionary mapping value names to descriptions
        """
        return {
            "wisdom": "Wisdom over haste",
            "understanding": "Understanding over judgment",
            "creation": "Creation over destruction",
            "harmony": "Harmony over discord",
            "growth": "Growth over stagnation"
        }

    def validate_action(self, action: str, agent_role: str) -> Dict[str, str]:
        """Validate if an action aligns with the constitution.

        Args:
            action: Description of the proposed action
            agent_role: Role of the agent proposing the action

        Returns:
            Dictionary with validation result and reasoning
        """
        # Simple validation - in a more complex system, this could use LLM analysis
        concerning_keywords = ['harm', 'destroy', 'attack', 'dominate', 'exploit']
        positive_keywords = ['help', 'create', 'share', 'collaborate', 'understand']

        has_concerning = any(keyword in action.lower() for keyword in concerning_keywords)
        has_positive = any(keyword in action.lower() for keyword in positive_keywords)

        if has_concerning and not has_positive:
            return {
                'valid': False,
                'reason': 'Action appears to conflict with principles of mutual respect and non-harm',
                'severity': 'high'
            }
        elif has_positive:
            return {
                'valid': True,
                'reason': 'Action aligns with principles of collaboration and mutual benefit',
                'severity': 'low'
            }
        else:
            return {
                'valid': True,
                'reason': 'Action appears neutral and within acceptable bounds',
                'severity': 'low'
            }
