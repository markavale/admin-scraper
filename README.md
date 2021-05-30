# djangovue-backend-boilerplate

## Project Details
This Template includes dj-rest-auth for authentication and Token authentication.


## Project setup for virtualenv users
```
python3 -m venv env
pip install -r requirements.txt
python manage.py migrate
```

## Project setup for pipenv users
```
pipenv shell
pipenv install
python manage.py migrate

```

## Create .env file for your env variables(Copy paste the details below and replace it with your own env variables)
```

[settings]
SECRET_KEY = 'your awesome secret key'
DJANGO_SETTINGS_MODULE = 'base.settings.dev'

[sql-database-config]
NAME=your_db_name
USER=your_db_user
PASSWORD=your_db_password
PORT=your_db_port
HOST=your_db_host

[email]
EMAIL_HOST_PASSWORD = 'your_email_pass'
EMAIL_HOST_USER = 'your_email'
```
See [Configuration Reference of python decouple](https://pypi.org/project/python-decouple/).

## Frontend Project setup
```
npm install --save
```
## Compiles and hot-reloads for development
```
npm run serve
```
## Compiles and minifies for production
```
npm run build
```
## Lints and fixes files
```
npm run lint
```
### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).


