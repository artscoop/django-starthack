# coding: utf-8
from uuid import uuid4

from django.db import models
from django.urls.base import reverse
from django.utils.timezone import now
from django.utils.translation import ugettext_lazy as _, pgettext_lazy
from model_utils.choices import Choices


class TyreModelQuerySet(models.QuerySet):
    """ Queryset for tyre models """

    # Getter and properties
    def in_production(self):
        """
        Returns the tyre models that you can still find in production

        :return: a (sub)queryset of all the tyre models still in production
        :rtype: models.QuerySet<TyreModel>
        """
        return self.filter(in_production=True)


class TyreModel(models.Model):
    """ A tyre model """

    # Constants
    RADIUS_CHOICES = Choices(
        (450, 'standard', _("standard")),
        (296, 'small', _("small")),
        (710, 'jumbo', _("jumbo")),
    )

    # Fields
    uuid = models.UUIDField(default=uuid4, verbose_name=_("UUID"))
    name = models.CharField(max_length=64, verbose_name=_("name"))
    description = models.TextField(blank=True, verbose_name=_("description"))
    manufacturer = models.ForeignKey('tyres.manufacturer', related_name='tyre_models', verbose_name=_("manufacturer"))
    radius = models.FloatField(default=RADIUS_CHOICES.standard, help_text=_("value in mm"), verbose_name=_("radius"))
    in_production = models.BooleanField(default=True, verbose_name=_("in production"))
    creation_date = models.DateTimeField(default=now, verbose_name=pgettext_lazy('tyres.tyre', "created on"))

    # Manager
    objects = TyreModelQuerySet.as_manager()

    # Metadata
    class Meta:
        verbose_name = _("tyre model")
        verbose_name_plural = _("tyre models")
        unique_together = ('name', 'manufacturer'),
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
        return reverse('index')
