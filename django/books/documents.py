from django_elasticsearch_dsl import (
    Document,
    fields,
    Index,
)

from .models import Book

book_index = Index('books')

book_index.settings(
    number_of_shards=1,
    number_of_replicas=0
)


@book_index.doc_type
class BookDocument(Document):
    title = fields.TextField(
        attr='title',
        fields={
            'suggest': fields.Completion(),
        }
    )
    summary = fields.TextField(
        attr='summary',
        fields={
            'suggest': fields.Completion(),
        }
    )
    tag = fields.ObjectField(
        properties={
            'tag_name': fields.TextField()
        }
    )
    class Django:
        model = Book
        fields = [
            'id',
        ]
