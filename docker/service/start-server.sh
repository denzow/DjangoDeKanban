#!/bin/bash

pip install -r requirements.txt
python manage.py migrate

if [ "${DJANGO_ENV}" = 'production' ]; then
    daphne --root-path /app -b 0.0.0.0 -p 3000 application.asgi:application
else
    python manage.py runserver 0.0.0.0:3000 --nostatic

fi

