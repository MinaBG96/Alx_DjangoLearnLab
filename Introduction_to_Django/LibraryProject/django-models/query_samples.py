# relationship_app/query_samples.py

import os
import django
import sys
from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent

sys.path.append(str(PROJECT_ROOT))


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LibraryProject.settings")
django.setup()

from relationship_app.models import Author, Book, Library, Librarian


def main():
    print("--- 1. Creating Test Data ---")

    # إنشاء المؤلفين
    author1, _ = Author.objects.get_or_create(name="Author One")
    author2, _ = Author.objects.get_or_create(name="Author Two")

    # إنشاء الكتب
    book1, _ = Book.objects.get_or_create(
        title="Book A (by Author One)", author=author1
    )
    book2, _ = Book.objects.get_or_create(
        title="Book B (by Author One)", author=author1
    )
    book3, _ = Book.objects.get_or_create(
        title="Book C (by Author Two)", author=author2
    )

    library1, _ = Library.objects.get_or_create(name="Main Library")

    library1.books.add(book1, book3)

    librarian1, _ = Librarian.objects.get_or_create(
        name="Mr. Library Man", library=library1
    )

    print("Test data created/verified successfully.\n")

    # -------------------------------------------------

    print("--- 2. Running Required Queries ---")

    print(f"\nQuery 1: All books by {author1.name}:")
    books_by_author = author1.books.all()
    for book in books_by_author:
        print(f"- {book.title}")

    print(f"\nQuery 2: All books in {library1.name}:")
    books_in_library = library1.books.all()
    for book in books_in_library:
        print(f"- {book.title}")

    print(f"\nQuery 3: Librarian for {library1.name}:")
    librarian = library1.librarian
    print(f"- {librarian.name}")

    print("\n--- Queries Complete ---")


if __name__ == "__main__":
    main()
