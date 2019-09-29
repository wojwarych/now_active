FROM python:3.7-slim-stretch
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
ARG REQUIREMENTS
RUN apt update && apt install
RUN mkdir /backend
WORKDIR /backend
COPY ./requirements/ /tmp/requirements/
RUN pip3 install -r $REQUIREMENTS
COPY ./backend /backend/
