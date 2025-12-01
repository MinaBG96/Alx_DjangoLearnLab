from django.urls import path
from .views import (
    BookListView,
    BookDetailView,
    BookCreateView,
    BookUpdateView,
    BookDeleteView,
)

urlpatterns = [
    # GET /api/books/
    path('books/', BookListView.as_view(), name='book-list'),

    # GET /api/books/<pk>/
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),

    # POST /api/books/create/
    path('books/create/', BookCreateView.as_view(), name='book-create'),

    # PUT/PATCH /api/books/update/<pk>/
    path('books/update/<int:pk>/', BookUpdateView.as_view(), name='book-update'),

    # DELETE /api/books/delete/<int:pk>/
    path('books/delete/<int:pk>/', BookDeleteView.as_view(), name='book-delete'),
]
