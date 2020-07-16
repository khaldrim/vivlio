# rest framework
from rest_framework import serializers

# models
from .models import User

class UserPostSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()
    list_of_tags = serializers.ListField(child=serializers.CharField())
    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'email',
            'password',
            'list_of_tags'
        )
class UserGetSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    class Meta:
        model = User
        fields = (
            'email',
        )

class UserAddgenres(serializers.Serializer):
    rut = serializers.CharField()
