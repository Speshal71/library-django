from django.contrib import admin

from .models import Pub_house, Author, Genre, Book


admin.site.register(Pub_house)
admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(Book)
