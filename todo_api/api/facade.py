from todo_api.api.models import Task


def _allowed_to_user(user):
    if user.is_superuser:
        qs = Task.objects.all()
    else:
        qs = Task.objects.filter(user=user)

    return qs


def tasks(user):
    return _allowed_to_user(user)
