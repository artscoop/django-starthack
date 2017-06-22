# coding: utf-8
from django.contrib import admin
from django.contrib.admin.options import ModelAdmin

from tyres.models.manufacturer import Manufacturer


@admin.register(Manufacturer)
class ManufacturerAdmin(ModelAdmin):
    """ Admin configuration for tyre manufacturers """

    # Configuration
    list_display = ['id', 'uuid', 'name']
    list_filter = []
    search_fields = ['name', 'uuid']
