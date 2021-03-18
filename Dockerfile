FROM python:3.8.5

WORKDIR /code
COPY requirements.txt /code

RUN pip install -r /code/requirements.txt --no-cache-dir

RUN echo its new docker

COPY . /code

CMD gunicorn foodgram.wsgi:application --bind 0.0.0.0:8000
