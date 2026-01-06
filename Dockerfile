FROM python:3.13-slim-trixie

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app

COPY pyproject.toml ./pyproject.toml
COPY uv.lock ./uv.lock

RUN uv sync

COPY app/ .

ARG VERSION
ENV DOCKER_TAG=$VERSION

EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

ENTRYPOINT ["uv", "run", "streamlit", "run", "Welcome.py", "--server.port=8501", "--server.address=0.0.0.0"]
