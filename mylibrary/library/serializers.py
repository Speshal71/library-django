from rest_framework import serializers
from .models import Genre, Author, Pub_house, Book


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id', 'genre']


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'first_name', 'second_name', 'last_name', 'desc']


class PubHouseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pub_house
        fields = ['id', 'name', 'phone', 'email', 'desc']


class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'name', 'desc', 'count', 'pub_house_fk', 'author', 'genre']