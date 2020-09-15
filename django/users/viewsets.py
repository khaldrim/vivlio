# Models
from .models import User
from tags.models import Tag
from books.models import Book
from tags.models import TagAffinity
from numpy.random import choice
# Django
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

# Serializer
from .serializers import UserPostSerializer
from .serializers import UserGetSerializer
from .serializers import UserAddgenres
# Utils
from utils.documentation import get_documentation
# drf yasg
from drf_yasg.utils import swagger_auto_schema as sas



#@sas(**get_documentation('post_user'))
@api_view(['POST'])
def post_user(request, *args, **kwargs):
    data = request.data
    
    serializer = UserPostSerializer(data = request.data)
    if serializer.is_valid():
        email = serializer.validated_data.get('email')
        try:
            user = User.objects.get(email = email)
        except User.DoesNotExist:
            user = None
        if(user):
            return Response(
                {'El usuario ya existe'},
                status=status.HTTP_200_OK,
            )
        first_name = serializer.validated_data.get('first_name')
        last_name = serializer.validated_data.get('last_name')
        password = serializer.validated_data.get('password')
        list_of_tags = serializer.validated_data.get('list_of_tags')
        list_of_affinities = serializer.validated_data.get('list_of_affinities')
        user = User(
            email = email,
            first_name = first_name,
            last_name = last_name,
            password = password
        )
        user.save()
        # Asignar tags
        i = 0
        while i < len(list_of_tags):
            tagAux = list_of_tags[i]
            affinity = int(list_of_affinities[i])
            tag = Tag.objects.get(tag_name = tagAux)
            user.tag.add(tag)
            tagAffinity = TagAffinity.objects.create(
                tag_name_affinity = tagAux,
                affinity = affinity
            )
            user.tagAffinity.add(tagAffinity)
            i = i+1
        user.save()
        return Response(
            {'Usuario creado!'},
            status=status.HTTP_201_CREATED,
        )
    return Response(
        serializer.errors,
        status=status.HTTP_400_BAD_REQUEST
    )
@api_view(['POST'])
def get_user(request, *args, **kwargs):
    data = request.data
    
    serializer = UserGetSerializer(data = request.data)
    if serializer.is_valid():
        try:
            user = User.objects.get(email = serializer.validated_data.get('email'))
        except User.DoesNotExist:
            user = None
        if(user):
            list_of_tags = []
            list_of_affinities = []
            print(user.tagAffinity.all())
            for tag in user.tagAffinity.all():
                list_of_tags.append(tag.tag_name_affinity)
                list_of_affinities.append(tag.affinity)

            response_dict = {
                'first_name': user.first_name,
                'second_name': user.last_name,
                'list_of_tags': list_of_tags,
                'list_of_affinities': list_of_affinities
            }
            return Response(
                response_dict,
                status=status.HTTP_200_OK,
            ) 
        return Response(
            {'El usuario no existe'},
            status=status.HTTP_400_BAD_REQUEST,
        )
    return Response(
        serializer.errors,
        status=status.HTTP_400_BAD_REQUEST
    )

@api_view(['POST'])
def get_recomendations(request, *args, **kwargs):
    data = request.data
    serializer = UserGetSerializer(data = request.data)
    if serializer.is_valid():
        try:
            user = User.objects.get(email = serializer.validated_data.get('email'))
        except User.DoesNotExist:
            user = None
        if(user):
            list_of_affinities = []
            list_of_affinities_aux = user.tagAffinity.all()
            tags = user.tag.all()
            i = 0
            for tag in tags:
                if(tag.tag_name == list_of_affinities_aux[i].tag_name_affinity):
                    list_of_affinities.append(list_of_affinities_aux[i].affinity)
                i = i+1
            list_of_books = []
            i = 0
            for tag in tags:
                books = Book.objects.filter(tag = tag)
                random_books = choice(books, list_of_affinities[i])
                i = i+1
                list_of_books.extend(random_books)
            final = choice(list_of_books, 20)
            dict_response = {}
            i = 1
            for book in final:
                dict_response.update({'Book '+str(i): {}})
                dict_response['Book '+str(i)].update({'title': book.title})
                dict_response['Book '+str(i)].update({'summary': book.summary})
                dict_response['Book '+str(i)].update({'tags': {}})
                j = 1
                for tag in book.tag.all():
                    dict_response['Book '+str(i)]['tags'].update({'tag_name '+str(j): tag.tag_name})
                    j = j+1
                i += 1
           
            return Response (
                dict_response,
                status=status.HTTP_200_OK
            )

        return Response(
            {'El usuario no existe'},
            status=status.HTTP_400_BAD_REQUEST,
        )
    return Response(
        serializer.errors,
        status=status.HTTP_400_BAD_REQUEST
    )