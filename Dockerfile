# syntax=docker/dockerfile:1

FROM python:3.11-slim

LABEL maintainer="stanar278@gmail.com"

WORKDIR /app

COPY requirements.txt requirements.txt

RUN python3 -m pip install -r requirements.txt

COPY . .

RUN ./setenv.sh && python3 load_data_in_db.py

CMD [ "python3", "start.py" ]
