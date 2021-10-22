import pytest
from rest_framework.test import APIClient


@pytest.fixture
def api_client():
    yield APIClient()


@pytest.fixture
def user(db, django_user_model):
    return django_user_model.objects.create_user(username='test', password='test')


@pytest.fixture
def api_client_logged_in(api_client, user):
    api_client.force_authenticate(user)
    yield api_client
