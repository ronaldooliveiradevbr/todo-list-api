from django_filters import rest_framework as filters

from todo_api.api.models import Task


class TaskFilter(filters.FilterSet):
    status = filters.MultipleChoiceFilter(
        label='Status',
        choices=Task.Status.choices,
        help_text='Lower cased task status. Options: "pending" and "completed"',
    )
