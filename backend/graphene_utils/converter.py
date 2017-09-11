from wagtail.wagtailcore.fields import StreamField
from graphene.types import Scalar, Union, String

from graphene_django.converter import convert_django_field


class StreamFieldType(Scalar):
    @staticmethod
    def serialize(dt):
        return dt.stream_data


class StreamFieldTypesUnion(Union):
    class Meta:
        types = (String,)


@convert_django_field.register(StreamField)
def convert_stream_field(field, registry=None):
    return StreamFieldTypesUnion()
