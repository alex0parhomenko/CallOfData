#!/bin/bash

su postgres -c "/usr/lib/postgresql/9.5/bin/pg_ctl  -D /usr/local/pgsql/data  start"
su postgres -c "createdb call_of_data"
su postgres -c "psql 'host=localhost port=5432 dbname=call_of_data user=postgres' -f /sql/init.sql"

python3.5 main.py --port 8080 --dbname=call_of_data --pg_user=postgres &
