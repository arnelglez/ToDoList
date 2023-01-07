from django.urls import path
from .views import *

urlpatterns = [
    path('todo/', ToDoList.as_view(), name='todo_list'),
    path('todo/<int:id>/', ToDoOperations.as_view(), name='todo_operations' ),
]