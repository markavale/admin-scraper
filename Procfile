release: python manage.py makemigrations
release: python manage.py migrate
web: gunicorn base.wsgi.prod --log-file -