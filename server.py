# server.py
# One small FastAPI bridge so frontend/main.html can talk to your root agent.

import os, sys
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

# Ensure the repo root is on the import path (so `agent.py` + sub_agents import cleanly)
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

# ⬇️ Your root agent lives in agent.py at the repo root
from agent import root_agent

app = FastAPI(title="HOF-Hackathon2 API")

# Wide-open CORS for local/dev; tighten in prod
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatIn(BaseModel):
    message: str

class ChatOut(BaseModel):
    reply: str

@app.get("/health")
def health():
    return {"ok": True}

@app.post("/api/chat", response_model=ChatOut)
def chat(body: ChatIn):
    """Send the user's text to the root agent; it will call sub-agents as needed."""
    text = body.message

    # ADK variants: some use .run, others .invoke. Prefer .run; fall back to .invoke.
    try:
        result = root_agent.run({"user_input": text})
    except AttributeError:
        result = root_agent.invoke({"user_input": text})

    # Normalize result -> string for the UI
    if isinstance(result, dict):
        reply = (
            result.get("meal_planning_result")
            or result.get("output")
            or result.get("reply")
            or result.get("text")
            or str(result)
        )
    else:
        reply = str(result)

    reply = (reply or "").strip()
    return ChatOut(reply=reply if reply else "No reply.")
