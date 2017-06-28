# coding: utf-8
from django.urls.base import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, CreateView, UpdateView
from django.views.generic.list import ListView

from tyres.models.manufacturer import Manufacturer


# Symbols imported with the wildcard
__all__ = ['ManufacturerList', 'ManufacturerCreate', 'ManufacturerDelete', 'ManufacturerDetail', 'ManufacturerUpdate']


class ManufacturerList(ListView):
    """ Class view to display the whole list of manufacturers """

    # Configuration
    model = Manufacturer
    template_name = 'tyres/manufacturer/manufacturer-list.html'


class ManufacturerDetail(DetailView):
    """ Class view to display a manufacturer's information """

    # Configuration
    model = Manufacturer
    template_name = 'tyres/manufacturer/manufacturer-detail.html'

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


class ManufacturerCreate(CreateView):
    """ Class view to add a new manufacturer """

    # Configuration
    model = Manufacturer
    template_name = 'tyres/manufacturer/manufacturer-edit.html'
    fields = ['name']
    success_url = reverse_lazy('index')


class ManufacturerUpdate(UpdateView):
    """ Class view to edit an existing manufacturer """

    # Configuration
    model = Manufacturer
    template_name = 'tyres/manufacturer/manufacturer-edit.html'
    fields = ['name']

    # Overrides
    def get_success_url(self):
        """ Returns redirection target upon form validation """
        return self.object.get_absolute_url()


class ManufacturerDelete(DeleteView):
    """ Class view to remove a manufacturer """

    # Configuration
    model = Manufacturer
    template_name = 'tyres/manufacturer/manufacturer-delete.html'
    success_url = reverse_lazy('index')
