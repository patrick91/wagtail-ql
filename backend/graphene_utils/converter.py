from wagtail.wagtailcore.fields import StreamField
from graphene.types import Scalar

from graphene_django.converter import convert_django_field


class StreamFieldType(Scalar):
    @staticmethod
    def serialize(dt):
        return dt.stream_data


@convert_django_field.register(StreamField)
def convert_stream_field(field, registry=None):
    return StreamFieldType(
        description=field.help_text, required=not field.null
    )
