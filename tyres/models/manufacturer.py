# coding: utf-8
from uuid import uuid4

from django.db import models
from django.urls.base import reverse
from django.utils.translation import ugettext_lazy as _


class ManufacturerQuerySet(models.QuerySet):
    """ Queryset for tyre manufacturers """
    pass


class Manufacturer(models.Model):
    """ Model for tyre manufacturers """

    # Fields
    uuid = models.UUIDField(default=uuid4, verbose_name=_("UUID"))
    name = models.CharField(max_length=64, unique=True, verbose_name=_("name"))

    # Manager
    objects = ManufacturerQuerySet.as_manager()

    # Metadata
    class Meta:
        verbose_name = _("manufacturer")
        verbose_name_plural = _("manufacturers")
        app_label = 'tyres'

    # Overrides
    def __str__(self):
        """ Return a string representation of the object """
        return str(self.name)

    def save(self, *args, **kwargs):
        """ Save the object to the database """
        super(self.__class__, self).save(*args, **kwargs)

    def get_absolute_url(self):
        """ Return the URL to access this model view page """
        return reverse('tyres:manufacturer-detail', kwargs={'pk': self.id})

    # Getters and properties
    def get_tyre_models(self):
        """
        Returns the tyre models linked to this manufacturer

        :return: A queryset of TyreModel that have a FK to this manufacturer
        :rtype: models.QuerySet<TyreModel>
        """
        return self.tyre_models.all()
