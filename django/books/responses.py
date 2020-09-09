# rest framework
from rest_framework import serializers






class bookGetExample(serializers.Serializer):
    name = serializers.CharField(
        required = False
    )
    author = serializers.CharField(
        required = False
    )
    summary = serializers.CharField(
        required = False
    )
   
class bookGetExampleList(serializers.Serializer):
    book_i = bookGetExample(many = True)