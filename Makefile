migrate:
	python manage.py makemigrations
	python manage.py migrate

run:
	gunicorn tx_microservice.wsgi

db_reset:
	find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
	find . -path "*/migrations/*.pyc"  -delete
	python manage.py makemigrations
	python manage.py migrate

install:
	pip install -r requirements.txt

seed:
	python manage.py seed_clients

test:
	python manage.py test

all: install migrate seed test run