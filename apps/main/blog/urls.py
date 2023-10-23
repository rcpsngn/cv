from django.urls import path

from apps.main.blog.views import blog, blog_detail
from apps.main.mainpage.views import *

app_name = "mainpage"

urlpatterns = [
    path('', blog, name='blog'),
    path('<slug:slug>/', blog_detail, name='blog-detail'),
]