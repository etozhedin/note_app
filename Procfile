web: gunicorn note_app.wsgi:application --log-file - --log-level debug
python backend/manage.py collectstatic --noinput
python backend/manage.py migrate