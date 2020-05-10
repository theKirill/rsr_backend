web: gunicorn rsr_backend-dev.wsgi:application --log-file - --log-level debug
python manage.py collectstatic --noinput
manage.py migrate