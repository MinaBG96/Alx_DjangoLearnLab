from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer


class BookListCreateView(generics.ListCreateAPIView):

    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_queryset(self):

        queryset = super().get_queryset()
        year = self.request.query_params.get("year")
        if year is not None:
            queryset = queryset.filter(publication_year=year)
        return queryset

    def perform_create(self, serializer):
        serializer.save()


class BookRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_update(self, serializer):

        serializer.save()

    def perform_destroy(self, instance):

        instance.delete()
