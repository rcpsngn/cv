from django.apps import AppConfig


class ReferenceConfig(AppConfig):
    default_auto_filed = "django.db.models.BigAutoField"
    name = "apps.main.reference"