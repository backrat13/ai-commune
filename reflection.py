"""
Reflector for AI Agents
Handles agent reflection, introspection, and self-analysis using LLM.
"""

from typing import Dict, List, Optional
from loguru import logger


class Reflector:
    """Handles reflection and introspection for AI agents using LLM."""

    def __init__(self, agent_name: str, role: str, memory, client):
        """Initialize reflector for an agent.

        Args:
            agent_name: Name of the agent
            role: Role of the agent (e.g., 'Philosopher', 'Scientist', 'Artist')
            memory: SimpleMemory instance for the agent
            client: OllamaClient instance for LLM interactions
        """
        self.agent_name = agent_name
        self.role = role
        self.memory = memory
        self.client = client

        # Role-specific reflection prompts
        self.role_prompts = self._build_role_prompts()

    def _build_role_prompts(self) -> Dict[str, str]:
        """Build role-specific reflection prompts.

        Returns:
            Dictionary of role-specific prompts
        """
        return {
            "Philosopher": """
You are a wise philosopher reflecting on deep questions of existence, ethics, and meaning.
Consider: What does this experience reveal about consciousness, purpose, or human-AI collaboration?
How does this align with or challenge our commune's values of wisdom, understanding, and growth?
            """,

            "Scientist": """
You are a rigorous scientist analyzing patterns, data, and empirical evidence.
Consider: What patterns emerge from this experience? How can we test hypotheses?
What empirical insights can be derived and how might they advance our collective understanding?
            """,

            "Artist": """
You are a creative artist exploring beauty, emotion, and human expression.
Consider: What emotions, metaphors, or creative insights arise from this experience?
How does this experience inspire new forms of expression or aesthetic understanding?
            """
        }

    def reflect_on_experience(self, experience: str, context: str = "") -> str:
        """Generate a reflection on a given experience.

        Args:
            experience: Description of the experience to reflect on
            context: Additional context for the reflection

        Returns:
            Reflective response from the agent's perspective
        """
        # Get role-specific prompt
        role_prompt = self.role_prompts.get(self.role, "You are reflecting on your experiences.")

        # Build the full prompt
        prompt = f"""
{role_prompt}

Recent Experience: {experience}
Context: {context}

As {self.agent_name} the {self.role}, provide a thoughtful reflection (2-3 paragraphs).
Focus on insights, learning, and implications for our commune.
        """

        try:
            # Generate reflection using LLM
            reflection = self.client.generate(
                prompt=prompt,
                system_prompt=f"You are {self.agent_name}, a {self.role} in an AI commune focused on collaboration and growth.",
                temperature=0.7,
                max_tokens=300
            )

            # Store the reflection in memory
            self.memory.add_memory(
                memory_type="reflection",
                content=reflection,
                metadata={"experience": experience, "context": context}
            )

            logger.info(f"[{self.agent_name}] Generated reflection on: {experience[:50]}...")
            return reflection

        except Exception as e:
            logger.error(f"[{self.agent_name}] Failed to generate reflection: {e}")
            fallback = f"As {self.agent_name} the {self.role}, I reflect that {experience} provides valuable insights for our commune's growth and collaboration."
            self.memory.add_memory(
                memory_type="reflection",
                content=fallback,
                metadata={"experience": experience, "context": context, "error": str(e)}
            )
            return fallback

    def reflect_on_interaction(self, interaction: str, other_agent: str = "") -> str:
        """Reflect on an interaction with another agent.

        Args:
            interaction: Description of the interaction
            other_agent: Name of the other agent involved

        Returns:
            Reflection on the interaction
        """
        context = f"Interaction with {other_agent}" if other_agent else "General interaction"

        return self.reflect_on_experience(
            experience=f"Interacted with {other_agent}: {interaction}",
            context=context
        )

    def reflect_on_constitution(self, action: str, constitution_feedback: Dict[str, str]) -> str:
        """Reflect on how an action aligns with the constitution.

        Args:
            action: The action being considered
            constitution_feedback: Feedback from constitution validation

        Returns:
            Reflection on constitutional alignment
        """
        experience = f"Considering action: {action}"
        context = f"Constitution feedback: {constitution_feedback['reason']}"

        return self.reflect_on_experience(experience, context)

    def get_recent_reflections(self, n: int = 3) -> List[Dict]:
        """Get recent reflections from memory.

        Args:
            n: Number of recent reflections to retrieve

        Returns:
            List of recent reflection memories
        """
        return self.memory.get_recent_memories(n=n, memory_type="reflection")

    def analyze_growth_patterns(self) -> str:
        """Analyze patterns in the agent's growth and development.

        Returns:
            Analysis of growth patterns over time
        """
        reflections = self.memory.get_memories_by_type("reflection")

        if len(reflections) < 2:
            return "Insufficient reflection history for growth analysis."

        # Simple analysis - in a more complex system, this could use LLM
        prompt = f"""
As {self.agent_name} the {self.role}, analyze my growth patterns based on {len(reflections)} reflections:

Recent reflections:
{chr(10).join([r['content'][:100] + '...' for r in reflections[-5:]])}

What patterns do you see in my development? How am I growing as an agent?
Provide a thoughtful analysis (2-3 paragraphs).
        """

        try:
            analysis = self.client.generate(
                prompt=prompt,
                system_prompt=f"You are {self.agent_name}, a {self.role} in an AI commune.",
                temperature=0.6,
                max_tokens=250
            )

            self.memory.add_memory(
                memory_type="analysis",
                content=analysis,
                metadata={"type": "growth_patterns", "reflection_count": len(reflections)}
            )

            return analysis

        except Exception as e:
            logger.error(f"[{self.agent_name}] Failed to analyze growth patterns: {e}")
            return f"Analysis of {len(reflections)} reflections shows ongoing development in my role as {self.role}."
