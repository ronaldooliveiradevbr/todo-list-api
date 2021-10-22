from django.shortcuts import resolve_url as r
from model_bakery import baker


def test_unauthorized(api_client):
    resp = api_client.get(r('api:task_list'))
    assert resp.status_code == 401


def test_get(api_client_logged_in):
    resp = api_client_logged_in.get(r('api:task_list'))
    assert resp.status_code == 200


def test_user_sees_only_its_tasks(api_client, db):
    user_a = baker.make('User')
    user_b = baker.make('User')
    t1 = baker.make('Task', user=user_a, summary='Task A')
    t2 = baker.make('Task', user=user_b, summary='Task B')

    api_client.force_authenticate(user_a)
    resp = api_client.get(r('api:task_list'))
    print(resp.json())
    assert resp.json()['count'] == 1
    assert 'Task A' in resp.json()['results'][0]['summary']

    api_client.force_authenticate(user_b)
    resp = api_client.get(r('api:task_list'))
    assert resp.json()['count'] == 1
    assert 'Task B' in resp.json()['results'][0]['summary']


def test_superuser_can_see_all_tasks(api_client, db):
    superuser = baker.make('User', is_superuser=True)
    user_a = baker.make('User')
    user_b = baker.make('User')
    t1 = baker.make('Task', user=user_a, summary='Task A')
    t2 = baker.make('Task', user=user_b, summary='Task B')

    api_client.force_authenticate(superuser)
    resp = api_client.get(r('api:task_list'))

    assert resp.json()['count'] == 2
    assert 'Task A' in resp.json()['results'][0]['summary']
    assert 'Task B' in resp.json()['results'][1]['summary']


def test_pending_before_completed(api_client_logged_in, db, user):
    t1 = baker.make('Task', user=user, summary='Task A', status='completed')
    t2 = baker.make('Task', user=user, summary='Task B', status='pending')

    resp = api_client_logged_in.get(r('api:task_list'))

    assert 'Task B' in resp.json()['results'][0]['summary']
    assert 'Task A' in resp.json()['results'][1]['summary']


def test_filter_status(api_client_logged_in, db, user):
    t1 = baker.make('Task', user=user, summary='Task A', status='completed')
    t2 = baker.make('Task', user=user, summary='Task B', status='pending')

    resp = api_client_logged_in.get(f"{r('api:task_list')}?status=pending")
    assert resp.json()['count'] == 1
    assert 'Task B' in resp.json()['results'][0]['summary']

    resp = api_client_logged_in.get(f"{r('api:task_list')}?status=completed")
    assert resp.json()['count'] == 1
    assert 'Task A' in resp.json()['results'][0]['summary']
