"""
Security Measures Implemented:
- CSRF protection using {% csrf_token %}.
- Query sanitization using Django ORM to prevent SQL injection.
- Added Content Security Policy header.
- Secure cookie settings in settings.py (CSRF + SESSION_COOKIE_SECURE).
"""




# Create your views here.
from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from .models import Book
from django.db.models import Q
from .forms import ExampleForm



@permission_required("bookshelf.can_view", raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, "bookshelf/book_list.html", {"books": books})

def secure_search(request):
    query = request.GET.get("q", "")

    # Avoid SQL Injection – using ORM only
    books = Book.objects.filter(
        Q(title__icontains=query)
    )

    return render(request, "bookshelf/book_list.html", {"books": books, "query": query})
