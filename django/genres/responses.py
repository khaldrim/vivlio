# rest framework
from rest_framework import serializers




class genresGetGenresExample(serializers.Serializer):
    genre = serializers.CharField(
        required = False
    )
   
class genresItemGetGenresExample(serializers.Serializer):
    genres = genresGetGenresExample(many = True)
