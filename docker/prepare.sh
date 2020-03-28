#!/usr/bin/bash
function migrate() {
    RETRIES=5
    until psql -h $POSTGRES_HOST -U $POSTGRES_USER -d $POSTGRES_DATABASE -c "select 1" > /dev/null 2>&1 || [ $RETRIES -eq 0 ]; do
      echo "Waiting for postgres server, $((RETRIES--)) remaining attempts..."
      sleep 1
    done
    python manage.py flush_db
    python manage.py migrate --noinput;
    python manage.py seed_db
}

migrate
