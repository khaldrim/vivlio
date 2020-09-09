from django_elasticsearch_dsl_drf.constants import (
    LOOKUP_FILTER_PREFIX,
    LOOKUP_FILTER_RANGE,
    LOOKUP_FILTER_TERMS,
    LOOKUP_FILTER_WILDCARD,
    LOOKUP_QUERY_EXCLUDE,
    LOOKUP_QUERY_GT,
    LOOKUP_QUERY_GTE,
    LOOKUP_QUERY_IN,
    LOOKUP_QUERY_ISNULL,
    LOOKUP_QUERY_LT,
    LOOKUP_QUERY_LTE,
)
from django_elasticsearch_dsl_drf.filter_backends import (
    DefaultOrderingFilterBackend,
    FacetedSearchFilterBackend,
    FilteringFilterBackend,
    HighlightBackend,
    IdsFilterBackend,
    PostFilterFilteringFilterBackend,
    OrderingFilterBackend,
    SearchFilterBackend,
)
from django_elasticsearch_dsl_drf.viewsets import (
    BaseDocumentViewSet,
)

from elasticsearch_dsl import DateHistogramFacet, RangeFacet

from ..documents import BookDocument
from ..serializers import BookDocumentSimpleSerializer

__all__ = (
    'BaseBookDocumentViewSet',
)


class BaseBookDocumentViewSet(BaseDocumentViewSet):
    """Base BookDocument ViewSet."""

    document = BookDocument
    # serializer_class = BookDocumentSerializer
    serializer_class = BookDocumentSimpleSerializer
    lookup_field = 'id'
    filter_backends = [
        FilteringFilterBackend,
        PostFilterFilteringFilterBackend,
        IdsFilterBackend,
        OrderingFilterBackend,
        DefaultOrderingFilterBackend,
        SearchFilterBackend,
        FacetedSearchFilterBackend,
        # SuggesterFilterBackend,
        # FunctionalSuggesterFilterBackend,
        HighlightBackend,
    ]
    # Define search fields
    search_fields = (
        'title',
        'summary',
    )
    # Define highlight fields
    highlight_fields = {
        'title': {
            'enabled': True,
            'options': {
                'pre_tags': ["<b>"],
                'post_tags': ["</b>"],
            }
        },
        'summary': {
            'options': {
                'fragment_size': 50,
                'number_of_fragments': 3
            }
        },
    }
    # Define filter fields
    filter_fields = {
        'id': {
            'field': 'id',
            'lookups': [
                LOOKUP_FILTER_RANGE,
                LOOKUP_QUERY_IN,
                LOOKUP_QUERY_GT,
                LOOKUP_QUERY_GTE,
                LOOKUP_QUERY_LT,
                LOOKUP_QUERY_LTE,
                LOOKUP_FILTER_TERMS,
            ],
        },
        'title': 'title',
        'summary': 'summary',
        'authors': 'authors',
        'language_code': 'language_code',
        'image_url': 'image_url',
        'small_image_url': 'small_image_url',
        #'price': {
        #    'field': 'price.raw',
        #    'lookups': [
        #        LOOKUP_FILTER_RANGE,
        #    ],
        #},
        #
        #'tags': {
        #    'field': 'tags',
        #    'lookups': [
        #        LOOKUP_FILTER_TERMS,
        #        LOOKUP_FILTER_PREFIX,
        #        LOOKUP_FILTER_WILDCARD,
        #        LOOKUP_QUERY_IN,
        #        LOOKUP_QUERY_EXCLUDE,
        #        LOOKUP_QUERY_ISNULL,
        #    ],
        #},
        #'tags.raw': {
        #    'field': 'tags.raw',
        #    'lookups': [
        #        LOOKUP_FILTER_TERMS,
        #        LOOKUP_FILTER_PREFIX,
        #        LOOKUP_FILTER_WILDCARD,
        #        LOOKUP_QUERY_IN,
        #        LOOKUP_QUERY_EXCLUDE,
        #    ],
        #},
    }
    # Post filter fields, copy filters as they are valid
    # Post filter fields, copy filters as they are valid
    post_filter_fields = {
        
    }
    faceted_search_fields = {
    }
    # Define ordering fields
    ordering_fields = {
        'id': 'id',
        'title': 'title',
    }
    # Specify default ordering
    ordering = ('id', 'title',)
    