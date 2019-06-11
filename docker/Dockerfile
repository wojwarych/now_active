FROM python:3.7-alpine
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
ARG REQUIREMENTS

RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev
RUN python -m pip install --upgrade pip

RUN mkdir /backend
WORKDIR /backend

COPY ./requirements/ /backend/requirements/
RUN pip install -r $REQUIREMENTS

COPY ./backend /backend/
