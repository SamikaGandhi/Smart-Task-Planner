# backend_app/app/main.py
import json
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from .planner import generate_plan_from_goal
from .db import init_db, SessionLocal, Plan

app = FastAPI(title="Smart Task Planner", version="2.0")

# Static & Templates
app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")

init_db()  # Ensure DB exists


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/generate", response_class=HTMLResponse)
async def generate(request: Request,
                   title: str = Form("My Plan"),
                   goal: str = Form(...)):

    # Generate dynamic plan
    plan = generate_plan_from_goal(goal, title)

    # Save to DB
    db = SessionLocal()
    db_plan = Plan(title=title, goal=goal, data=json.dumps(plan))
    db.add(db_plan)
    db.commit()
    db.refresh(db_plan)

    plan["id"] = db_plan.id

    return templates.TemplateResponse("result.html", {
        "request": request,
        "plan": plan
    })


@app.get("/plans", response_class=HTMLResponse)
async def list_plans(request: Request):
    db = SessionLocal()
    rows = db.query(Plan).order_by(Plan.id.desc()).all()
    return templates.TemplateResponse("plans.html", {
        "request": request,
        "plans": rows
    })


# -------- JSON API endpoint --------

@app.post("/generate-plan")
def api_generate(req: dict):
    title = req.get("title", "My Plan")
    goal = req.get("goal")

    if not goal:
        return {"success": False, "error": "Goal is required"}

    try:
        plan = generate_plan_from_goal(goal, title)
    except Exception as e:
        return {"success": False, "error": str(e)}

    return {"success": True, "data": plan}
