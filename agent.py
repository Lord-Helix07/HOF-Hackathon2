'''
HOF-Hackathon2 Orchestrator Agent
'''

from google.adk.agents import LlmAgent
from typing import Dict, List, Optional, Any
import json
from . import prompt
from .sub_agents.meal_planning_agent import meal_planning_agent
from .sub_agents.mood_agent import mood_agent

GEMINI_MODEL = "gemini-2.0-flash"

root_agent = LlmAgent(
    name="CoordinatorAgent",
    model=GEMINI_MODEL,
    instruction=prompt.COORDINATOR_PROMPT,
    sub_agents=[meal_planning_agent, mood_agent],
)
