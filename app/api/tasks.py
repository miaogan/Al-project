from fastapi import APIRouter, HTTPException
from app.schemas.task import TaskCreate, TaskResponse
from app.celery_worker import create_task

router = APIRouter()

@router.post("/tasks/", response_model=TaskResponse)
async def create_new_task(task: TaskCreate):
    try:
        result = create_task.delay(task.type, task.data)
        return TaskResponse(id=str(result.id), status="pending")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/tasks/{task_id}", response_model=TaskResponse)
async def get_task_status(task_id: str):
    try:
        result = create_task.AsyncResult(task_id)
        return TaskResponse(id=task_id, status=result.status, result=result.result if result.ready() else None)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))