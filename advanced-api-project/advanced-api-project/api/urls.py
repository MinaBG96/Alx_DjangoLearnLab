from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookListCreateView, AuthorListCreateView, BookViewSet

router = DefaultRouter()
router.register(r'books', BookViewSet, basename='book')

urlpatterns = [
    path('books-list/', BookListCreateView.as_view(), name='books-list'),
    path('authors/', AuthorListCreateView.as_view(), name='authors-list'),
    path('', include(router.urls)),
]
