from django.db import models
from django.utils.translation import ugettext_lazy as _
# Create your models here.


class User(models.Model):
    # required fields
    rut = models.CharField(
        _('rut'),
        unique=True,
        db_index=True,
        max_length=20,
    )
    email = models.EmailField(
        _('email address'),
        unique=True,
        db_index=True,
    )
    # optional fields
    first_name = models.CharField(
        _('first name'),
        max_length=100,
        blank=True,
    )
    last_name = models.CharField(
        _('last name'),
        max_length=100,
        blank=True,
    )

    def __str__(self):
        return self.first_name +" "+ self.last_name
