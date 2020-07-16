from django.contrib import admin


# models
from .models import Tag

@admin.register(Tag)
class tagAdmin(admin.ModelAdmin):
    pass
