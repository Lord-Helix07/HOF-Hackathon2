"""
Mood Agent
"""

from google.adk import Agent
from . import prompt

MODEL = "gemini-2.5-flash"

mood_agent = Agent(
    model=MODEL,
    name="mood_agent",
    instruction=prompt.MOOD_PROMPT,
    output_key="mood_result",
)


