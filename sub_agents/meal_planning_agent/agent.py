"""
Meal Planning Agent
"""

from google.adk import Agent
from . import prompt

MODEL = "gemini-2.5-flash"

meal_planning_agent = Agent(
    model=MODEL,
    name="meal_planning_agent",
    instruction=prompt.MEAL_PLANNING_PROMPT,
    output_key="meal_planning_result",
)

root_agent = meal_planning_agent
