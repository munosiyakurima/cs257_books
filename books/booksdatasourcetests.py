'''
   booksdatasourcetest.py
   Jeff Ondich, 24 September 2021
'''

from booksdatasource import Author, Book, BooksDataSource
import unittest

class BooksDataSourceTester(unittest.TestCase):
    def setUp(self):
        self.data_source = BooksDataSource('books1.csv')

    def tearDown(self):
        pass

    def test_unique_author(self):
        authors = self.data_source.authors('Pratchett')
        self.assertTrue(len(authors) == 1)
        self.assertTrue(authors[0] == Author('Pratchett', 'Terry'))

    def test_unique_book(self):
        books = self.data_source.books('Blackout')
        self.assertTrue(len(books) == 1)
        self.assertTrue(books[0] == Book('Blackout'))

    def test_unique_book_numbers(self):
        books = self.data_source.books('1Q84')
        self.assertTrue(len(books) == 1)
        self.assertTrue(books[0] == Book('1Q84'))

    def test_unique_book_repeat_title(self):
        books = self.data_source.books('and')
        self.assertTrue(len(books) == 7)
        self.assertTrue(books[0] == Book('And Then There Were None'))
        self.assertTrue(books[1] == Book('Boys and Sex'))
        self.assertTrue(books[2] == Book('Girls and Sex'))
        self.assertTrue(books[3] == Book('Hard-Boiled Wonderland and the End of the World'))
        self.assertTrue(books[4] == Book('Pride and Prejudice'))
        self.assertTrue(books[5] == Book('Sense and Sensibility'))
        self.assertTrue(books[6] == Book('\"The Life and Opinions of Tristram Shandy, Gentleman\"'))

    def test_all_books(self):
        tiny_data_source = BooksDataSource('tinybooks.csv')
        books = tiny_data_source.books()
        self.assertTrue(len(books) == 3)
        self.assertTrue(books[0].title == 'Emma')
        self.assertTrue(books[1].title == 'Neverwhere')
        self.assertTrue(books[2].title == 'Omoo')

    def test_all_authors(self):
        tiny_data_source = BooksDataSource('tinybooks.csv')
        authors = tiny_data_source.authors()
        self.assertTrue(len(authors) == 3)
        self.assertTrue(authors[0] == Author('Austen', 'Jane'))
        self.assertTrue(authors[1] == Author('Gaiman', 'Neil'))
        self.assertTrue(authors[2] == Author('Melville', 'Herman'))

        
if __name__ == '__main__':
    unittest.main()

