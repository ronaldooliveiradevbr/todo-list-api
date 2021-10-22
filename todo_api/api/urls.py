from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from todo_api.api import views

app_name = 'api'

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('tasks/', views.TaskListCreateView.as_view(), name='task_list')
]
