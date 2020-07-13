# rest framework
from rest_framework import serializers

# models
from .models import Book

class BookGetSerializer(serializers.ModelSerializer):
    author = serializers.CharField(required = False)
    genres = serializers.CharField(required = False)
    name = serializers.CharField(required = False)
    class Meta:
        model = Book
        fields = (
            'author',
            'genres',
            'name'
        )