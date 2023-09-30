from django.db.backends.ddl_references import Reference
from django.shortcuts import render

from apps.main.mainpage.models import MainPage
from apps.main.service.models import Services
from apps.main.reference.models import References


def index(request):
    main_page = MainPage.objects.filter().last()
    services = Services.objects.filter()
    refereces = References.objects.all()
    context = {
        'main_page': main_page,
        'services': services,
        'refereces': refereces,
    }

    return render(request, "index.html", context)
