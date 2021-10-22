from django.shortcuts import resolve_url as r
from model_bakery import baker


def test_unauthorized(api_client):
    data = {'summary': 'test', 'description': 'test description'}
    resp = api_client.post(r('api:task_list'))
    assert resp.status_code == 401


def test_post(api_client_logged_in):
    data = {'summary': 'test', 'description': 'test description'}
    resp = api_client_logged_in.post(r('api:task_list'), data)
    assert resp.status_code == 201


# def test_user_see_only_its_tasks(api_client, db):
#     user_a = baker.make('User')
#     user_b = baker.make('User')
#     t1 = baker.make('Task', user=user_a, summary='Task A')
#     t2 = baker.make('Task', user=user_b, summary='Task B')

#     api_client.force_authenticate(user_a)
#     resp = api_client.get(r('api:task_list'))
#     assert len(resp.data) == 1
#     assert 'Task A' in resp.json()[0]['summary']

#     api_client.force_authenticate(user_b)
#     resp = api_client.get(r('api:task_list'))
#     assert len(resp.data) == 1
#     assert 'Task B' in resp.json()[0]['summary']


# def test_superuser_can_see_all_tasks(api_client, db):
#     superuser = baker.make('User', is_superuser=True)
#     user_a = baker.make('User')
#     user_b = baker.make('User')
#     t1 = baker.make('Task', user=user_a, summary='Task A')
#     t2 = baker.make('Task', user=user_b, summary='Task B')

#     api_client.force_authenticate(superuser)
#     resp = api_client.get(r('api:task_list'))

#     assert len(resp.data) == 2
#     assert 'Task A' in resp.json()[0]['summary']
#     assert 'Task B' in resp.json()[1]['summary']


# def test_pending_before_completed(api_client_logged_in, db, user):
#     t1 = baker.make('Task', user=user, summary='Task A', status='completed')
#     t2 = baker.make('Task', user=user, summary='Task B', status='pending')

#     resp = api_client_logged_in.get(r('api:task_list'))

#     assert 'Task B' in resp.json()[0]['summary']
#     assert 'Task A' in resp.json()[1]['summary']
