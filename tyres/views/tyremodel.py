# coding: utf-8
from django.urls.base import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, CreateView, UpdateView

from tyres.models.manufacturer import Manufacturer
from tyres.models.tyremodel import TyreModel


# Symbols imported with the wildcard
__all__ = ['TyreModelCreate', 'TyreModelDelete', 'TyreModelDetail', 'TyreModelUpdate']


class TyreModelDetail(DetailView):
    """ Class view to display a tyre model information """

    # Configuration
    model = TyreModel
    template_name = 'tyres/tyremodel/tyremodel-detail.html'

    # Overrides
    def get_context_data(self, **kwargs):
        """
        Return the context passed to render the template

        :param kwargs: internal, not used here
        :return: context passed to render the template
        :rtype: dict
        """
        context = super().get_context_data(**kwargs)
        return context


class TyreModelCreate(CreateView):
    """ Class view to add a new tyre model """

    # Configuration
    model = TyreModel
    template_name = 'tyres/tyremodel/tyremodel-edit.html'
    fields = ['name', 'description', 'manufacturer', 'radius']
    success_url = reverse_lazy('index')


class TyreModelUpdate(UpdateView):
    """ Class view to edit an existing tyre model """

    # Configuration
    model = TyreModel
    template_name = 'tyres/tyremodel/tyremodel-edit.html'
    fields = ['name', 'description', 'manufacturer', 'radius']
    success_url = reverse_lazy('index')


class TyreModelDelete(DeleteView):
    """ Class view to remove a tyre model """

    # Configuration
    model = TyreModel
    template_name = 'tyres/tyremodel/tyremdel-delete.html'
    success_url = reverse_lazy('index')
