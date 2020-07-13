# Models
from .models import User
from genres.models import Genres
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



@sas(**get_documentation('post_user'))
@api_view(['POST'])
def post_user(request, *args, **kwargs):
    data = request.data
    
    serializer = UserPostSerializer(data = request.data)
    if serializer.is_valid():
        try:
            user = User.objects.get(rut = serializer.validated_data.get('rut'))
        except User.DoesNotExist:
            user = None
        if(user):
           return Response(
                {'El usuario ya existe'},
                status=status.HTTP_200_OK,
            ) 
        user = User(
            rut = serializer.validated_data.get('rut'),
            email = serializer.validated_data.get('email'),
            first_name = serializer.validated_data.get('first_name'),
            last_name = serializer.validated_data.get('last_name')
        )
        user.save()
        return Response(
            {'Usuario creado exitosamente!'},
            status=status.HTTP_201_CREATED,
        )
    return Response(
        serializer.errors,
        status=status.HTTP_400_BAD_REQUEST
    )

@sas(**get_documentation('get_user'))
@sas(method='get')
@api_view(['GET'])
def get_user(request, *args, **kwargs):
    data = request.data
    
    serializer = UserGetSerializer(data = request.data)
    if serializer.is_valid():
        try:
            user = User.objects.get(rut = serializer.validated_data.get('rut'))
        except User.DoesNotExist:
            user = None
        if(user):
            response_dict = {
                'first_name': user.first_name,
                'second_name': user.last_name,
                'email': user.email,
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

@sas(**get_documentation('list_user_genres'))
@sas(method='get')
@api_view(['GET'])
def get_genres(request, *args, **kwargs):
    data = request.data
    
    serializer = UserGetSerializer(data = request.data)
    if serializer.is_valid():
        try:
            user = User.objects.get(rut = serializer.validated_data.get('rut'))
        except User.DoesNotExist:
            user = None
        if(user):
            dict_response = {'genres': {}}
            i = 1
            for genre in user.genres_set.all():
                dict_response['genres'].update({'genre '+str(i): genre.genre})
                i += 1
            return Response(
                dict_response,
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
    """
    for genre in genres:
        dict_response['genres'].update({'genre '+str(i): genre.genre})
        i += 1
    return Response(
        dict_response,
        status=status.HTTP_200_OK,
    )  
    """

@sas(**get_documentation('add_genre_to_user'))
@api_view(['POST'])
def add_genres(request, *args, **kwargs):
    data = request.data
    serializer = UserAddgenres(data = request.data)
    if serializer.is_valid():
        list_of_genres = serializer.validated_data.get('list_of_genres')
        try:
            user = User.objects.get(rut = serializer.validated_data.get('rut'))
        except User.DoesNotExist:
            user = None
        if(user):
            for genre in list_of_genres:
                genre = Genres.objects.get(genre = genre)
                genre.user.add(user)
            return Response(
                {'Preferencias agregadas al usuario!'},
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