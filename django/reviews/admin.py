from django.contrib import admin


# models
from .models import Review

@admin.register(Review)
class reviewsAdmin(admin.ModelAdmin):
    pass
