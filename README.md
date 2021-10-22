# TO-DO LIST API

![TO-DO LIST CI](https://github.com/rfdeoliveira/todo-list-api/workflows/To-Do%20List%20API%20CI/badge.svg)

This REST API allows registered users to list, create and filter their tasks and by status (pending or completed).

Authentication is implemented using JWT (Json Web Token).

Superusers can list all tasks (including other users' tasks) and create their own tasks.


## Usage

### Authentication:

```console
$ curl \
  -X POST \
  -H "Content-Type: application/json" \
  -d '{"username": "john", "password": "$uper$ecret"}' \
  http://localhost:8000/api/token/
```

Authentication sample response:

```json
{
    "access": "some-access-token",
    "refresh": "some-refresh-token"
}
```

### List tasks:

```console
$ curl \
  -X GET \
  -H "Authorization: Bearer some-access-token"
  http://localhost:8000/api/tasks/
```

List tasks sample response:

```json
{
    "count": 2,
    "next": null,
    "previous": null,
    "results": [
        {
            "summary": "test",
            "description": "test description",
            "status": "pending",
            "created_at": "2021-01-01T04:26:08",
            "updated_at": "2021-01-01T04:26:08"
        },
        {
            "summary": "teste",
            "description": "descricao",
            "status": "completed",
            "created_at": "2021-01-01T04:26:19",
            "updated_at": "2021-01-01T04:26:55"
        }
    ]
}
```

### Filter tasks:

```console
$ curl \
  -X GET \
  -H "Authorization: Bearer some-access-token"
  http://localhost:8000/api/tasks/?status=pending
```

Filter tasks sample response:

```json
{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "summary": "test",
            "description": "test description",
            "status": "pending",
            "created_at": "2021-01-01T04:26:08",
            "updated_at": "2021-01-01T04:26:08"
        }
    ]
}
```

### Create task:

```console
$ curl \
  -X POST \
  -d '{"summary": "Walk the dog", "description": "Take Spike to a walk for 15 minutes", "status": "pending"}
  -H "Authorization: Bearer some-access-token"
  http://localhost:8000/api/tasks/
```

Create task sample response:

```json
{
    "summary": "Walk the dog",
    "description": "Take Spike to a walk for 15 minuts",
    "status": "pending",
    "created_at": "2021-01-01T13:37:52",
    "updated_at": "2021-01-01T13:37:52"
}
```


## How to develop

1. Clone the repository.
1. Create a virtualenv with Python 3.9.
1. Activate virtualenv.
1. Install dependencies.
1. Configure enviroment variables.
1. Run test suite.

```console
git clone git@github.com:rfdeoliveira/todo-list-api.git
cd todo-list-api
python -m venv .todo-list-api
source .todo-list-api/bin/activate
pip install -r requirements-dev.txt
cp contrib/env-sample .env
make test
```


## How to deploy

1. Create an instance in Heroku
1. Configure environment variables in Heroku instance.
1. Set a secure SECRET_KEY
1. Set `DEBUG=False`
1. Run deploy command

```console
heroku app:create my-instance-name
heroku config:push
heroku config:set SECRET_KEY=`python manage.py generate_secret_key`
heroku config:set DEBUG=False
make deploy
```


## Workflows

There are two GitHub Actions configured in this project:
* _CI_: which runs the test suite and is triggered by opening a PR to branch `main`
* _CD_: which runs the test suite, deploys to Heroku instance and is triggered by `push` on branch `main`


## Useful command-line features

* `make drop-local-db`: drop sqlite3 database file. Useful for a fresh start
* `make install`: recreates sqlite3 database file, run all migrations and creates sample users
* `make run`: start server on [http://localhost:8000](http://localhost:8000)
* `make test`: run tests suite
* `make deploy`: push changes to branch `main` and trigger `cd` workflow, which deploys api to Heroku instance
