from django.shortcuts import render

from apps.main.blog.models import Blog


def blog(request):
    context = {}
    return render(request, "apps/blog/blog.html", context)

def blog_detail(request, slug):
    blog_content = Blog.objects.get(slug=slug)
    context = {
        'blog_content': blog_content
    }
    return render(request, "apps/blog/blog-detail.html", context)
