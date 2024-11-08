# 包含poetry的python基础镜像
FROM sunpeek/poetry:py3.10-slim
LABEL maintainer="robocanic@gmail.com"
# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1
# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# mv source code to a specific directory
WORKDIR /appruntime
COPY . /appruntime

# no need to create virtual env
RUN poetry config virtualenvs.create false
# analyze deps
RUN poetry lock
# Install deps
RUN poetry install

# Creates a non-root user with an explicit UID and adds permission to access the /appruntime folder
RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /appruntime
USER appuser

CMD ["uvicorn", "poetry_fastapi_demo.main:app", "--host=0.0.0.0", "--port=8080", "--log-config=/appruntime/log.yaml"]