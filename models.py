from pydantic import BaseModel
from typing import Literal
import datetime


class TodoItem(BaseModel):
    task: str
    priority: Literal["low", "medium", "high"]
    tag: str # TODO: Should be from a list of tags the user can create. The model can suggest them too


# ICS format
class CalendarEvent(BaseModel):
    summary: str
    dtstart: str
    dtend: str
    description: str


class AssistantResponse(BaseModel):
    summary: str
    todos: list[TodoItem]
    calendar_events: list[CalendarEvent]
    reminders: list[str] # Should probably be a model -- need times on when to remind



