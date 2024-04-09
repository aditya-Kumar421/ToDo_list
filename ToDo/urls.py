from django.urls import path
from .views import *

urlpatterns = [
    path('task/', TaskListView.as_view()),
    path('change/<int:pk>/', TaskDetailView.as_view()),
    path('get/<int:pk>/', TaskGetView.as_view()),
]