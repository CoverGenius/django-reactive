FROM python:3.10

ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code

RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install
