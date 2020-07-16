
# views
from . import viewsets as tags_views
from django.conf.urls import include
from django.conf.urls import url
tags_urls = [
    url(
        r'^list-tags$',
        tags_views.get_tags,
        name='tags'
    ),
    url(
        r'^get-books$',
        tags_views.get_book_tags,
        name='tags'
    ),
]
urlpatterns = [
    url(r'^tags/', include(tags_urls)),
]
