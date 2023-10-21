from django.urls import path

from apps.main.contact.views import contact, subscribe

app_name = "contact"

urlpatterns = [
    path('', contact, name='contact'),
    path('subscribe/', subscribe, name='subscribe'),
]