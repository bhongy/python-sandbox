FROM python:2.7.15-alpine

# RUN apk add --no-cache

WORKDIR /usr/app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY pytest.ini .

ENTRYPOINT [ "/bin/sh" ]