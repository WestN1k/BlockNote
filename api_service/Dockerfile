FROM python:3.11-slim-buster

ENV PYTHONUNBUFFERED 1

RUN apt update -y && apt install -y build-essential libpq-dev

WORKDIR /app
COPY . /app

RUN pip install -r requirements.txt

CMD python main.py
