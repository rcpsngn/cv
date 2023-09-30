from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from apps.main.mainpage.views import index
from projem01 import settings
from django.conf.urls.i18n import i18n_patterns

urlpatterns = i18n_patterns(
    path('', index, name="index"),
    path('super/user/admin', admin.site.urls),
    path('rosetta/lang/trans/', include('rosetta.urls')),
    path('i18n/', include('django.conf.urls.i18n'))
)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)