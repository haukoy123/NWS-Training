import unittest
from models import Author, Book, Book_Author, Session
session = Session()
from sqlalchemy import func

def count_book(id=None):
    if id is None:
        return 0
    authors = session.query(
        func.count(Book.name).label('count')
    ).select_from(Author).join(Book_Author).join(Book).filter(Author.id==id).first()
    return authors.count



class TestAuthor(unittest.TestCase):
    def setUp(self):
        return super().setUp()

    def test_id_is_none(self):
        self.assertEqual(count_book(), 0)

    def test_author_has_no_book(self):
        self.assertEqual(count_book(4), 0)

    def test_author_has_one_books(self):
        self.assertEqual(count_book(2), 1)

    def test_author_has_two_books(self):
        self.assertEqual(count_book(1), 2)