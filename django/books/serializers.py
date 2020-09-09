# rest framework
from rest_framework import serializers

# models
from .models import Book
from .documents import BookDocument
from django_elasticsearch_dsl_drf.serializers import DocumentSerializer

class BookDocumentSimpleSerializer(DocumentSerializer):
    """Serializer for the Book document."""

    # tags = serializers.SerializerMethodField()
    # authors = serializers.SerializerMethodField()

    #summary = serializers.SerializerMethodField()
    #authors = serializers.SerializerMethodField()

    class Meta(object):
        """Meta options."""
        document = BookDocument
        fields = (
            'id',
            'title',
            'summary',
            'authors',
        )

    """
    def get_authors(self, obj):
        print(obj.meta)
        if hasattr(obj.meta, 'authors'):
            return obj.meta.authors
        return None
    def get_summary(self, obj):
        if hasattr(obj.meta, 'summary'):
            return obj.meta.summary
        return None
    """
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