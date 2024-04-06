import datetime

from django.test import TestCase
from django.utils import timezone

from .models import Book

# Create your tests here.
def create_book(return_date):
    """
    Create a book with the given `return_date`.
    """
    return Book.objects.create(title='Title', return_date=return_date, library='Library')

class BookModelTests(TestCase):
    def test_return_next_week_with_old_book(self):
        """
        return_next_week() returns True for books whose return_date
        is within one week.
        """
        date = timezone.now() + datetime.timedelta(days=6, hours=23)
        old_book = create_book(return_date=date)
        self.assertIs(old_book.return_next_week(), True)
        
    def test_return_next_week_with_new_book(self):
        """
        return_next_week() returns False for books whose return_date
        is not within one week.
        """
        date = timezone.now() + datetime.timedelta(days=7, hours=1)
        new_book = create_book(return_date=date)
        self.assertIs(new_book.return_next_week(), False)