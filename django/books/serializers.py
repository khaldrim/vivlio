# rest framework
from rest_framework import serializers

# models
from .models import Book
from .documents import BookDocument
from django_elasticsearch_dsl_drf.serializers import DocumentSerializer

class BookDocumentSerializer(DocumentSerializer):
    class Meta:
        document = BookDocument
        fields = (
            'id',
            'title',
            'summary'
        )

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