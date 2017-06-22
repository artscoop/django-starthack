# coding: utf-8
from django.contrib import admin
from django.contrib.admin.options import ModelAdmin

from tyres.models.tyremodel import TyreModel


@admin.register(TyreModel)
class TyreModelAdmin(ModelAdmin):
    """ Admin configuration for tyre models """

    # Configuration
    list_display = ['id', 'uuid', 'name', 'manufacturer', 'in_production']
    list_filter = ['creation_date', 'manufacturer', 'in_production']
    search_fields = ['name', 'uuid', 'manufacturer__name']
    list_select_related = True
