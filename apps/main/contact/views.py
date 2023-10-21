from apps.main.contact.models import Contact, Subscribe
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.utils.translation import gettext_lazy as _


def contact(request):
    if request.POST:
        name = request.POST.get('name')
        tel = request.POST.get('tel')
        email = request.POST.get('email')
        message = request.POST.get('message')

        control = Contact.objects.create(
            name=name,
            tel=tel,
            email=email,
            message=message,
        )
        if control:
            messages.success(request, _("İşlem Başarılı"))
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
        else:
            messages.success(request, _("Teknik Bir Hata Oluştu"))
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

    messages.warning(request, _("Gönderilen İstek Geçersiz"))
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

def subscribe(request):
    if request.POST:
        email = request.POST.get('email')

        control = Subscribe.objects.create(
            email=email,
        )
        if control:
            messages.success(request, _("İşlem Başarılı"))
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
        else:
            messages.success(request, _("Teknik Bir Hata Oluştu"))
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

    messages.warning(request, _("Gönderilen İstek Geçersiz"))
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))