# Models
from .models import Preferences
# Django
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

# Serializer
#from .serializers import UserPostSerializer
#from .serializers import UserGetSerializer
# Utils
from utils.documentation import get_documentation
# drf yasg
from drf_yasg.utils import swagger_auto_schema as sas


"""
@sas(**get_documentation('post_user'))
@api_view(['POST'])
def post_user(request, *args, **kwargs):
    data = request.data
"""