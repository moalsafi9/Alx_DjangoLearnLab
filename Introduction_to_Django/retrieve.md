books = Book.objects.all()
for b in books:
print(b.id, b.title, b.author, b.publication_year)
