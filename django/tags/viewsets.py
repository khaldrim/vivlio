# Django
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
import requests
# Serializers
from .serializers import GetBooksTag
# drf yasg
from drf_yasg.utils import swagger_auto_schema as sas
# Utils
from utils.documentation import get_documentation
# Model
from .models import Tag
from books.models import Book


@api_view(['GET'])
def get_tags(request, *args, **kwargs):
    i = 1
    tag_objs = Tag.objects.all()
    dict_response = {}
    for tag in tag_objs:
        dict_response.update({'Tag '+str(i): {}})
        dict_response['Tag '+str(i)].update({'name ': tag.tag_name})
        i += 1
    return Response(
        dict_response,
        status=status.HTTP_200_OK,
    )

@sas(method='get')
@api_view(['GET'])
def get_book_tags(request, *args, **kwargs):
    data = request.data
    serializer = GetBooksTag(data = request.data)
    if serializer.is_valid():
        list_of_tags = serializer.validated_data.get('list_of_tags')
        dict_response = {}
        for tag in list_of_tags:
            tag_obj = Tag.objects.get(tag_name = tag) 
            dict_response.update({tag: {}})
            book_objs = Book.objects.filter(tag = tag_obj)
            list_of_books = []
            i = 1
            for book in book_objs:
                dict_response[tag].update({'Book '+str(i): {}})
                dict_response[tag]['Book '+str(i)].update({'summary ': book.summary})
                dict_response[tag]['Book '+str(i)].update({'authors ': book.authors})
                dict_response[tag]['Book '+str(i)].update({'image_url ': book.image_url})
                i += 1
        return Response(
            dict_response,
            status=status.HTTP_200_OK,
        )
    return Response(
        serializer.errors,
        status=status.HTTP_400_BAD_REQUEST
    )