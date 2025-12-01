from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework


from .serializers import BookSerializer


class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    filter_backends = [
        DjangoFilterBackend,   # للـ filtering
        filters.SearchFilter,  # للـ search
        filters.OrderingFilter # للـ ordering
    ]

    # 1) FILTERING

    #   /api/books/?title=Harry
    #   /api/books/?author=1
    #   /api/books/?publication_year=1997
    filterset_fields = ['title', 'author', 'publication_year']

    # 2) SEARCH
    #   /api/books/?search=Rowling
    #   /api/books/?search=Harry
    search_fields = ['title', 'author__name']
    ordering_fields = ['title', 'publication_year']
    ordering = ['title']



class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # مهم: لازم يكون عامل تسجيل دخول

    def perform_create(self, serializer):
        serializer.save()


class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        publication_year = serializer.validated_data.get('publication_year')
        if publication_year is not None and publication_year < 1800:
            from rest_framework.exceptions import ValidationError
            raise ValidationError("لا نسمح بكتب أقدم من سنة 1800 في هذا النظام (مثال تعليمي).")

        serializer.save()


class BookDeleteView(generics.DestroyAPIView):

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_destroy(self, instance):
        instance.delete()
