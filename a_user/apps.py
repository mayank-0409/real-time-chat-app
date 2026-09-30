from django.apps import AppConfig


class AUserConfig(AppConfig):
    name = 'a_user'

    def ready(self):
        import a_user.signals