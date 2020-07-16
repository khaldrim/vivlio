
# views
from . import viewsets as users_views
from django.conf.urls import include
from django.conf.urls import url
users_urls = [
    url(
        r'^create$',
        users_views.post_user,
        name='users'
    ),
    url(
        r'^get$',
        users_views.get_user,
        name='users'
    )
]
urlpatterns = [
    url(r'^users/', include(users_urls)),
]
