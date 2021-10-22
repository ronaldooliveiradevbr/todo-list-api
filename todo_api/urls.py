from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('todo_api.api.urls', namespace='api')),
    path('ht/', include('health_check.urls')),
]
