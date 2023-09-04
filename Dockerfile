FROM python:3.10

WORKDIR /app

COPY requirements.txt ./requirements.txt

RUN pip install --upgrade pip -r requirements.txt

COPY app/ .

ARG VERSION
ENV DOCKER_TAG=$VERSION

EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

ENTRYPOINT ["streamlit", "run", "Welcome.py", "--server.port=8501", "--server.address=0.0.0.0"]

