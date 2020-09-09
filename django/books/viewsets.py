# Elastic
from django_elasticsearch_dsl_drf.constants import (
    LOOKUP_FILTER_RANGE,
    LOOKUP_QUERY_GT,
    LOOKUP_QUERY_GTE,
    LOOKUP_QUERY_IN,
    LOOKUP_QUERY_LT,
    LOOKUP_QUERY_LTE,
    SUGGESTER_COMPLETION,
)
from django_elasticsearch_dsl_drf.filter_backends import (
    DefaultOrderingFilterBackend,
    FilteringFilterBackend,
    SearchFilterBackend,
    SuggesterFilterBackend,
)
from django_elasticsearch_dsl_drf.viewsets import DocumentViewSet
# Document
from .documents import BookDocument

# Django
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
import requests
from elasticsearch_dsl.connections import connections
# Serializers
from .serializers import BookGetByName
from .serializers import BookGetByNameAuthor
from .serializers import BookDocumentSerializer
# drf yasg
from drf_yasg.utils import swagger_auto_schema as sas
# Utils
from utils.documentation import get_documentation
# Model
from .models import Book
from .models import BookLibrary


@sas(method='get')
@api_view(['GET'])
def get_library_book_by_name(request, *args, **kwargs):
    data = request.data
    serializer = BookGetByNameAuthor(data = request.data)
    if serializer.is_valid():
        title = serializer.validated_data.get('title')
        authors = serializer.validated_data.get('authors')
        book = Book.objects.get(title = title, authors=authors)
        books_library = BookLibrary.objects.filter(book=book)
        list_of_librarys = []
        i = 1
        dict_response = {}
        for book_library in books_library:
            dict_response.update({'Library '+str(i): {}})
            dict_response['Library '+str(i)].update({'name ': book_library.library.name})
            dict_response['Library '+str(i)].update({'price ': book_library.price})
            i += 1
        return Response(
            dict_response,
            status=status.HTTP_200_OK
        )
    return Response(
        serializer.errors,
        status=status.HTTP_400_BAD_REQUEST
    )

@sas(method='get')
@api_view(['GET'])
def get_book(request, *args, **kwargs):
    data = request.data
    serializer = BookGetByName(data = request.data)
    if serializer.is_valid():
        title = serializer.validated_data.get('title')
        
        book_objs = Book.objects.filter(title = title)
        if(len(book_objs) == 0):
            return Response(
                {'El libro no existe'},
                status=status.HTTP_404_NOT_FOUND
            )
            
        list_of_books = []
        i = 1
        dict_response = {}
        for book in book_objs:
            dict_response.update({'Book '+str(i): {}})
            dict_response['Book '+str(i)].update({'summary ': book.summary})
            dict_response['Book '+str(i)].update({'authors ': book.authors})
            dict_response['Book '+str(i)].update({'image_url ': book.image_url})
            i += 1
        return Response(
            dict_response,
            status=status.HTTP_200_OK
        )
    return Response(
        serializer.errors,
        status=status.HTTP_400_BAD_REQUEST
    )
@api_view(['POST'])
def test(request, *args, **kwargs):
    
    print(conn)
    return Response(
        status=status.HTTP_200_OK,
    )


class BookViewSet(DocumentViewSet):
    #conn = connections.create_connection()
    document = BookDocument
    serializer_class = BookDocumentSerializer
    ordering = ('id',)
    lookup_field = 'id'

    filter_backends = [
        DefaultOrderingFilterBackend,
        FilteringFilterBackend,
        SearchFilterBackend,
        SuggesterFilterBackend,
    ]

    search_fields = (
        'title',
    )

    filter_fields = {
        'id': {
            'field': 'id',
            'lookups': [
                LOOKUP_FILTER_RANGE,
                LOOKUP_QUERY_IN,
                LOOKUP_QUERY_GT,
                LOOKUP_QUERY_GTE,
                LOOKUP_QUERY_LT,
                LOOKUP_QUERY_LTE,
            ],
        },
        'title': 'title',
    }

    suggester_fields = {
        'title_suggest': {
            'field': 'title.suggest',
            'suggesters': [
                SUGGESTER_COMPLETION,
            ],
        },
    }