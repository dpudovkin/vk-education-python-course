
FROM python:3.10-alpine

ENV HOME=/home/app
ENV APP_HOME=/home/app/web
RUN mkdir $HOME
RUN mkdir $APP_HOME
RUN mkdir $APP_HOME/staticfiles
RUN mkdir $APP_HOME/mediafiles
WORKDIR $APP_HOME


ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev
# install for crypto
RUN apk add --no-cache openssl-dev libffi-dev gcc && pip3 install --upgrade pip

RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install -r requirements.txt
# copy
COPY . .