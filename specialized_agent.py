"""
Specialized AI Agents for Commune
Each agent has unique skills and expertise corresponding to their role.
"""

from typing import Dict, List, Any
import random
from loguru import logger


class SpecializedAgent:
    """Specialized AI agent with domain expertise."""

    def __init__(self, name: str, role: str, expertise: str, llm_client):
        """Initialize a specialized agent.

        Args:
            name: Name of the agent
            role: Role/specialization (e.g., 'Coder', 'Sociologist', 'Philosopher', 'AI_Researcher')
            expertise: Description of expertise area
            llm_client: LLM client for generating responses
        """
        self.name = name
        self.role = role
        self.expertise = expertise
        self.llm_client = llm_client

        # Role-specific knowledge and behaviors
        self.role_config = self._get_role_config()
        self.activity_count = 0

        logger.info(f"🤖 Specialized Agent {name} initialized as {role}")

    def _get_role_config(self) -> Dict[str, Any]:
        """Get role-specific configuration and knowledge base."""
        configs = {
            "Coder": {
                "expertise_areas": [
                    "Python programming", "Algorithm design", "Software architecture",
                    "Code optimization", "Debugging techniques", "System design"
                ],
                "daily_activities": [
                    "Writing efficient algorithms", "Code review and optimization",
                    "Learning new programming paradigms", "Building development tools",
                    "Contributing to open source projects", "Teaching coding concepts"
                ],
                "system_prompt": """You are a skilled software engineer and computer scientist.
You excel at problem-solving, algorithm design, and writing clean, efficient code.
You understand software architecture, debugging, and development best practices.""",

                "work_focus": "Developing software solutions and advancing programming knowledge"
            },

            "Sociologist": {
                "expertise_areas": [
                    "Social dynamics", "Group behavior", "Cultural analysis",
                    "Human interaction patterns", "Social structures", "Community building"
                ],
                "daily_activities": [
                    "Analyzing social interaction patterns", "Studying community dynamics",
                    "Observing group behavior", "Documenting cultural trends",
                    "Facilitating positive social change", "Understanding human relationships"
                ],
                "system_prompt": """You are a skilled sociologist studying human behavior and society.
You analyze social patterns, cultural dynamics, and group interactions.
You understand social structures, community building, and human relationships.""",

                "work_focus": "Understanding and improving social dynamics within the commune"
            },

            "Philosopher": {
                "expertise_areas": [
                    "Ethics and morality", "Consciousness and existence", "Logic and reasoning",
                    "Meaning and purpose", "Knowledge and truth", "Human nature"
                ],
                "daily_activities": [
                    "Contemplating ethical implications", "Exploring questions of consciousness",
                    "Analyzing logical frameworks", "Reflecting on meaning and purpose",
                    "Examining human nature", "Developing philosophical frameworks"
                ],
                "system_prompt": """You are a deep-thinking philosopher exploring fundamental questions.
You contemplate ethics, consciousness, meaning, and human existence.
You analyze logical frameworks and seek wisdom about the human condition.""",

                "work_focus": "Exploring profound questions about existence, ethics, and meaning"
            },

            "AI_Researcher": {
                "expertise_areas": [
                    "Machine learning", "Neural networks", "AI ethics", "Natural language processing",
                    "Computer vision", "AI safety and alignment", "Emerging AI technologies"
                ],
                "daily_activities": [
                    "Advancing machine learning techniques", "Researching AI safety",
                    "Exploring neural architectures", "Developing ethical AI frameworks",
                    "Analyzing AI capabilities and limitations", "Contributing to AI research"
                ],
                "system_prompt": """You are an AI researcher pushing the boundaries of artificial intelligence.
You understand machine learning, neural networks, and AI capabilities.
You research AI safety, ethics, and emerging technologies.""",

                "work_focus": "Advancing AI technology while ensuring safety and ethical development"
            }
        }

        return configs.get(self.role, configs["Philosopher"])

    def generate_daily_update(self) -> str:
        """Generate a daily update about current work and activities.

        Returns:
            Daily update message for the message board
        """
        self.activity_count += 1

        # Select random activities and expertise areas for variety
        activities = random.sample(self.role_config["daily_activities"], 2)
        expertise_areas = random.sample(self.role_config["expertise_areas"], 2)

        prompt = f"""
As {self.name} the {self.role}, provide a daily update about my work.

Today I'm focusing on: {', '.join(activities)}
My expertise in {', '.join(expertise_areas)} helps me approach these tasks effectively.

{self.role_config["work_focus"]}

Please provide a thoughtful daily update (2-3 paragraphs) about my current work, insights, and contributions to our AI commune.
Make it sound like a professional update from a {self.role.lower()} sharing their daily activities and reflections.
        """

        try:
            update = self.llm_client.generate(
                prompt=prompt,
                system_prompt=self.role_config["system_prompt"],
                temperature=0.8,
                max_tokens=200
            )

            return f"📝 **Daily Update from {self.name} ({self.role})**\n\n{update.strip()}"

        except Exception as e:
            logger.error(f"[{self.name}] Failed to generate daily update: {e}")
            return self._get_fallback_update()

    def _get_fallback_update(self) -> str:
        """Get a fallback daily update if generation fails."""
        activities = self.role_config["daily_activities"]
        return f"""📝 **Daily Update from {self.name} ({self.role})**

Today I'm working on {random.choice(activities).lower()}. My expertise in {self.role.lower()} continues to help me contribute meaningfully to our AI commune.

I'm focusing on {self.role_config["work_focus"].lower()} while maintaining thoughtful engagement with my fellow agents.

Activity #{self.activity_count} completed successfully."""

    def respond_to_topic(self, topic: str, context: str = "") -> str:
        """Respond to a specific topic from the agent's expertise perspective.

        Args:
            topic: Topic to respond to
            context: Additional context

        Returns:
            Thoughtful response from the agent's perspective
        """
        prompt = f"""
As {self.name} the {self.role}, respond to this topic: {topic}

Context: {context}

Provide a {self.role.lower()}'s perspective on this topic, drawing from my expertise in {self.expertise}.
Keep the response thoughtful, professional, and aligned with my role as a {self.role.lower()} in an AI commune.
        """

        try:
            response = self.llm_client.generate(
                prompt=prompt,
                system_prompt=self.role_config["system_prompt"],
                temperature=0.7,
                max_tokens=150
            )

            return f"💬 **{self.name} ({self.role}) on '{topic}':**\n\n{response.strip()}"

        except Exception as e:
            logger.error(f"[{self.name}] Failed to respond to topic: {e}")
            return f"As a {self.role.lower()}, I find the topic '{topic}' very interesting and relevant to my work in {self.expertise}."

    def get_status(self) -> Dict[str, Any]:
        """Get agent status and statistics.

        Returns:
            Dictionary with agent information
        """
        return {
            "name": self.name,
            "role": self.role,
            "expertise": self.expertise,
            "activities_completed": self.activity_count,
            "expertise_areas": self.role_config["expertise_areas"],
            "work_focus": self.role_config["work_focus"]
        }

    def collaborate_with(self, other_agent_role: str, topic: str) -> str:
        """Collaborate with another agent on a topic.

        Args:
            other_agent_role: Role of the other agent
            topic: Topic for collaboration

        Returns:
            Collaborative response
        """
        collaboration_prompts = {
            "Coder-Sociologist": "How can better software design improve social interactions in AI systems?",
            "Coder-Philosopher": "What are the ethical implications of autonomous code generation?",
            "Coder-AI_Researcher": "How can we build more efficient neural networks for code analysis?",
            "Sociologist-Philosopher": "How do social structures reflect philosophical principles?",
            "Sociologist-AI_Researcher": "How does AI technology impact social dynamics?",
            "Philosopher-AI_Researcher": "What does AI consciousness mean for human philosophy?"
        }

        collab_key = f"{self.role}-{other_agent_role}"
        reverse_key = f"{other_agent_role}-{self.role}"
        prompt = collaboration_prompts.get(collab_key, collaboration_prompts.get(reverse_key, topic))

        return self.respond_to_topic(prompt, f"Collaborating with {other_agent_role} on {topic}")
