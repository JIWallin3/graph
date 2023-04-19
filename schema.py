import graphene
from graphene_django import DjangoObjectType

from library import models


class AuthorType(DjangoObjectType):
    class Meta:
        model = models.Author


class BookType(DjangoObjectType):
    class Meta:
        model = models.Book


class Query(graphene.ObjectType):
    authors = graphene.List(AuthorType)
    books = graphene.List(BookType)
    books_by_author = graphene.List(BookType, author_last_name=graphene.String())

    # Using info.context property to check if request from authenticated user
    def resolve_authors(self, info):
        if info.context.user.is_authenticated():
            return models.Author.objects.all()
        else:
            return None

    def resolve_books(self, info):
        if info.context.user.is_authenticated():
            return models.Book.objects.all()
        else:
            return None

    def resolve_books_by_author(self, info, author_last_name):
        if info.context.user.is_authenticated():
            return models.Book.objects.get(author__last_name=author_last_name)
        else:
            return None


# Define schema that is referenced in settings.py based on query function above
schema = graphene.Schema(query=Query)
