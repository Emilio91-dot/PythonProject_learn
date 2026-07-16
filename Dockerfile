#FROM python:3.12-alpine
#
#ARG run_env=dev
#ENV ENV=${run_env}
#
#LABEL channel="LearnGorke"
#LABEL creator="GorkeMorke"
#
#WORKDIR /usr/lessons
#
#COPY requirements.txt .
#
#RUN apk update && apk upgrade && apk add --no-cache bash
#
#RUN pip install --no-cache-dir -r requirements.txt
#
#COPY . .
#
#CMD ["sh", "-c", "pytest -m $ENV -s -v tests"]


FROM python:3.12-slim

ARG run_env=dev
ENV ENV=${run_env}

LABEL channel="LearnGorke"
LABEL creator="GorkeMorke"

WORKDIR /usr/lessons

VOLUME /allureResults

RUN python -m pip install --upgrade pip

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

#CMD ["pytest", "-s", "-v", "tests", "--alluredir=allure-results"]

#FROM ubuntu:latest
#LABEL authors="emilgabdrahmanov"
#
#ENTRYPOINT ["top", "-b"]


