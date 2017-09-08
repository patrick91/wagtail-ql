from django.apps import AppConfig


class MyAppConfig(AppConfig):
    name = 'graphene_utils'

    def ready(self):
        from . import converter  # noqa