FROM ubuntu:16.04

RUN mkdir -p /backend
COPY backend /backend
RUN mkdir -p /sql
COPY sql /sql

RUN apt-get update \
  && apt-get install -y python3-pip python3-dev \
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3 python \
  && pip3 install --upgrade pip

RUN apt-get install -y postgresql postgresql-contrib

RUN pip3 install pytesseract transliterate psycopg2 requests tornado opencv-python
RUN pip3 install git+https://github.com/deepmipt/ner.git
RUN apt-get update \
    && apt-get install -y vim
