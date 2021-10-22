import pytest

from todo_api.api.models import Task


@pytest.fixture
def task(db, user):
    return Task.objects.create(
        user=user,
        summary='some text',
        description='more text',
        status=Task.Status.PENDING,
        created_at='2021-01-01 00:00:00',
    )


def test_create(task):
    assert Task.objects.exists()
