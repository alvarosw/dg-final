.PHONY: dev

populate-db:
	@python manage.py migrate
	@python populate.py

dev:
	@python manage.py runserver