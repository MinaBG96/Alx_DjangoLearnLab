from django.db import models

# Create your models here.
from django.db import models


class Author(models.Model):

    name = models.CharField(
        max_length=255,
        help_text="اسم المؤلف"
    )

    def __str__(self):
        return self.name


class Book(models.Model):

    title = models.CharField(
        max_length=255,
        help_text="عنوان الكتاب"
    )
    publication_year = models.IntegerField(
        help_text="سنة نشر الكتاب"
    )
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name='books', 
        help_text="المؤلف المرتبط بهذا الكتاب"
    )

    def __str__(self):
        return f"{self.title} ({self.publication_year})"
