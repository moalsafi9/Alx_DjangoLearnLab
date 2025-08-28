# Create Operation (Bookshelf App)

This document explains how to perform the **Create** operation for the `Book` model in the `bookshelf` app.

---

## Model Reference

The `Book` model has the following fields:

- `title` (CharField)
- `author` (CharField)
- `publication_year` (IntegerField)

---

## Using the Django Shell

To create a new book record:

```python
from bookshelf.models import Book

# Create a new book instance
book = Book.objects.create(
    title="1984",
    author="George Orwell",
    publication_year=1949
)

# Verify the object
print(book)
```
