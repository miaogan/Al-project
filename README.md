# FastAPI with Celery Project

# FastAPI + Celery 异步任务处理系统

本项目是一个集成了 Celery 分布式任务队列的 FastAPI 应用程序，用于处理异步任务。

## ✨ 功能特性

- 🚀 FastAPI 高性能 Web 框架
- 🎯 Celery 分布式任务队列
- 🔄 Redis 作为消息代理和结果后端
- 🗃️ SQLAlchemy ORM 数据库操作
- 📦 Docker 容器化部署
- 📊 完善的 API 文档

## 📂 项目结构

```
./
├── app/                  # 应用主目录
│   ├── api/              # API 路由
│   ├── core/             # 核心配置
│   ├── database/         # 数据库配置
│   ├── models/           # 数据库模型
│   ├── schemas/          # Pydantic 数据模型
│   ├── celery_worker.py  # Celery 配置
│   └── main.py          # FastAPI 入口
├── docker-compose.yml    # Docker 编排配置
├── Dockerfile            # 应用容器配置
├── celery_worker.Dockerfile # Celery 容器配置
├── requirements.txt      # Python 依赖
└── pyproject.toml       # 项目元数据
```

## 🛠️ 安装与运行

### 🐳 Docker 方式 (推荐)

1. 克隆项目仓库
2. 构建并启动服务:

```bash
docker-compose up --build
```

服务启动后访问:
- API 文档: http://localhost:8002/docs
- 健康检查: http://localhost:8002/health

### 💻 本地开发

1. 确保已安装:
   - Python 3.9+
   - Redis 服务器

2. 安装依赖:

```bash
pip install -r requirements.txt
```

3. 启动服务:

```bash
uvicorn app.main:app --reload --port 8002
```

4. 启动 Celery worker:

```bash
celery -A app.celery_worker worker --loglevel=info
```

## 📡 API 文档

### 任务相关接口

| 方法 | 端点 | 描述 |
|------|------|------|
| POST | `/api/v1/tasks/` | 创建新任务 |
| GET  | `/api/v1/tasks/{task_id}` | 获取任务状态 |

### 系统接口

| 方法 | 端点 | 描述 |
|------|------|------|
| GET  | `/` | 欢迎页面 |
| GET  | `/health` | 健康检查 |

## 📝 使用示例

### 创建任务

```bash
curl -X POST "http://localhost:8002/api/v1/tasks/" \
     -H "Content-Type: application/json" \
     -d '{"type": "compute", "data": {"numbers": [1, 2, 3, 4, 5]}}'
```

### 查询任务状态

```bash
curl -X GET "http://localhost:8002/api/v1/tasks/{task_id}"
```

## 📦 依赖项

主要技术栈:

- [FastAPI](https://fastapi.tiangolo.com/)
- [Celery](https://docs.celeryproject.org/)
- [Redis](https://redis.io/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [Pydantic](https://pydantic-docs.helpmanual.io/)

完整依赖请查看 `requirements.txt` 文件。