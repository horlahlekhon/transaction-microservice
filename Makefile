migrate:
	python manage.py makemigrations
	python manage.py migrate

run:
	python manage.py runserver

db_reset:
	find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
	find . -path "*/migrations/*.pyc"  -delete
	python manage.py makemigrations
	python manage.py migrate