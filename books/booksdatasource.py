#!/usr/bin/env python3
'''
    booksdatasource.py
    Jeff Ondich, 21 September 2022

    For use in the "books" assignment at the beginning of Carleton's
    CS 257 Software Design class, Fall 2022.

    Revised by Muno Siyakurima and Kyle Machalec
'''

import csv
from operator import attrgetter
from turtle import title


class Author:
    def __init__(self, surname='', given_name='', birth_year=None, death_year=None):
        self.surname = surname
        self.given_name = given_name
        self.birth_year = birth_year
        self.death_year = death_year

    def __eq__(self, other):
        ''' For simplicity, we're going to assume that no two authors have the same name. '''
        return self.surname == other.surname and self.given_name == other.given_name
    
    def __lt__(self, other):
        '''Sorts by surname otherwise if they are the same it compares their given name and sorts them alphabetically.'''
        if self.surname < other.surname:
            return True
        if self.surname == other.surname and self.given_name < other.given_name:
            return True
        return False
    
    def __hash__(self):
        '''Used to check if surname and given name already exist in the set'''
        return hash(self.surname + self.given_name)

class Book:
    def __init__(self, title='', publication_year=None, authors=[]):
        ''' Note that the self.authors instance variable is a list of
            references to Author objects. '''
        self.title = title
        self.publication_year = publication_year
        self.authors = authors

    def __eq__(self, other):
        ''' We're going to make the excessively simplifying assumption that
            no two books have the same title, so "same title" is the same
            thing as "same book". '''
        return self.title == other.title
    
    def __lt__(self, other):
        '''Sorts the book titles alphabetically'''
        return self.title < other.title

class BooksDataSource:
    
    authors_list = {}
    authors_list = set()
    books_list = []

    def __init__(self, books_csv_file_name):
        ''' The books CSV file format looks like this:

                title,publication_yea(r,author_description

            For example:

                All Clear,2010,Connie Willis (1945-)
                "Right Ho, Jeeves",1934,Pelham Grenville Wodehouse (1881-1975)

            This __init__ method parses the specified CSV file and creates
            suitable instance variables for the BooksDataSource object containing
            a collection of Author objects and a collection of Book objects.
        '''

        with open(books_csv_file_name) as f:
            reader = csv.reader(f)
            for row in reader:
                book = Book(row[0], row[1], row[2]) #Makes the Book object with row[0] = title, row[1] = publication_year and row[2] = authors
                BooksDataSource.books_list.append(book)
                split_authors = row[2].split(' and ') # splits string of potentially multiple authors into individual authors
                for a in split_authors:
                    split_name = a.split()
                    if len(split_name) == 3: #If author has one surname
                        split_dates = split_name[2].split('-')
                        author = Author(split_name[1], split_name[0], split_dates[0][-4:], split_dates[1][:4])
                        BooksDataSource.authors_list.add(author)
                    elif len(split_name) == 4: #If author has two surnames
                        split_dates = split_name[3].split('-')
                        author = Author(split_name[1] + " " + split_name[2], split_name[0], split_dates[0][-4:], split_dates[1][:4])
                        BooksDataSource.authors_list.add(author)

    
    def authors(self, search_text=None):
        ''' Returns a list of all the Author objects in this data source whose names contain
            (case-insensitively) the search text. If search_text is None, then this method
            returns all of the Author objects. In either case, the returned list is sorted
            by surname, breaking ties using given name (e.g. Ann Brontë comes before Charlotte Brontë).
        '''
        
        authors_returned = []
        if search_text == None:
            authors_returned = BooksDataSource.authors_list
        else:
            for author in BooksDataSource.authors_list:
                if search_text.lower() in author.given_name.lower() or search_text.lower() in author.surname.lower():
                    authors_returned.append(author)

        return sorted(authors_returned)
        

    def books(self, search_text=None, sort_by='title'):
        ''' Returns a list of all the Book objects in this data source whose
            titles contain (case-insensitively) search_text. If search_text is None,
            then this method returns all of the books objects.

            The list of books is sorted in an order depending on the sort_by parameter:

                'year' -- sorts by publication_year, breaking ties with (case-insenstive) title
                'title' -- sorts by (case-insensitive) title, breaking ties with publication_year
                default -- same as 'title' (that is, if sort_by is anything other than 'year'
                            or 'title', just do the same thing you would do for 'title')
        '''
        books_returned = []
        if search_text == None:
            books_returned = BooksDataSource.books_list
        else:
            for book in BooksDataSource.books_list:
                if search_text.lower() in book.title.lower():
                    books_returned.append(book)
        
        if sort_by == 'year':
            books_returned = sorted(books_returned, key = attrgetter('publication_year', 'title')) #Sorts by publication year and if there are ties, sorts by title
        else:
            books_returned = sorted(books_returned, key = attrgetter('title', 'publication_year'))  #Sorts by title and if there are ties, sorts by publication year

        return books_returned



    def books_between_years(self, start_year=None, end_year=None):
        ''' Returns a list of all the Book objects in this data source whose publication
            years are between start_year and end_year, inclusive. The list is sorted
            by publication year, breaking ties by title (e.g. Neverwhere 1996 should
            come before Thief of Time 1996).

            If start_year is None, then any book published before or during end_year
            should be included. If end_year is None, then any book published after or
            during start_year should be included. If both are None, then all books
            should be included.
        '''
        publication_books = []

        if start_year == 'none' and end_year == 'none':
            publication_books = BooksDataSource.books_list
        elif start_year == 'none':
            for book in BooksDataSource.books_list:
                if book.publication_year <= end_year:
                    publication_books.append(book)
        elif end_year == 'none':
            for book in BooksDataSource.books_list:
                if book.publication_year >= start_year:
                    publication_books.append(book)
        else:
            for book in BooksDataSource.books_list:
                if book.publication_year <= end_year and book.publication_year >= start_year:
                    publication_books.append(book)
            
        return sorted(publication_books, key = attrgetter('publication_year', 'title')) #Sorts by publication year and if there are ties, sorts by title