import datetime

from django.test import TestCase
from django.utils import timezone

from .models import Book, Library

# Create your tests here.
def create_book(return_date):
    """
    Create a book with the given `return_date`.
    """
    library = Library.objects.create(name='Library')
    return Book.objects.create(title='Title', return_date=return_date, library=library)

class BookModelTests(TestCase):
    def test_return_next_week_with_old_book(self):
        """
        return_next_week() returns True for books whose return_date
        is within one week.
        """
        date = timezone.now() + datetime.timedelta(days=6)
        old_book = create_book(return_date=date)
        self.assertIs(old_book.return_next_week(), True)
        
    def test_return_next_week_with_new_book(self):
        """
        return_next_week() returns False for books whose return_date
        is not within one week.
        """
        date = timezone.now() + datetime.timedelta(days=8)
        new_book = create_book(return_date=date)
        self.assertIs(new_book.return_next_week(), False)