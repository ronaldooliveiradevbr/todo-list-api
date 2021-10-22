import pytest
from django.shortcuts import resolve_url as r


@pytest.fixture
def resp(api_client, db, user):
    credentials = {'username': 'test', 'password': 'test'}
    return api_client.post(r('api:token_obtain_pair'), credentials)


def test_post(resp):
    assert resp.status_code == 200


def test_response_has_access_token(resp):
    assert 'access' in resp.json()


def test_response_has_refresh_token(resp):
    assert 'refresh' in resp.json()
