web: gunicorn note_app.wsgi:application --log-file - --log-level debug
heroku ps:scale web=1
python backend/manage.py migrate