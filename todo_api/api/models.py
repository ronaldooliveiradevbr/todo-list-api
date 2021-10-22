from django.contrib.auth.models import User
from django.db import models


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Task(TimeStampedModel):
    class Status(models.TextChoices):
        COMPLETED = 'completed', 'Completed'
        PENDING = 'pending', 'Pending'

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    summary = models.CharField('summary', max_length=100)
    description = models.TextField('description', max_length=200)
    status = models.CharField('status', max_length=10, choices=Status.choices, default=Status.PENDING)

    class Meta:
        ordering = ('-status',)
