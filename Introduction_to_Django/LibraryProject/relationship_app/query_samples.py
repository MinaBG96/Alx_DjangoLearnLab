import os
import django
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LibraryProject.settings")
django.setup()

from relationship_app.models import Author, Book, Library, Librarian


def create_sample_data():
    author_name = "Author One"
    library_name = "Main Library"

    author, _ = Author.objects.get_or_create(name=author_name)
    library, _ = Library.objects.get_or_create(name=library_name)
    book, _ = Book.objects.get_or_create(title="Book One", author=author)
    library.books.add(book)
    Librarian.objects.get_or_create(name="Librarian One", library=library)


def queries():
    author_name = "Author One"
    author = Author.objects.get(name=author_name)
    books_by_author = author.books.all()
    print(f"Books by {author_name}: {[b.title for b in books_by_author]}")

    library_name = "Main Library"
    library = Library.objects.get(name=library_name)
    books_in_library = library.books.all()
    print(f"Books in {library_name}: {[b.title for b in books_in_library]}")

    librarian = Librarian.objects.get(library=library)
    print(f"Librarian for {library_name}: {librarian.name}")


if __name__ == "__main__":
    create_sample_data()  # نتأكد من وجود بيانات أولاً
    queries()
