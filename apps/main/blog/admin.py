from django.contrib import admin

from apps.main.blog.models import *

admin.site.register(BlogCategory)
admin.site.register(Blog)
admin.site.register(BlogTag)
admin.site.register(BlogComment)
