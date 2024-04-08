.PHONY: dev

dev:
	@python manage.py migrate
	@python manage.py runserver