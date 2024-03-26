import logging
from django.test import TestCase
from django.urls import reverse
from .models import Book, Individual, Author, Book_Issue, BookInstance
from django.utils import timezone
from datetime import timedelta

logger = logging.getLogger(__name__)

class LibraryManagementSystemTestCase(TestCase):
    def setUp(self):
        # Create sample data for testing
        self.author = Author.objects.create(name="John Doe", bio="Sample bio")
        self.book = Book.objects.create(book_title="Sample Book", author=self.author, book_pages=200)  # Provide a value for book_pages
        self.individual = Individual.objects.create(fullname="Alice Smith", address="Sample Address", Email="alice@example.com")
        self.book_instance = BookInstance.objects.create(book=self.book)

        # Create a book issue record
        self.issue = Book_Issue.objects.create(individual=self.individual, book_instance=self.book_instance, due_date=timezone.now() + timedelta(days=7))

    def test_display_books_list(self):
        # Test the view for displaying the list of books
        logger.info("Testing display_books_list")
        response = self.client.get(reverse('show_books'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Sample Book")

    def test_search_books(self):
        # Test the view for searching books
        logger.info("Testing search_books")
        response = self.client.get(reverse('search_books') + '?query=Sample')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Sample Book")

    def test_search_books_by_author(self):
        # Test the view for searching books by author
        logger.info("Testing search_books_by_author")
        response = self.client.get(reverse('search_books') + '?query=John')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Sample Book")


    def test_delete_book(self):
        # Test the view for deleting a book
        logger.info("Testing delete_book")
        response = self.client.post(reverse('delete_book_data', args=[self.book.id]))
        self.assertEqual(response.status_code, 302)  # Redirect status code
        self.assertFalse(Book.objects.filter(id=self.book.id).exists())  # Check if the book is deleted

    
    def test_search_books(self):
        # Test the view for searching books
        logger.info("Testing search_books")
        response = self.client.get(reverse('search_books') + '?query=Sample')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Sample Book")

    def test_search_books_by_author(self):
        # Test the view for searching books by author
        logger.info("Testing search_books_by_author")
        response = self.client.get(reverse('search_books') + '?query=John')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Sample Book")

    def test_book_issue_and_return(self):
        # Test the view for issuing and returning a book
        logger.info("Testing book_issue_and_return")
        response = self.client.post(reverse('book_issue'), {'individual': self.individual.id,
                                                            'book_instance': self.book_instance.id,
                                                            'due_date': timezone.now() + timedelta(days=14),
                                                            'remarks_on_issue': 'Good condition'})
        self.assertEqual(response.status_code, 302)  # Redirect status code
        self.assertTrue(Book_Issue.objects.filter(individual=self.individual, book_instance=self.book_instance).exists())  # Check if the book is issued

        # Check if the book instance is borrowed before attempting to return it
        self.assertTrue(BookInstance.objects.filter(id=self.book_instance.id, is_borrowed=True).exists())

        response = self.client.post(reverse('return_issued_book', args=[self.issue.id]))
        self.assertEqual(response.status_code, 302)  # Redirect status code
        self.assertFalse(BookInstance.objects.filter(id=self.book_instance.id, is_borrowed=True).exists())  # Check if the book is returned

    def test_count_books(self):
        # Test to count the number of books
        logger.info("Testing count_books")
        expected_count = 1  # Update this with the expected count of books
        actual_count = Book.objects.count()
        self.assertEqual(actual_count, expected_count)

    def tearDown(self):
        # Clean up after each test
        pass
