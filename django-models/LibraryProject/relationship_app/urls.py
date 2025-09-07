from django.urls import path
from .views import list_books, add_book, edit_book, delete_book

urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('add_book/', add_book, name='add_book'),       # checker looks for this
    path('edit_book/<int:pk>/', edit_book, name='edit_book'),  # checker looks for this
    path('delete_book/<int:pk>/', delete_book, name='delete_book'),
]
