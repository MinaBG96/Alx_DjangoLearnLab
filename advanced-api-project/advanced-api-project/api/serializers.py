from rest_framework import serializers
from .models import Author, Book
import datetime

# -------------------------------------------------------------------
# BookSerializer
# -------------------------------------------------------------------
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'  # id, title, publication_year, author

    def validate_publication_year(self, value):
        current_year = datetime.date.today().year
        if value > current_year:
            raise serializers.ValidationError("publication_year cannot be in the future.")
        return value


# -------------------------------------------------------------------
# AuthorSerializer
# -------------------------------------------------------------------
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)  # uses related_name 'books' from Book.author

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']
