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
RUN apt-get install -y libglib2.0-0

RUN apt update && apt install -y libsm6 libxext6
RUN apt-get install -y python-dev python-numpy libtbb2 libtbb-dev libjpeg-dev libpng-dev libtiff-dev libjasper-dev libdc1394-22-dev
RUN apt-get install -y cmake git libgtk2.0-dev pkg-config libavcodec-dev libavformat-dev libswscale-dev
RUN pip3 install pytesseract transliterate psycopg2 requests tornado opencv-python
RUN pip3 install git+https://github.com/deepmipt/ner.git -q
RUN apt-get update \
    && apt-get install -y vim

COPY index.html /

#POSTGRES
RUN mkdir -p /usr/local/pgsql/data/
RUN chown -R postgres /usr/local/pgsql/data/
RUN su postgres -c "/usr/lib/postgresql/9.5/bin/initdb -D /usr/local/pgsql/data"
COPY docker/entry.sh /
#RUN su postgres -c "/usr/lib/postgresql/9.5/bin/pg_ctl  -D /usr/local/pgsql/data  start"
#
#RUN su postgres -c "createdb call_of_data"
#RUN psql 'host=localhost port=5432 dbname=call_of_data user=postgres' -f /sql/init.sql
