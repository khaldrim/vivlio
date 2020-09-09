from django.contrib import admin


# models
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass
