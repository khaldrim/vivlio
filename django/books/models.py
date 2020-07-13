from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.

class Book(models.Model):
    # foreign keys
    genres = models.ManyToManyField(
        'genres.Genres',
        verbose_name=_('Género'),
        blank=True
    )

    # Fields
    author = models.CharField(
        _('Autor'),
        blank=True,
        max_length=20,
    )
    summary = models.CharField(
        _('Resumen'),
        blank=True,
        max_length=100,
    )
    name = models.CharField(
        _('Nombre'),
        blank=True,
        max_length=50,
    )

    def __str__(self):
        return self.name