from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase
from rest_framework import status

from .models import Author, Book


class BookAPITests(APITestCase):
    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(username="testuser", password="testpass123")
        self.author = Author.objects.create(name="Author One")
        self.book1 = Book.objects.create(
            title="First Book",
            publication_year=2000,
            author=self.author,
        )
        self.book2 = Book.objects.create(
            title="Second Book",
            publication_year=2010,
            author=self.author,
        )
        self.book3 = Book.objects.create(
            title="Third Book",
            publication_year=2005,
            author=self.author,
        )

    def test_list_books_unauthenticated(self):
        url = reverse("book-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)

    def test_retrieve_single_book(self):
        url = reverse("book-detail", args=[self.book1.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["id"], self.book1.id)
        self.assertEqual(response.data["title"], self.book1.title)

    def test_create_book_unauthenticated(self):
        url = reverse("book-create")
        data = {
            "title": "New Book",
            "publication_year": 2024,
            "author": self.author.id,
        }
        response = self.client.post(url, data, format="json")
        self.assertIn(response.status_code, [status.HTTP_401_UNAUTHORIZED, status.HTTP_403_FORBIDDEN])

    def test_create_book_authenticated(self):
        self.client.login(username="testuser", password="testpass123")
        url = reverse("book-create")
        data = {
            "title": "New Book Auth",
            "publication_year": 2022,
            "author": self.author.id,
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 4)
        self.assertEqual(Book.objects.last().title, "New Book Auth")

    def test_update_book_unauthenticated(self):
        url = reverse("book-update", args=[self.book1.id])
        data = {
            "title": "Updated Title",
            "publication_year": 2001,
            "author": self.author.id,
        }
        response = self.client.put(url, data, format="json")
        self.assertIn(response.status_code, [status.HTTP_401_UNAUTHORIZED, status.HTTP_403_FORBIDDEN])

    def test_update_book_authenticated(self):
        self.client.login(username="testuser", password="testpass123")
        url = reverse("book-update", args=[self.book1.id])
        data = {
            "title": "Updated Title",
            "publication_year": 2015,
            "author": self.author.id,
        }
        response = self.client.put(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Updated Title")
        self.assertEqual(self.book1.publication_year, 2015)

    def test_delete_book_unauthenticated(self):
        url = reverse("book-delete", args=[self.book2.id])
        response = self.client.delete(url)
        self.assertIn(response.status_code, [status.HTTP_401_UNAUTHORIZED, status.HTTP_403_FORBIDDEN])
        self.assertEqual(Book.objects.count(), 3)

    def test_delete_book_authenticated(self):
        self.client.login(username="testuser", password="testpass123")
        url = reverse("book-delete", args=[self.book2.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 2)

    def test_filter_books_by_publication_year(self):
        url = reverse("book-list")
        response = self.client.get(url, {"publication_year": 2010})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["id"], self.book2.id)

    def test_search_books_by_title(self):
        url = reverse("book-list")
        response = self.client.get(url, {"search": "First"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["id"], self.book1.id)

    def test_search_books_by_author_name(self):
        url = reverse("book-list")
        response = self.client.get(url, {"search": "Author One"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)

    def test_order_books_by_publication_year_ascending(self):
        url = reverse("book-list")
        response = self.client.get(url, {"ordering": "publication_year"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        years = [item["publication_year"] for item in response.data]
        self.assertEqual(years, sorted(years))

    def test_order_books_by_publication_year_descending(self):
        url = reverse("book-list")
        response = self.client.get(url, {"ordering": "-publication_year"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        years = [item["publication_year"] for item in response.data]
        self.assertEqual(years, sorted(years, reverse=True))
