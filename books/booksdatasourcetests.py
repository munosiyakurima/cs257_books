'''
   booksdatasourcetest.py
   Jeff Ondich, 24 September 2021
   
   Adapted By:
   Muno Siyakurima and Kyle Machalec
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
        self.assertTrue(books[0] == Book('\"The Life and Opinions of Tristram Shandy, Gentleman\"'))
        self.assertTrue(books[1] == Book('And Then There Were None'))
        self.assertTrue(books[2] == Book('Boys and Sex'))
        self.assertTrue(books[3] == Book('Girls and Sex'))
        self.assertTrue(books[4] == Book('Hard-Boiled Wonderland and the End of the World'))
        self.assertTrue(books[5] == Book('Pride and Prejudice'))
        self.assertTrue(books[6] == Book('Sense and Sensibility'))

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

    def test_all_books_year(self):
        tiny_data_source = BooksDataSource('tinybooks.csv')
        books = tiny_data_source.books(sort_by = 'year')
        self.assertTrue(len(books) == 3)
        self.assertTrue(books[0].title == 'Emma')
        self.assertTrue(books[1].title == 'Omoo')
        self.assertTrue(books[2].title == 'Neverwhere')

    def test_between_two_years(self):
        books_between_years = self.data_source.books_between_years(start_year = 1920, end_year = 1938)
        self.assertTrue(len(books_between_years) == 6)
        self.assertTrue(books_between_years[0].title == 'Main Street')
        self.assertTrue(books_between_years[1].title == 'Leave it to Psmith')
        self.assertTrue(books_between_years[2].title == 'Elmer Gantry')
        self.assertTrue(books_between_years[3].title == '\"Right Ho, Jeeves\"')
        self.assertTrue(books_between_years[4].title == 'Murder on the Orient Express')
        self.assertTrue(books_between_years[5].title == 'The Code of the Woosters')

    def test_start_year_only(self):
        books_between_years = self.data_source.books_between_years(start_year = 2016)
        self.assertTrue(len(books_between_years) == 5)
        self.assertTrue(books_between_years[0].title == 'Girls and Sex')
        self.assertTrue(books_between_years[1].title == '\"There, There\"')
        self.assertTrue(books_between_years[2].title == '\"Fine, Thanks\"')
        self.assertTrue(books_between_years[3].title == 'Boys and Sex')
        self.assertTrue(books_between_years[4].title == 'The Invisible Life of Addie LaRue')

    def test_end_year_only(self):
        books_between_years = self.data_source.books_between_years(end_year = 1840)
        self.assertTrue(len(books_between_years) == 4)
        self.assertTrue(books_between_years[0].title == '\"The Life and Opinions of Tristram Shandy, Gentleman\"')
        self.assertTrue(books_between_years[1].title == 'Pride and Prejudice')
        self.assertTrue(books_between_years[2].title == 'Sense and Sensibility')
        self.assertTrue(books_between_years[3].title == 'Emma')

    def test_no_end_or_start_year(self):
        tiny_data_source = BooksDataSource('tinybooks.csv')
        books_between_years = tiny_data_source.books_between_years()
        self.assertTrue(len(books_between_years) == 3)
        self.assertTrue(books_between_years[0].title == 'Emma')
        self.assertTrue(books_between_years[1].title == 'Omoo')
        self.assertTrue(books_between_years[2].title == 'Neverwhere')
        
if __name__ == '__main__':
    unittest.main()

