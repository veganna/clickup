from django.urls import path
from .views import *

app_name = "Accounts"

urlpatterns = [
    path('getUser/', get_user, name="get_user" )
]