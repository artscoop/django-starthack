# coding: utf-8
from django.views.generic.base import TemplateView


class Index(TemplateView):
    """ Index page viex """

    # Confoigration
    template_name = 'layout/base.html'
