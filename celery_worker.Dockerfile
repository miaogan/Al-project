FROM python:latest

WORKDIR /app

# 使用国内镜像源加速依赖安装
RUN pip install --upgrade pip -i https://pypi.tuna.tsinghua.edu.cn/simple
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

COPY . .

CMD ["celery", "-A", "app.celery_worker.celery_app", "worker", "--loglevel=info", "--pool=solo"]