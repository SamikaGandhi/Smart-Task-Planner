# backend_app/app/schemas.py
from pydantic import BaseModel
from typing import Optional, List, Dict, Any

class PlanRequest(BaseModel):
    title: Optional[str] = "My Plan"
    goal: str
    due_date: Optional[str] = None

class TaskItem(BaseModel):
    id: str
    title: str
    description: Optional[str]
    duration_days: int
    depends_on: List[str] = []
    priority: Optional[str] = "medium"

class PlanResponse(BaseModel):
    title: str
    goal: str
    tasks: List[TaskItem]
    recommended_schedule: Dict[str, Any]
