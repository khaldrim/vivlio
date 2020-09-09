
# views
from . import viewsets as library_views
from django.conf.urls import include
from django.conf.urls import url
library_urls = [
    url(
        r'^list-library$',
        library_views.get_library,
        name='library'
    ),
]
urlpatterns = [
    url(r'^library/', include(library_urls)),
]
