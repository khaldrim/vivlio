from django.utils.translation import ugettext as _

# Serializers
from users.serializers import UserPostSerializer
from users.serializers import UserGetSerializer

# Response examples
from users.responses import UserGetExample
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
    }
}



ENDPOINTS = {}
ENDPOINTS.update(USERS)

def get_documentation(key):
    return ENDPOINTS.get(key)