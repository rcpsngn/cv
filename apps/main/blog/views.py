from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from apps.main.blog.models import Blog, BlogCategory, BlogComment


def blog(request):
    context = {}
    return render(request, "apps/blog/blog.html", context)





def blog_detail(request, slug):
    blog_content = Blog.objects.get(slug=slug)
    last_blog = Blog.objects.filter(id__lt=blog_content.id).order_by('-id').first()    # Mevcut blog gönderisinin ID'sine göre sonraki gönderiyi al
    next_blog = Blog.objects.filter(id__gt=blog_content.id).order_by('id').first()    # Mevcut blog gönderisinin ID'sine
    category_list = BlogCategory.objects.filter()
    comment_list = BlogComment.objects.filter(blog=blog_content).order_by("-date")

    if request.POST:
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        if name and email and message:
            control = BlogComment.objects.create(comment=message, name=name, email=email, blog=blog_content)
            if control:
                messages.success(request, ("Kayıt Başarılı"))
                return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
            else:
                messages.warning(request, ("Teknik Bir Hata Oluştu"))
                return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
        else:
            messages.warning(request, ("Tüm Alanları Doldurun"))
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


    context = {
        'blog_content': blog_content,
        'category_list': category_list,
        'next_blog': next_blog,
        'last_blog': last_blog,
        'comment_list': comment_list,

    }
    return render(request, "apps/blog/blog-detail.html", context)
