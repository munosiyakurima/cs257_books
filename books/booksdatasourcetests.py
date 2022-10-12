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
        self.tiny_data_source = BooksDataSource('tinybooks.csv')

    def tearDown(self):
        BooksDataSource.authors_list = {}
        BooksDataSource.authors_list = set()
        BooksDataSource.books_list = []

    def test_unique_author(self):
        authors = self.tiny_data_source.authors('Pratchett')
        self.assertTrue(len(authors) == 1)
        self.assertTrue(authors[0] == Author('Pratchett', 'Terry'))

    def test_unique_book(self):
        books = self.tiny_data_source.books('Blackout')
        self.assertTrue(len(books) == 1)
        self.assertTrue(books[0] == Book('Blackout'))

    def test_unique_book_numbers(self):
        books = self.tiny_data_source.books('1Q84')
        self.assertTrue(len(books) == 1)
        self.assertTrue(books[0] == Book('1Q84'))

    def test_unique_book_repeat_title(self):
        books = self.tiny_data_source.books('and')
        self.assertTrue(len(books) == 4)
        self.assertTrue(books[0] == Book('And Then There Were None'))
        self.assertTrue(books[1] == Book('Boys and Sex'))
        self.assertTrue(books[2] == Book('Girls and Sex'))
        self.assertTrue(books[3] == Book('The Life and Opinions of Tristram Shandy, Gentleman'))

    def test_all_books(self):
        books = self.tiny_data_source.books()
        self.assertTrue(len(books) == 11)
        self.assertTrue(books[0].title == '1Q84')
        self.assertTrue(books[1].title == 'And Then There Were None')
        self.assertTrue(books[2].title == 'Blackout')
        self.assertTrue(books[3].title == 'Boys and Sex')
        self.assertTrue(books[4].title == 'Emma')
        self.assertTrue(books[5].title == 'Girls and Sex')
        self.assertTrue(books[6].title == 'Good Omens')
        self.assertTrue(books[7].title == 'Neverwhere')
        self.assertTrue(books[8].title == 'Omoo')
        self.assertTrue(books[9].title == 'The Life and Opinions of Tristram Shandy, Gentleman')
        self.assertTrue(books[10].title == 'Thief of Time')

    def test_all_authors(self):
        authors = self.tiny_data_source.authors()
        self.assertTrue(len(authors) == 9)
        self.assertTrue(authors[0] == Author('Austen', 'Jane'))
        self.assertTrue(authors[1] == Author('Christie', 'Agatha'))
        self.assertTrue(authors[2] == Author('Gaiman', 'Neil'))
        self.assertTrue(authors[3] == Author('Melville', 'Herman'))
        self.assertTrue(authors[4] == Author('Murakami', 'Haruki'))
        self.assertTrue(authors[5] == Author('Orenstein', 'Peggy'))
        self.assertTrue(authors[6] == Author('Pratchett', 'Terry'))
        self.assertTrue(authors[7] == Author('Sterne', 'Laurence'))
        self.assertTrue(authors[8] == Author('Willis', 'Connie'))

    def test_all_books_year(self):
        books = self.tiny_data_source.books(sort_by = 'year')
        self.assertTrue(len(books) == 11)
        self.assertTrue(books[0].title == 'The Life and Opinions of Tristram Shandy, Gentleman')
        self.assertTrue(books[1].title == 'Emma')
        self.assertTrue(books[2].title == 'Omoo')
        self.assertTrue(books[3].title == 'And Then There Were None')
        self.assertTrue(books[4].title == 'Good Omens')
        self.assertTrue(books[5].title == 'Neverwhere')
        self.assertTrue(books[6].title == 'Thief of Time')
        self.assertTrue(books[7].title == '1Q84')
        self.assertTrue(books[8].title == 'Blackout')
        self.assertTrue(books[9].title == 'Girls and Sex')
        self.assertTrue(books[10].title == 'Boys and Sex')

    def test_between_two_years(self):
        books_between_years = self.tiny_data_source.books_between_years(start_year = '1814', end_year = '1939')
        self.assertTrue(len(books_between_years) == 3)
        self.assertTrue(books_between_years[0].title == 'Emma')
        self.assertTrue(books_between_years[1].title == 'Omoo')
        self.assertTrue(books_between_years[2].title == 'And Then There Were None')

    def test_start_year_only(self):
        books_between_years = self.tiny_data_source.books_between_years(start_year = '2016', end_year = 'none')
        self.assertTrue(len(books_between_years) == 2)
        self.assertTrue(books_between_years[0].title == 'Girls and Sex')
        self.assertTrue(books_between_years[1].title == 'Boys and Sex')

    def test_end_year_only(self):
        books_between_years = self.tiny_data_source.books_between_years(start_year = 'none', end_year = '1847')
        self.assertTrue(len(books_between_years) == 3)
        self.assertTrue(books_between_years[0].title == 'The Life and Opinions of Tristram Shandy, Gentleman')
        self.assertTrue(books_between_years[1].title == 'Emma')
        self.assertTrue(books_between_years[2].title == 'Omoo')


    def test_no_end_or_start_year(self):
        books_between_years = self.tiny_data_source.books_between_years(start_year = 'none', end_year = 'none')
        self.assertTrue(len(books_between_years) == 11)
        self.assertTrue(books_between_years[0].title == 'The Life and Opinions of Tristram Shandy, Gentleman')
        self.assertTrue(books_between_years[1].title == 'Emma')
        self.assertTrue(books_between_years[2].title == 'Omoo')
        self.assertTrue(books_between_years[3].title == 'And Then There Were None')
        self.assertTrue(books_between_years[4].title == 'Good Omens')
        self.assertTrue(books_between_years[5].title == 'Neverwhere')
        self.assertTrue(books_between_years[6].title == 'Thief of Time')
        self.assertTrue(books_between_years[7].title == '1Q84')
        self.assertTrue(books_between_years[8].title == 'Blackout')
        self.assertTrue(books_between_years[9].title == 'Girls and Sex')
        self.assertTrue(books_between_years[10].title == 'Boys and Sex')

    def test_negative_years(self):
        books_between_years = self.tiny_data_source.books_between_years(start_year = '-1900', end_year = '-90')
        self.assertTrue(len(books_between_years) == 0)
    
    def test_multiple_authors(self):
        books = self.tiny_data_source.books(search_text = 'Good')
        self.assertTrue(len(books) == 1)
        self.assertTrue(books[0].authors == 'Neil Gaiman (1960-) and Terry Pratchett (1948-2015)')
    
        
        
if __name__ == '__main__':
    unittest.main()

