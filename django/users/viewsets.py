# Models
from .models import User
from tags.models import Tag
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
        user = User(
            email = email,
            first_name = first_name,
            last_name = last_name,
            password = password
        )
        user.save()
        # Asignar tags
        for tag in list_of_tags:
            tag = Tag.objects.get(tag_name = tag)
            user.tag.add(tag)
        return Response(
            {'Usuario creado!'},
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
            user = User.objects.get(email = serializer.validated_data.get('email'))
        except User.DoesNotExist:
            user = None
        if(user):
            list_of_tags = []
            for tag in user.tag.all():
                list_of_tags.append(tag.tag_name)
            response_dict = {
                'first_name': user.first_name,
                'second_name': user.last_name,
                'list_of_tags': list_of_tags
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
