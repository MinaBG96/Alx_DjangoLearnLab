from bookshelf.models import Book

# Retrieve the book you created

book = Book.objects.get(title="1984")
print(book.title, book.author, book.publication_year)

# Expected output:

# 1984 George Orwell 1949
