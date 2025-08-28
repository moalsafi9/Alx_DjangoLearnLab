# Retrieve Operation (Bookshelf App)

This document explains how to perform the **Read / Retrieve** operation for the `Book` model in the `bookshelf` app.

---

## Retrieve All Books

```python
from bookshelf.models import Book

# Get all books
books = Book.objects.all()

print(books)
```
