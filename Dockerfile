FROM python:3.11-slim

# 设置工作目录
WORKDIR /app

# 将依赖文件复制到容器中
COPY requirements.txt requirements.txt


RUN echo "Installing dependencies..." && pip install -r requirements.txt


# 复制当前项目的所有代码到容器中
COPY . .

# 暴露 Flask 默认端口
EXPOSE 5000

# 设置环境变量
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV PYTHONUNBUFFERED=1

# 启动 Flask 应用
CMD ["flask", "run", "--port=5000"]
