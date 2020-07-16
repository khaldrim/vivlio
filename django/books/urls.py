
# views
from . import viewsets as books_views
from django.conf.urls import include
from django.conf.urls import url
books_urls = [
    url(
        r'^get-library-book$',
        books_views.get_library_book_by_name,
        name='book'
    ),
    url(
        r'^get-book$',
        books_views.get_book,
        name='book'
    )
]
urlpatterns = [
    url(r'^books/', include(books_urls)),
]
