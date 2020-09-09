from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.

class Library(models.Model):
    # Fields
    name = models.CharField(
        _('Nombre'),
        blank=True,
        max_length=200,
    )
    address = models.CharField(
        _('Dirección'),
        blank=True,
        max_length=200,
    )

    def __str__(self):
        return self.name