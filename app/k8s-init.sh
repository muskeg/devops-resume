#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."
    echo "Looking for $SQL_HOST on port $SQL_PORT"
    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

python /home/app/web/manage.py migrate --noinput
python /home/app/web/manage.py collectstatic --no-input
/usr/local/bin/gunicorn raph.wsgi:application --bind 0.0.0.0:8000


