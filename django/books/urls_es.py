
from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from .es_viewsets import (
    BookDocumentViewSet,
    BookMoreLikeThisDocumentViewSet,
    BookMoreLikeThisNoOptionsDocumentViewSet
)

__all__ = ('urlpatterns',)

router = DefaultRouter()


# **********************************************************
# ************************** Books *************************
# **********************************************************
router.register(
    r'books',
    BookDocumentViewSet,
    base_name='bookdocument'
)

router.register(
    r'books-more-like-this',
    BookMoreLikeThisDocumentViewSet,
    base_name='bookdocument_more_like_this'
)
router.register(
    r'books-more-like-this-no-options',
    BookMoreLikeThisNoOptionsDocumentViewSet,
    base_name='bookdocument_more_like_this_no_options'
)

# **********************************************************
# ********************** URL patterns **********************
# **********************************************************

urlpatterns = [
    url(r'^', include(router.urls)),
]