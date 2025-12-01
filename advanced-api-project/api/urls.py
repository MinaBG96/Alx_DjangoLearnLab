from django.urls import path
from .views import (
    BookListView,
    BookDetailView,
    BookCreateView,
    BookUpdateView,
    BookDeleteView,
)

urlpatterns = [
    # ListView: 
    # GET /api/books/
    path('books/', BookListView.as_view(), name='book-list'),

    # DetailView:  pk
    # GET /api/books/1/
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),

    # CreateView: 
    # POST /api/books/create/
    path('books/create/', BookCreateView.as_view(), name='book-create'),

    # UpdateView: 
    # PUT/PATCH /api/books/1/update/
    path('books/<int:pk>/update/', BookUpdateView.as_view(), name='book-update'),

    # DeleteView: 
    # DELETE /api/books/1/delete/
    path('books/<int:pk>/delete/', BookDeleteView.as_view(), name='book-delete'),
]
