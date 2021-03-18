FROM python:3.8.5

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

WORKDIR /code
COPY requirements.txt /code

RUN pip install -r /code/requirements.txt --no-cache-dir

COPY . /code

CMD gunicorn foodgram.wsgi:application --bind 0.0.0.0:8000
