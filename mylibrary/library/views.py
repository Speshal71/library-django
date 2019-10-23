from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views import generic
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets, permissions
from django.db.models.functions import Concat
from django.db.models import CharField, Value as V

from .models import Pub_house, Author, Genre, Book
from .forms import AuthorForm, BookForm, PubHouseForm
from .serializers import GenreSerializer, AuthorSerializer, PubHouseSerializer, BookSerializer


def index(request):
    num_books = len(Book.objects.all())
    num_inst_books = sum(book.count for book in Book.objects.all())
    num_authors = len(Author.objects.all())
    num_pub = len(Pub_house.objects.all())

    context = {
        'num_books': num_books,
        'num_inst_books': num_inst_books,
        'num_authors': num_authors,
        'num_pub': num_pub,
    }

    return render(request, 'index.html', context=context)


class BookListView(generic.ListView):
    model = Book
    context_object_name = 'books'
    template_name = '../templates/book_list.html'
    paginate_by = 5

    def get_queryset(self):
        if self.request.GET.get('filter'):
            query = Book.objects.filter(name__contains=self.request.GET.get('filter'))
        else:
            query = Book.objects.all()
        
        return query


class BookDetailView(generic.DetailView):
    model = Book
    template_name = '../templates/book_detail.html'


class AuthorListView(generic.ListView):
    model = Author
    context_object_name = 'authors'
    template_name = '../templates/author_list.html'
    paginate_by = 5

    def get_queryset(self):
        if self.request.GET.get('filter'):
            a = Author.objects.annotate(
                fullname=Concat(
                    'first_name', V(' '), 'second_name', V(' '), 'last_name',
                    output_field=CharField()
                ),
            )
            query = a.filter(fullname__contains=self.request.GET.get('filter'))
        else:
            query = Author.objects.all()
        
        return query


class AuthorDetailView(generic.DetailView):
    model = Author
    template_name = '../templates/author_detail.html'


class PubHouseListView(generic.ListView):
    model = Pub_house
    context_object_name = 'ph'
    template_name = '../templates/pub_houses_list.html'
    paginate_by = 5

    def get_queryset(self):
        if self.request.GET.get('filter'):
            query = Pub_house.objects.filter(name__contains=self.request.GET.get('filter'))
        else:
            query = Pub_house.objects.all()
        
        return query


class PubHouseDetailView(generic.DetailView):
    model = Pub_house
    context_object_name = 'ph'
    template_name = '../templates/pub_house_detail.html'


def create_record(request, Form, redir_link):
    if request.method == 'POST':
        form = Form(request.POST)

        if form.is_valid():
            form.save()
            return redirect(redir_link)

    form = Form()

    return render(request, '../templates/create_record.html', {'form': form})


def update_record(request, record, Form, redir_link, del_link):
    if request.method == 'POST':
        form = Form(request.POST, instance=record)

        if form.is_valid():
            form.save()
            return redirect(redir_link)

    form = Form(instance=record)

    return render(request, '../templates/create_record.html', {'form': form, 'record': record, 'del_link': del_link})


def delete_record(request, record, redir_link):
    if request.method == 'POST':
        record.delete()
        return redirect(redir_link)
    
    return render(request, 'confirm_delete.html', {'record': record})


@login_required
def create_author(request):
    return create_record(request, AuthorForm, 'authors')


@login_required
def update_author(request, id):
    return update_record(request, Author.objects.get(id=id), AuthorForm, 'authors', 'delete_author')
     

@login_required
def delete_author(request, id):
    return delete_record(request, Author.objects.get(id=id), 'authors')


@login_required
def create_book(request):
    return create_record(request, BookForm, 'books')


@login_required
def update_book(request, id):
    return update_record(request, Book.objects.get(id=id), BookForm, 'books', 'delete_book')
     

@login_required
def delete_book(request, id):
    return delete_record(request, Book.objects.get(id=id), 'books')


@login_required
def create_pub_house(request):
    return create_record(request, PubHouseForm, 'pubhouses')


@login_required
def update_pub_house(request, id):
    return update_record(request, Pub_house.objects.get(id=id), PubHouseForm, 'pubhouses', 'delete_pub_house')
     

@login_required
def delete_pub_house(request, id):
    return delete_record(request, Pub_house.objects.get(id=id), 'pubhouses')


class APIGenreView(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class APIAuthorView(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class APIPubHouseView(viewsets.ModelViewSet):
    queryset = Pub_house.objects.all()
    serializer_class = PubHouseSerializer


class APIBookView(viewsets.ModelViewSet):
    serializer_class = BookSerializer

    def get_queryset(self):
        title = self.request.GET.get('title', '')
        pub_name = self.request.query_params.get('pub_name', '')
        fn = self.request.query_params.get('fn', '')
        sn = self.request.query_params.get('sn', '')
        ln = self.request.query_params.get('ln', '')

        query = Book.objects.filter(name__startswith=title, 
                                    pub_house_fk__name__startswith=pub_name,
                                    author__first_name__startswith=fn,
                                    author__second_name__startswith=sn,
                                    author__last_name__startswith=ln).distinct()
        
        return query