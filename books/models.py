from django.db import models
from datetime import datetime, timedelta
import uuid
from django.utils import timezone


def get_returndate():
    return timezone.now() + timedelta(days=8)


class Individual(models.Model):
    fullname = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    Email = models.EmailField(max_length=100)

    def __str__(self):
        return self.fullname


class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    book_title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    book_pages = models.PositiveIntegerField(blank=True)
    summary = models.TextField(max_length=500, help_text="Summary about the book", null=True, blank=True)
    image = models.ImageField(upload_to='book_images/', null=True, blank=True)  # Image field

    @property
    def is_available(self):
        return self.bookinstance_set.filter(is_borrowed=False).exists()

    def __str__(self):
        return self.book_title


class BookInstance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Book unique id across the Library")
    book = models.ForeignKey(Book, on_delete=models.CASCADE, null=True)
    is_borrowed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.id} {self.book}"


class Book_Issue(models.Model):
    individual = models.ForeignKey(Individual, on_delete=models.CASCADE)
    book_instance = models.ForeignKey(BookInstance, on_delete=models.CASCADE)
    issue_date = models.DateTimeField(auto_now=True, help_text="Date the book is issued")
    due_date = models.DateTimeField(default=get_returndate, help_text="Date the book is due to")
    date_returned = models.DateField(null=True, blank=True, help_text="Date the book is returned")
    remarks_on_issue = models.CharField(max_length=100, default="Book in good condition", help_text="Book remarks/condition during issue")
    remarks_on_return = models.CharField(max_length=100, default="", help_text="Book remarks/condition during return")

    def __str__(self):
        return self.individual.fullname + " borrowed " + self.book_instance.book.book_title
