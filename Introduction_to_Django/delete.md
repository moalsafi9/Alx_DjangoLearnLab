book = Book.objects.get(id=1)
book.delete()
Book.objects.all()
