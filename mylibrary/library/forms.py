from django import forms
from .models import Genre, Author, Book, Pub_house

class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = ['genre']


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['first_name', 'second_name', 'last_name', 'desc']


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['name', 'count', 'pub_house_fk', 'author', 'genre', 'desc']


class PubHouseForm(forms.ModelForm):
    class Meta:
        model = Pub_house
        fields = ['name', 'phone', 'email', 'desc']