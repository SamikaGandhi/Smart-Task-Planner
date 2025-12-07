import os
import requests
import re
from dotenv import load_dotenv

load_dotenv()

TOGETHER_API_KEY = os.getenv("TOGETHER_API_KEY")
LLM_MODEL = os.getenv("LLM_MODEL", "meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo")
TOGETHER_URL = "https://api.together.xyz/v1/chat/completions"

if not TOGETHER_API_KEY:
    raise ValueError("TOGETHER_API_KEY missing from .env")


# ---------------- LLM CALL -----------------

def call_llm(prompt: str) -> str:
    headers = {
        "Authorization": f"Bearer {TOGETHER_API_KEY}",
        "Content-Type": "application/json",
    }

    payload = {
        "model": LLM_MODEL,
        "messages": [
            {"role": "system", "content": "You are a helpful task-planning AI."},
            {"role": "user", "content": prompt}
        ],
        "max_tokens": 500,
        "temperature": 0.4,
    }

    res = requests.post(TOGETHER_URL, json=payload, headers=headers)

    if res.status_code != 200:
        raise RuntimeError(f"LLM Error: {res.status_code} - {res.text}")

    data = res.json()
    return data["choices"][0]["message"]["content"]


# ---------------- TASK GENERATOR -----------------

def generate_plan_from_goal(goal: str, title: str):
    """
    Generate 8 clean tasks:
    - No numbering
    - No bullets
    - No hyphens
    - No introductions
    - Only plain tasks
    """
    prompt = f"""
    You are a task creation bot.

    Break the goal below into EXACTLY 8 clear actionable tasks.

    GOAL: "{goal}"

    RULES:
    - Do NOT include introductions, summaries or notes.
    - Do NOT number tasks (no 1. or 1)).
    - Do NOT use bullets (- or •).
    - Do NOT use bold or formatting.
    - ONLY return a Python list of 8 plain task strings.

    Example (format only):
    ["Clean the kitchen", "Wash clothes", "Organize items", ...]
    """

    raw_output = call_llm(prompt).strip()

    # Convert safely into list
    try:
        tasks = eval(raw_output)
    except:
        # Fallback if model outputs weird format
        tasks = raw_output.split("\n")

    clean = []
    for t in tasks:
        t = t.strip()
        t = re.sub(r"^[\-\•]\s*", "", t)     # remove hyphens/bullets
        t = re.sub(r"^\d+[\.\)]\s*", "", t)  # remove numbering
        if t:
            clean.append(t)

    # ensure max 8 tasks
    clean = clean[:8]

    # failure fallback
    if len(clean) < 1:
        clean = ["Unable to generate tasks. Please try again."]

    return {
        "title": title,
        "goal": goal,
        "tasks": clean
    }
