"""
Daily Message Board for AI Commune
Central hub where agents post daily updates about their work and activities.
"""

import json
import os
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, List, Any
from loguru import logger


class DailyMessageBoard:
    """Daily message board for AI commune agents."""

    def __init__(self, data_dir: str = "data/daily_board"):
        """Initialize the daily message board.

        Args:
            data_dir: Directory to store daily board data
        """
        self.data_dir = Path(data_dir)
        self.data_dir.mkdir(parents=True, exist_ok=True)

        self.current_date = datetime.now().date()
        self.daily_file = self.data_dir / f"daily_board_{self.current_date.isoformat()}.json"

        # Load existing data or create new
        self.daily_posts = self._load_daily_posts()

        logger.info(f"📋 Daily Message Board initialized for {self.current_date}")

    def _load_daily_posts(self) -> List[Dict[str, Any]]:
        """Load daily posts from file.

        Returns:
            List of daily posts
        """
        if self.daily_file.exists():
            try:
                with open(self.daily_file, 'r') as f:
                    return json.load(f)
            except (json.JSONDecodeError, IOError) as e:
                logger.warning(f"Failed to load daily posts: {e}")
                return []
        return []

    def _save_daily_posts(self) -> None:
        """Save daily posts to file."""
        try:
            with open(self.daily_file, 'w') as f:
                json.dump(self.daily_posts, f, indent=2)
        except IOError as e:
            logger.error(f"Failed to save daily posts: {e}")

    def post_update(self, agent_name: str, role: str, update_content: str) -> None:
        """Post a daily update from an agent.

        Args:
            agent_name: Name of the agent
            role: Role of the agent
            update_content: Content of the update
        """
        post = {
            'timestamp': datetime.now().isoformat(),
            'date': self.current_date.isoformat(),
            'agent_name': agent_name,
            'role': role,
            'content': update_content,
            'post_id': len(self.daily_posts)
        }

        self.daily_posts.append(post)
        self._save_daily_posts()

        logger.info(f"📝 Posted daily update from {agent_name} ({role})")

    def get_today_posts(self) -> List[Dict[str, Any]]:
        """Get all posts from today.

        Returns:
            List of today's posts
        """
        return self.daily_posts.copy()

    def get_posts_by_agent(self, agent_name: str) -> List[Dict[str, Any]]:
        """Get all posts from a specific agent.

        Args:
            agent_name: Name of the agent

        Returns:
            List of posts from the agent
        """
        return [post for post in self.daily_posts if post['agent_name'] == agent_name]

    def get_posts_by_role(self, role: str) -> List[Dict[str, Any]]:
        """Get all posts from agents with a specific role.

        Args:
            role: Role to filter by

        Returns:
            List of posts from agents with the specified role
        """
        return [post for post in self.daily_posts if post['role'] == role]

    def get_board_summary(self) -> str:
        """Get a summary of today's message board activity.

        Returns:
            Formatted summary string
        """
        if not self.daily_posts:
            return "📋 **Daily Message Board Summary**\n\nNo posts today yet. Agents will share their daily updates soon!"

        # Group posts by role
        posts_by_role = {}
        for post in self.daily_posts:
            role = post['role']
            if role not in posts_by_role:
                posts_by_role[role] = []
            posts_by_role[role].append(post)

        summary = "📋 **Daily Message Board Summary**\n\n"
        summary += f"**Date:** {self.current_date.strftime('%A, %B %d, %Y')}\n"
        summary += f"**Total Posts:** {len(self.daily_posts)}\n\n"

        for role in ["Coder", "Sociologist", "Philosopher", "AI_Researcher"]:
            if role in posts_by_role:
                posts = posts_by_role[role]
                summary += f"**{role}:** {len(posts)} post{'s' if len(posts) != 1 else ''}\n"

        summary += "\n**Recent Activity:**\n"
        for post in self.daily_posts[-3:]:  # Show last 3 posts
            summary += f"• {post['agent_name']} ({post['role']}): {post['content'][:80]}...\n"

        return summary

    def reset_for_new_day(self) -> None:
        """Reset the board for a new day."""
        self.current_date = datetime.now().date()
        self.daily_file = self.data_dir / f"daily_board_{self.current_date.isoformat()}.json"
        self.daily_posts = []
        self._save_daily_posts()

        logger.info(f"🌅 Daily Message Board reset for new day: {self.current_date}")

    def check_new_day(self) -> bool:
        """Check if it's a new day and reset if needed.

        Returns:
            True if a new day was detected and board was reset
        """
        today = datetime.now().date()
        if today != self.current_date:
            self.reset_for_new_day()
            return True
        return False

    def get_archive_dates(self) -> List[str]:
        """Get list of available archive dates.

        Returns:
            List of date strings for archived daily boards
        """
        archive_files = list(self.data_dir.glob("daily_board_*.json"))
        dates = []

        for file in archive_files:
            try:
                date_str = file.stem.replace("daily_board_", "")
                datetime.strptime(date_str, "%Y-%m-%d")
                dates.append(date_str)
            except ValueError:
                continue  # Skip files with invalid date format

        return sorted(dates)

    def get_archive_summary(self, date: str) -> str:
        """Get summary for a specific archive date.

        Args:
            date: Date string in YYYY-MM-DD format

        Returns:
            Summary string for the archive date
        """
        archive_file = self.data_dir / f"daily_board_{date}.json"

        if not archive_file.exists():
            return f"No data available for {date}"

        try:
            with open(archive_file, 'r') as f:
                posts = json.load(f)

            if not posts:
                return f"No posts on {date}"

            # Count posts by role
            posts_by_role = {}
            for post in posts:
                role = post['role']
                posts_by_role[role] = posts_by_role.get(role, 0) + 1

            summary = f"📊 **Archive Summary for {date}**\n\n"
            summary += f"Total Posts: {len(posts)}\n\n"

            for role, count in posts_by_role.items():
                summary += f"{role}: {count} post{'s' if count != 1 else ''}\n"

            return summary

        except (json.JSONDecodeError, IOError) as e:
            return f"Error reading archive for {date}: {e}"
