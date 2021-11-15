from django.urls import path
from .views import *

app_name = "Tasks"

urlpatterns = [
    path('', get_task, name="get_task" ),
]