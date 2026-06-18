
FROM python:3.12-alpine

LABEL channel="LearnGorke"
LABEL creator="GorkeMorke"

WORKDIR /usr/lessons

COPY requirements.txt .

RUN apk update && apk upgrade && apk add --no-cache bash

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["pytest", "-s", "-v", "tests"]




#FROM ubuntu:latest
#LABEL authors="emilgabdrahmanov"
#
#ENTRYPOINT ["top", "-b"]