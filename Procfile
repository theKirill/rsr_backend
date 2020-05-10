web: gunicorn rsr_backend.wsgi:application --preload --log-file - --log-level debug
python manage.py collectstatic --noinput
manage.py migrate