# FastAPI with Celery Project

This project demonstrates a FastAPI application integrated with Celery for asynchronous task processing.

## Project Structure

```
app/
├── main.py              # FastAPI application entry point
├── api/
│   └── tasks.py         # Task-related API endpoints
├── core/
│   └── config.py        # Application configuration
├── models/
│   └── task.py          # Database models
├── schemas/
│   └── task.py          # Pydantic schemas for data validation
├── database/
│   └── database.py      # Database configuration
└── celery_worker.py     # Celery worker configuration
```

## Features

- FastAPI application with RESTful API
- Celery for asynchronous task processing
- Redis as message broker and result backend
- SQLAlchemy for database operations
- Docker and Docker Compose for containerization

## Prerequisites

### For Docker Deployment
- Docker
- Docker Compose

### For Local Development
- Python 3.9 or higher
- Redis server

## Getting Started

### Running with Docker

1. Clone the repository
2. Run the application using Docker Compose:

```bash
docker-compose up --build
```

The application will be available at `http://localhost:8002`.

**Note:** If you encounter network issues when building Docker images, try using a Docker registry mirror or VPN.

### Running Locally

1. Clone the repository
2. Install the dependencies:

```bash
pip install -r requirements.txt
```

3. Start a Redis server (required for Celery)
4. Run the FastAPI application:

```bash
# On Unix/Linux/macOS
./start.sh

# On Windows
start.bat
```

5. In a separate terminal, start the Celery worker:

```bash
# On Unix/Linux/macOS
./start-worker.sh

# On Windows
start-worker.bat
```

## API Endpoints

- `GET /` - Welcome message
- `GET /health` - Health check
- `POST /api/v1/tasks/` - Create a new task
- `GET /api/v1/tasks/{task_id}` - Get task status

## Example Usage

Create a new task:

```bash
curl -X POST "http://localhost:8000/api/v1/tasks/" -H "Content-Type: application/json" -d '{"type": "compute", "data": {"numbers": [1, 2, 3, 4, 5]}}'
```

Check task status:

```bash
curl -X GET "http://localhost:8000/api/v1/tasks/{task_id}"
```

## Project Dependencies

- FastAPI
- Celery
- Redis
- SQLAlchemy
- Pydantic