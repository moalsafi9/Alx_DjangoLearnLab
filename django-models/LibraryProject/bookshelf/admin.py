from django.contrib import admin
from .models import Book

# Basic registration
class BookAdmin(admin.ModelAdmin):
    # Show these fields in the list page (table view)
    list_display = ("title", "author", "publication_year")

    # Add filters in the sidebar (e.g., filter by year)
    list_filter = ("publication_year",)

    # Enable search by title or author
    search_fields = ("title", "author")
    
admin.site.register(Book, BookAdmin)