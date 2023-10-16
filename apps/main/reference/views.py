from django.db.backends.ddl_references import Reference
from django.shortcuts import render

from apps.main.mainpage.models import MainPage
from apps.main.service.models import Services
from apps.main.reference.models import *

def reference(request):
    context = {
    }

    return render(request, "apps/reference/reference.html", context)


