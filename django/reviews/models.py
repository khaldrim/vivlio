from django.db import models

# Create your models here.
from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.

class Review(models.Model):
    STAR_CHOICES = (
        (1, "Muy malo"),
        (2, "Malo"),
        (3, "Normal"),
        (4, "Bueno"),
        (5, "Muy bueno"),
    )
    # foreign keys
    book = models.OneToOneField(
        'books.Book',
        verbose_name=_('Libro'),
        blank=True
    )
    # Fields
    user = models.OneToOneField(
        'users.User',
        verbose_name = _('Autor de la reseña'),
        blank=True,
    )
    text = models.CharField(
        _('Texto'),
        blank=True,
        max_length=200,
    )
    stars = models.IntegerField(
        _('Valoración'),
        choices = STAR_CHOICES,
        blank=True,
        null=True,
    )
    def __str__(self):
        object_name = "Reseña de: "+self.user.first_name+" sobre el libro: "+self.book.name
        return object_name