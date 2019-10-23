from django.db import models


class Pub_house(models.Model):
    name  = models.CharField(max_length=100, verbose_name='Name')
    phone = models.CharField(max_length=100, verbose_name='Phone')
    email = models.CharField(max_length=100, verbose_name='Email')
    desc  = models.TextField(max_length=1000, help_text='The description of publishing house', verbose_name='Description')

    def __str__(self):
        return self.name


class Author(models.Model):
    first_name  = models.CharField(max_length=100, verbose_name='First name')
    second_name = models.CharField(max_length=100, verbose_name='Second name')
    last_name   = models.CharField(max_length=100, verbose_name='Last name')
    desc = models.TextField(max_length=1000, help_text='The description of author', verbose_name='Description')

    def __str__(self):
        return ' '.join([self.first_name, self.second_name, self.last_name])


class Genre(models.Model):
    genre  = models.CharField(max_length=100, verbose_name='Genre name')

    def __str__(self):
        return self.genre


class Book(models.Model):
    name  = models.CharField(max_length=200, verbose_name='Name')
    desc  = models.TextField(max_length=1000, help_text='The description of the book', verbose_name='Description')
    count = models.PositiveIntegerField(help_text='The current number of available books', verbose_name='Count')
    
    pub_house_fk = models.ForeignKey(Pub_house, on_delete=models.SET_NULL, null=True, verbose_name='Publishing House')

    author = models.ManyToManyField(Author)
    genre  = models.ManyToManyField(Genre) 

    def __str__(self):
        return self.name