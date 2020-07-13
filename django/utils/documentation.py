from django.utils.translation import ugettext as _

# Serializers
from users.serializers import UserPostSerializer
from users.serializers import UserGetSerializer
from users.serializers import UserAddgenres
from books.serializers import BookGetSerializer

# Response examples
from users.responses import UserGetExample
from genres.responses import genresItemGetGenresExample
from books.responses import bookGetExampleList
USERS = {
    'post_user': {
        'methods': ['post'],
        'query_serializer': UserPostSerializer,
        'operation_id': 'Add new user',
        'operation_summary': _('Add new user to the system.'),
        'responses': {
            200: _('User already exists'),
            201: _('User created'),
            400: _('Bad request'),
        }
    },
    'get_user': {
        'methods': ['get'],
        'query_serializer': UserGetSerializer,
        'operation_id': 'Get user data',
        'operation_summary': _('Get user information.'),
        'responses': {
            200: UserGetExample,
            400: _('Bad request'),
        }
    },
    'list_user_genres': {
        'methods': ['get'],
        'query_serializer': UserGetSerializer,
        'operation_id': 'Get user genres',
        'operation_summary': _('Get user genres.'),
        'responses': {
            200: UserGetExample,
            400: _('Bad request'),
        }
    },
    'add_genre_to_user': {
        'methods': ['post'],
        'query_serializer': UserAddgenres,
        'operation_id': 'Add genres to user',
        'operation_summary': _('Add genres to user.'),
        'responses': {
            200: _('Preferencias agregadas al usuario!'),
            400: _('Bad request'),
        }
    }
}
GENRES = {
    'get_all_genres': {
        'methods': ['get'],
        'query_serializer': None,
        'operation_id': 'List all genres',
        'operation_summary': _('List all genres.'),
        'responses': {
            200: genresItemGetGenresExample,
        }
    }
}
BOOKS = {
    'get_book': {
        'methods': ['get'],
        'query_serializer': BookGetSerializer,
        'operation_id': 'List books by author, by genres or by name.',
        'operation_summary': _('List books by author, by genres, or by name.'),
        'responses': {
            200: bookGetExampleList,
            400: _('Bad request'),
        }
    }
}

ENDPOINTS = {}
ENDPOINTS.update(USERS)
ENDPOINTS.update(GENRES)
ENDPOINTS.update(BOOKS)

def get_documentation(key):
    return ENDPOINTS.get(key)