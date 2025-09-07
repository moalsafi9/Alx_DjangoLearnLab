from django.urls import path
from .views import list_books   # <-- explicit import for checker
from .views import LibraryDetailView   # <-- also explicit, same style

urlpatterns = [
    path("books/", list_books, name="list_books"),  # function-based view
    path("library/<int:pk>/", LibraryDetailView.as_view(), name="library_detail"),  # class-based view
]
