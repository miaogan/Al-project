from fastapi import FastAPI
from app.api import tasks
from app.database.database import Base, engine

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="FastAPI with Celery", description="A FastAPI application integrated with Celery", version="0.1.0")

app.include_router(tasks.router, prefix="/api/v1")

@app.get("/")
async def root():
    return {"message": "Welcome to FastAPI with Celery"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}