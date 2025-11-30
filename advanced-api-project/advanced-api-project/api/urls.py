from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .  import BookListCreateView, AuthorListCreateView, BookViewSet 
from api import views

router = DefaultRouter()
router.register(r'books', BookViewSet, basename='book')

urlpatterns = [
    path('books-list/', BookListCreateView.as_view(), name='books-list'),
    path('', include(router.urls)),
    path('books/<int:pk>/', BookRetrieveUpdateDestroyView.as_view(), name='book-detail'),
    path('books/', BookListCreateView.as_view(), name='book-list-create'),
]
