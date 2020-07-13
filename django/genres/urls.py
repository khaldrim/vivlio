
# views
from . import viewsets as genres_views
from django.conf.urls import include
from django.conf.urls import url
genres_urls = [
    url(
        r'^list-all$',
        genres_views.get_all_genres,
        name='users'
    )
]
urlpatterns = [
    url(r'^genres/', include(genres_urls)),
]
