from django.urls import path

from apps.main.mainpage.views import *

urlpatterns = [
    path('', index, name='index')
]