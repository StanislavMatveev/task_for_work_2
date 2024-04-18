FROM python:3.11-slim

LABEL maintainer="stanar278@gmail.com"

ENV BOT_TOKEN=<bot_token_value> \
    DB_HOST=mongodb \
    DB_PORT=27017

WORKDIR /app

COPY requirements.txt requirements.txt

RUN python3 -m pip install -r requirements.txt

COPY . .

CMD python3 migration.py &&\
    python3 start.py
