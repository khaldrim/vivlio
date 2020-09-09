from django.db import models
from django.utils.translation import ugettext_lazy as _
from library.models import Library
# Create your models here.


class Book(models.Model):
    # foreign keys
    tag = models.ManyToManyField(
        'tags.Tag',
        verbose_name=_('Género'),
        blank=True
    )
    library = models.ManyToManyField(
        'library.Library',
        verbose_name=_('Librería'),
        through='BookLibrary',
        blank=True
    )
    # Fields
    authors = models.CharField(
        _('Autor'),
        blank=True,
        max_length=300,
    )
    title = models.CharField(
        _('Título'),
        blank=True,
        max_length=400,
    )
    summary = models.CharField(
        _('Resumen'),
        blank=True,
        null=True,
        max_length=10000,
    )
    goodreads_book_id = models.IntegerField(
        blank = True,
        null = True
    )
    best_book_id = models.IntegerField(
        blank = True,
        null = True
    )
    work_id = models.IntegerField(
        blank = True,
        null = True
    )
    books_count = models.IntegerField(
        blank = True,
        null = True
    )
    isbn = models.IntegerField(
        blank = True,
        null = True
    )
    isbn13 = models.IntegerField(
        blank = True,
        null = True
    )
    
    original_publication_year = models.IntegerField(
        blank = True,
        null = True
    )
    original_title = models.CharField(
        blank=True,
        max_length=200,
    )
    language_code = models.CharField(
        blank=True,
        max_length=200,
    )
    image_url = models.CharField(
        blank=True,
        max_length=500,
    )
    small_image_url = models.CharField(
        blank=True,
        max_length=200,
    )
    

    def __str__(self):
        return self.title

class BookLibrary(models.Model):
    book = models.ForeignKey(Book)
    library = models.ForeignKey(Library)
    price = models.IntegerField(
        blank = True,
        null = True
    )