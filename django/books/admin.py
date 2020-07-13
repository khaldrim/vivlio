from django.contrib import admin


# models
from .models import Book

@admin.register(Book)
class booksAdmin(admin.ModelAdmin):
    pass
