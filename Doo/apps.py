from django.apps import AppConfig


class DooConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Doo'

    def ready(self):
        print("Ready")
        import Doo.signals
