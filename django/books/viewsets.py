# Elastic
from django_elasticsearch_dsl import (
    Document,
    fields,
    Index,
)
# Django
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
import requests
from elasticsearch_dsl.connections import connections
# Serializers
from .serializers import BookGetByName
from .serializers import BookGetByNameAuthor
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
"""
@api_view(['POST'])
def test(request, *args, **kwargs):
    conn = connections.create_connection()
    print(conn)
    return Response(
        status=status.HTTP_200_OK,
    )
@sas(**get_documentation('get_book'))
@sas(method='get')
@api_view(['GET'])
def get_book(request, *args, **kwargs):
    data = request.data
    
    serializer = BookGetSerializer(data = request.data)
    if serializer.is_valid():
        author = serializer.validated_data.get('author')
        genres = serializer.validated_data.get('genres')
        name = serializer.validated_data.get('name')
        if(author):
            books = Book.objects.filter(author = author)
        if(genres):
            genre = Genres.objects.get(genre = genres)
            books = Book.objects.filter(genres = genre)
        if(author and genres):
            genre = Genres.objects.get(genre = genres)
            books = Book.objects.filter(author = author, genres = genre)
        if(name):
            books = Book.objects.filter(name = name)
        if(author and name):
            books = Book.objects.filter(name = name, author = author)
        if(name and genre):
            genre = Genres.objects.get(genre = genres)
            books = Book.objects.filter(genres = genre, name = name)
        if(name and genre and author):
            genre = Genres.objects.get(genre = genres)
            books = Book.objects.filter(genres = genre, author = author,name = name)

        i = 1
        dict_response = {}
        for book in books:
            dict_response.update({'book '+str(i): {}})
            dict_response['book '+str(i)].update({'name ': book.name})
            dict_response['book '+str(i)].update({'author ': book.author})
            dict_response['book '+str(i)].update({'summary ': book.summary})
            i += 1
        return Response(
            dict_response,
            status=status.HTTP_200_OK,
        )   
    return Response(
        serializer.errors,
        status=status.HTTP_400_BAD_REQUEST
    )
@sas(**get_documentation('post_book'))
@api_view(['POST'])
def post_book(request, *args, **kwargs):
    data = request.data
    
    serializer = BookPostSerializer(data = request.data)
    if serializer.is_valid():
"""
