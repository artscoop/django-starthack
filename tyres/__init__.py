# coding: utf-8
from django.apps.config import AppConfig
from django.utils.translation import ugettext_lazy


class TyresConfig(AppConfig):
    """ Django Configuration class for the tyres application """

    # Configuration
    name = 'tyres'
    label = 'tyres'
    verbose_name = ugettext_lazy("Tyres")

    # Overrides
    def ready(self):
        pass


# Automatically configure app when used with name "tyres"
default_app_config = 'tyres.TyresConfig'
