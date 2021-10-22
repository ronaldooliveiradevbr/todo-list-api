release: python manage.py migrate && python manage.py loaddata --app api initial_data.json
web: gunicorn todo_api.wsgi --log-file -