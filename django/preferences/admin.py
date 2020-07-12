from django.contrib import admin


# models
from .models import Preferences

@admin.register(Preferences)
class PreferencesAdmin(admin.ModelAdmin):
    pass
