'''
HOF-Hackathon2 Orchestrator Agent
'''

from google.adk.agents import LlmAgent
from typing import Dict, List, Optional, Any
import json

GEMINI_MODEL = "gemini-2.0-flash"

root_agent = LlmAgent(
    name="MeLoCoordinator",
    model=GEMINI_MODEL,
    instruction=COORDINATOR_PROMPT,
    sub_agents=[],
)
    