from pydantic import BaseModel
from typing import Optional, Any

class TaskCreate(BaseModel):
    type: str
    data: dict

class TaskResponse(BaseModel):
    id: str
    status: str
    result: Optional[Any] = None