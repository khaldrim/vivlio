# Django
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
import requests
# Serializers
#from .serializers import BookGetSerializer
# drf yasg
from drf_yasg.utils import swagger_auto_schema as sas
# Utils
from utils.documentation import get_documentation
# Model
from .models import Library
from books.models import BookLibrary


@api_view(['GET'])
def get_library(request, *args, **kwargs):
    i = 1
    library_objs = Library.objects.all()
    dict_response = {}
    for library in library_objs:
        dict_response.update({'Library '+str(i): {}})
        dict_response['Library '+str(i)].update({'name ': library.name})
        dict_response['Library '+str(i)].update({'address ': library.address})
        i += 1
    return Response(
        dict_response,
        status=status.HTTP_200_OK,
    )