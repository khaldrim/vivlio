# rest framework
from rest_framework import serializers

# models
from .models import Book

class BookGetByNameAuthor(serializers.ModelSerializer):
    title = serializers.CharField()
    authors = serializers.CharField()
    class Meta:
        model = Book
        fields = (
            'title',
            'authors'
        )

class BookGetByName(serializers.ModelSerializer):
    title = serializers.CharField()
    class Meta:
        model = Book
        fields = (
            'title',
        )