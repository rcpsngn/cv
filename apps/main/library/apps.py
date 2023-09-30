from django.apps import AppConfig


class LibraryConfig(AppConfig):
    default_auto_filed = "django.db.models.BigAutoField"
    name = "apps.main.library"