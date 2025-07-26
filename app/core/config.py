import os
from typing import Optional
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "FastAPI with Celery"
    PROJECT_VERSION: str = "0.1.0"
    PROJECT_DESCRIPTION: str = "A FastAPI application integrated with Celery"
    
    # Database settings
    DATABASE_URL: Optional[str] = os.environ.get("DATABASE_URL", "sqlite:///./test.db")
    
    # Celery settings
    CELERY_BROKER_URL: str = os.environ.get("CELERY_BROKER_URL", "redis://localhost:6379/0")
    CELERY_RESULT_BACKEND: str = os.environ.get("CELERY_RESULT_BACKEND", "redis://localhost:6379/0")
    
    class Config:
        case_sensitive = True

settings = Settings()