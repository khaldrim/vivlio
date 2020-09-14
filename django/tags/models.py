from django.db import models
from django.utils.translation import ugettext_lazy as _
# Create your models here.


class Tag(models.Model):
    # required fields
    tag_name = models.CharField(
        _('Género'),
        unique=True,
        max_length=50
    )
    affinity = models.IntegerField(
        blank = True,
        null = True
    )
    def __str__(self):
        return self.tag_name
class TagAffinity(models.Model):
    tag_name_affinity = models.CharField(
        _('Género'),
        max_length=50
    )
    affinity = models.IntegerField(
        blank = True,
        null = True
    )
    def __str__(self):
        return self.tag_name_affinity