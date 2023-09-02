FROM python:3.10

WORKDIR /app

# RUN apt-get update && apt-get install -y \
#     build-essential \
#     curl \
#     software-properties-common \
#     && rm -rf /var/lib/apt/lists/*

# ENV VIRTUAL_ENV=./venv
# RUN python3 -m venv $VIRTUAL_ENV
# RUN . $VIRTUAL_ENV/bin/activate

COPY requirements.txt ./requirements.txt

RUN pip install --upgrade pip -r requirements.txt

COPY app/ .

ARG VERSION
ENV DOCKER_TAG=$VERSION

EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

ENTRYPOINT ["streamlit", "run", "Welcome.py", "--server.port=8501", "--server.address=0.0.0.0"]
