from celery import Celery
import os

celery_app = Celery(
    "worker",
    broker=os.environ.get("CELERY_BROKER_URL", "redis://localhost:6379/0"),
    backend=os.environ.get("CELERY_RESULT_BACKEND", "redis://localhost:6379/0")
)

celery_app.conf.update(
    task_serializer="json",
    accept_content=["json"],
    result_serializer="json",
    timezone="UTC",
    enable_utc=True,
    worker_pool="solo"  # For Windows compatibility
)

@celery_app.task
def create_task(task_type: str, task_data: dict):
    if task_type == "compute":
        # Simulate a computation task
        result = sum(task_data.get("numbers", []))
        return {"task_type": task_type, "result": result}
    elif task_type == "io":
        # Simulate an I/O task
        return {"task_type": task_type, "message": "I/O task completed"}
    else:
        return {"task_type": task_type, "message": "Unknown task type"}