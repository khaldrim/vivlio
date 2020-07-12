# rest framework
from rest_framework import serializers

# models
from .models import User


class UserGetExample(serializers.ModelSerializer):
    first_name = serializers.CharField(
        required = False
    )
    last_name = serializers.CharField(
        required = False
    )
    email = serializers.EmailField(
        required = False
    )
    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'email',
        )