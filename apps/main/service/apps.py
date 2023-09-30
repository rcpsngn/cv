from django.apps import AppConfig


class ServiceConfig(AppConfig):
    default_auto_filed = "django.db.models.BigAutoField"
    name = "apps.main.service"