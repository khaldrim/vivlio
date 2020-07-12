from django.db import models

# Create your models here.
from django.db import models
from django.utils.translation import ugettext_lazy as _
# Create your models here.


class Preferences(models.Model):
    # foreign keys
    user = models.ManyToManyField(
        'users.User',
        verbose_name=_('Usuario'),
        null=True,
    )

    # required fields
    genre = models.CharField(
        _('genre'),
        unique=True,
        max_length=20,
    )
    

    def __str__(self):
        return self.genre 
