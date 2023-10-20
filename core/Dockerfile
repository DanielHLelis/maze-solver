FROM python:3.11-slim

ENV PYTHONUNBUFFERED 1
ENV FLASK_ENV production
ENV PYTHONDONTWRITEBYTECODE 1
ENV PIPENV_IGNORE_VIRTUALENVS 1

RUN mkdir -p /app/core
WORKDIR /app

RUN pip install --upgrade pip \
    && pip install pipenv

COPY Pipfile Pipfile.lock /app/

RUN pipenv install --deploy --ignore-pipfile

COPY . /app/core

CMD ["pipenv", "run", "gunicorn", "-b", "0.0.0.0:8000", "core.server.app:app"]
