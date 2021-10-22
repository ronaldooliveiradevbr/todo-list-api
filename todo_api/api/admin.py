from django.contrib import admin

from todo_api.api.models import Task


@admin.register(Task)
class TaskModelAdmin(admin.ModelAdmin):
    fields = ('user', 'summary', 'description', 'status')
    readonly_fields = ('created_at', 'updated_at')
    list_display = ('summary', 'status', 'created_at')
