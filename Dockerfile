FROM python:3.8-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

WORKDIR /code
COPY requirements.txt /code

RUN apk update \
    && apk add gcc python3-dev musl-dev \
    && apk add postgresql \
    && apk add postgresql-dev \
    && pip3 install psycopg2 \
    && apk add jpeg-dev zlib-dev libjpeg \
    && pip3 install Pillow

RUN pip3 install -r /code/requirements.txt --no-cache-dir

COPY . /code

CMD gunicorn foodgram.wsgi:application --bind 0.0.0.0:8000
