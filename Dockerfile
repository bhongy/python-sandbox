FROM python:2.7.15-alpine

COPY ./requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
WORKDIR /app