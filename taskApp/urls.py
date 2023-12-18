from django.urls import path
from .views import *

urlpatterns = [

    path('',taskList,name='tasks' ),

]
