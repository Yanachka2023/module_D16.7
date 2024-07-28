from django.apps import AppConfig

class BillboardAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'billboard_app'

def ready(self):
        from . import signals