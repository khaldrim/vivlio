# Models
from .models import Genres
# Django
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from django.core import serializers

# Serializer

# Utils
from utils.documentation import get_documentation
# drf yasg
from drf_yasg.utils import swagger_auto_schema as sas

@sas(**get_documentation('get_all_genres'))
@sas(method='get')
@api_view(['GET'])
def get_all_genres(request, *args, **kwargs):
    genres = Genres.objects.all()
    dict_response = {'genres': {}}
    i = 1
    for genre in genres:
        dict_response['genres'].update({'genre '+str(i): genre.genre})
        i += 1
    return Response(
        dict_response,
        status=status.HTTP_200_OK,
    )     


