from graphene.types.generic import GenericScalar

from graphene_django import DjangoObjectType

from .models import SitePage


class Page(DjangoObjectType):
    body_json = GenericScalar(required=True)

    class Meta:
        model = SitePage

    def resolve_body(self, info):
        return self.body

    def resolve_body_json(self, info):
        return self.body.stream_data
