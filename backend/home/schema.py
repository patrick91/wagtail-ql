from graphene_django import DjangoObjectType

from .models import SitePage


class Page(DjangoObjectType):
    class Meta:
        model = SitePage
