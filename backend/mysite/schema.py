import graphene

from home.schema import Page
from home.models import SitePage


class Query(graphene.ObjectType):
    pages = graphene.List(Page)

    @graphene.resolve_only_args
    def resolve_pages(self):
        return SitePage.objects.all()


schema = graphene.Schema(query=Query)
