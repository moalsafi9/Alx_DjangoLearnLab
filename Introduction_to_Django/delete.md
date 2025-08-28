# Fetch the book instance you want to delete

book = Book.objects.get(title="1984")

# Delete it

book.delete()
