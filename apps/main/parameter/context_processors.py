from apps.main.parameter.models import Menu, Settings


def menu(request):
    header_menu = Menu.objects.filter().order_by("alignment")
    return {'header_menu': header_menu}

def site(request):
    site_settings = Settings.objects.filter().last()
    return {'site_settings': site_settings}