from django.test import TestCase
from main.models import Book 
class TestBook(TestCase): 
    def test_book_creation(self): 
        book = Book.objects.create(name='book1') 
        self.assertEqual(Book.objects.all().count(), 1) 