web: gunicorn firstDjango.wsgi:application --log-file - --log-level debug
web: python backend/manage.py collectstatic --noinput
web: python backend/manage.py migrate