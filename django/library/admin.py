from django.contrib import admin


# models
from .models import Library

@admin.register(Library)
class libraryAdmin(admin.ModelAdmin):
    pass
