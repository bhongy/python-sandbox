FROM python:2.7.15-alpine

COPY ./requirements.txt .
RUN pip install -r requirements.txt
WORKDIR /app