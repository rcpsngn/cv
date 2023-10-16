from django.urls import path
from apps.main.reference.views import *

app_name = "reference"

urlpatterns = [
    path('', reference, name='reference')
]