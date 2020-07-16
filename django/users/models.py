from django.db import models
from django.utils.translation import ugettext_lazy as _
# Create your models here.


class User(models.Model):
    # Foreign
    tag = models.ManyToManyField(
        'tags.Tag',
        verbose_name=_('Preferencia'),
        blank=True
    )

    # required fields
    email = models.EmailField(
        _('Email'),
        unique=True,
        db_index=True,
    )
    password = models.CharField(
        _('Contraseña'),
        max_length=100,
        blank=True,
    )
    # optional fields
    first_name = models.CharField(
        _('Nombre'),
        max_length=100,
        blank=True,
    )
    last_name = models.CharField(
        _('Apellido'),
        max_length=100,
        blank=True,
    )

    def __str__(self):
        return self.first_name +" "+ self.last_name
