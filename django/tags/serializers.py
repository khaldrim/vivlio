# rest framework
from rest_framework import serializers

# models
from .models import Tag

class GetBooksTag(serializers.ModelSerializer):
    list_of_tags = serializers.ListField(child=serializers.CharField())
    class Meta:
        model = Tag
        fields = (
            'list_of_tags',
        )