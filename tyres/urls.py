# coding: utf-8
from django.conf.urls import url

from tyres.views.manufacturer import ManufacturerCreate, ManufacturerDelete, ManufacturerDetail, ManufacturerList, ManufacturerUpdate

app_name = 'tyres'

urlpatterns = [
    # Manufacturers
    url(r'^manufacturer/list/$', ManufacturerList.as_view(), name='manufacturer-list'),
    url(r'^manufacturer/create/$', ManufacturerCreate.as_view(), name='manufacturer-create'),
    url(r'^manufacturer/(?P<pk>[0-9]+)/$', ManufacturerDetail.as_view(), name='manufacturer-detail'),
    url(r'^manufacturer/(?P<pk>[0-9]+)/update/$', ManufacturerUpdate.as_view(), name='manufacturer-update'),
    url(r'^manufacturer/(?P<pk>[0-9]+)/delete/$', ManufacturerDelete.as_view(), name='manufacturer-delete'),
]
