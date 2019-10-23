from django.urls import path, include
from rest_framework import routers

from . import views


router = routers.DefaultRouter()
router.register('genre', views.APIGenreView)#, basename='apigenre')
router.register('author', views.APIAuthorView)#, basename='apiauthor')
router.register('pubhouse', views.APIPubHouseView)#, basename='apipubhouse')
router.register('book', views.APIBookView, basename='apibook')

urlpatterns = [
    path('', views.index, name='index'),

    path('books/', views.BookListView.as_view(), name='books'),
    path('book/<int:pk>/', views.BookDetailView.as_view(), name='book'),
    path('books/create/', views.create_book, name='create_book'),
    path('books/update/<int:id>', views.update_book, name='update_book'),
    path('books/delete/<int:id>', views.delete_book, name='delete_book'),

    path('authors/', views.AuthorListView.as_view(), name='authors'),
    path('author/<int:pk>/', views.AuthorDetailView.as_view(), name='author'),
    path('author/create/', views.create_author, name='create_author'),
    path('author/update/<int:id>', views.update_author, name='update_author'),
    path('author/delete/<int:id>', views.delete_author, name='delete_author'),

    path('pubhouses/', views.PubHouseListView.as_view(), name='pubhouses'),
    path('pubhouse/<int:pk>/', views.PubHouseDetailView.as_view(), name='pub_house'),
    path('pubhouse/create/', views.create_pub_house, name='create_pub_house'),
    path('pubhouse/update/<int:id>', views.update_pub_house, name='update_pub_house'),
    path('pubhouse/delete/<int:id>', views.delete_pub_house, name='delete_pub_house'),

    path('api', include(router.urls)), 
]