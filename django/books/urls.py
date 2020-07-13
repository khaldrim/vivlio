
# views
from . import viewsets as books_views
from django.conf.urls import include
from django.conf.urls import url
books_urls = [
    url(
        r'^test$',
        books_views.test,
        name='books'
    ),
    url(
        r'^get-book$',
        books_views.get_book,
        name='books'
    )
]
urlpatterns = [
    url(r'^books/', include(books_urls)),
]
