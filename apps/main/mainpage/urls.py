from django.urls import path

from apps.main.mainpage.views import *

app_name = "mainpage"

urlpatterns = [
    path('', index, name='index')
]