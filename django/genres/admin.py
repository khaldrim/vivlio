from django.contrib import admin


# models
from .models import Genres

@admin.register(Genres)
class genresAdmin(admin.ModelAdmin):
    pass
