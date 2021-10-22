drop-local-db:
	@rm db.sqlite3

install:
	@python manage.py migrate
	@python manage.py loaddata --app api initial_data.json

test:
	@pytest

run:
	@python manage.py runserver -v2

deploy:
	@git push origin main
