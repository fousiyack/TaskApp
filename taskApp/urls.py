from django.urls import path
from .views import *

urlpatterns = [

    path('',taskList.as_view({'get': 'list'}),name='tasks' ),
    path('add/',AddTask.as_view(),name='add' ),
    path('edit/<int:task_id>/', edit_task, name='edit'),
    path('delete/<int:task_id>/', delete_task, name='delete'),

]
