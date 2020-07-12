# Models
from .models import User
# Django
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

# Serializer
from .serializers import UserPostSerializer
from .serializers import UserGetSerializer
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