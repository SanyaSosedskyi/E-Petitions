import factory

from books import models 

from accounts import factories as account_factories


class GenreFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Genre

    name = 'Example name'


class BookFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Book
    
    genre = factory.SubFactory(GenreFactory)
    year = 2000
    title = 'Example title'
    author = 'Example author'
    pages = 200
    description = 'Example description'
    price = 200
    in_stock = 100


class CommentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Comment
    
    profile = factory.SubFactory(account_factories.ProfileFactory)
    book = factory.SubFactory(BookFactory)
    text = 'Example text'

