# rest framework
from rest_framework import serializers

# models
from .models import User

class UserPostSerializer(serializers.ModelSerializer):
    rut = serializers.CharField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.EmailField()
    class Meta:
        model = User
        fields = (
            'rut',
            'first_name',
            'last_name',
            'email',
        )
class UserGetSerializer(serializers.ModelSerializer):
    rut = serializers.CharField()
    class Meta:
        model = User
        fields = (
            'rut',
        )