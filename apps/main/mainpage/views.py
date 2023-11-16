from django.db.backends.ddl_references import Reference
from django.db.models import Q
from django.shortcuts import render

from apps.main.about.models import Career, Skills
from apps.main.blog.models import Blog
from apps.main.mainpage.models import MainPage
from apps.main.service.models import Services
from apps.main.reference.models import References


def index(request):
    main_page = MainPage.objects.filter().last()
    services = Services.objects.filter()
    refereces = References.objects.all()
    career_list = Career.objects.all()
    skill_list = Skills.objects.filter(~Q(count=0))
    blog_list = Blog.objects.all()
    context = {
        'main_page': main_page,
        'services': services,
        'refereces': refereces,
        'career_list': career_list,
        'skill_list': skill_list,
        'blog_list' : blog_list,
    }

    return render(request, "index.html", context)
