# Fetch the book instance you want to update

book = Book.objects.get(title="1984")

# Update its author

book.author = "George Orwell (Updated)"
book.save()
