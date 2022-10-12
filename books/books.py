'''
    books.py
    Created by Muno Siyakurima and Kyle Machalec

    For use in the "books" assignment at the beginning of Carleton's
    CS 257 Software Design class, Fall 2022.
'''

import sys
import booksdatasource

def usage_statement():
    statement = ' Usage:\n'
    statement += ' python3 books.py title [-t | -y] <search_string>\n'
    statement += ' python3 books.py author <search_string>\n'
    statement += ' python3 books.py years <start_date|none> <end_date|none>\n'
    statement += ' python3 books.py -h'
    return statement

def print_error():
    print("Invalid command line syntax, please check usage statement: python3 books.py -h")
    exit()

def parse_command_line():
    '''Takes in the command-line arguments entered by the user and assigns them to the appropriate
    variables. Also handles invalid input entered by the user.'''

    arguments = {}
    if len(sys.argv) < 2:
        print(usage_statement())
        exit()
    if sys.argv[1] == 'title': #If 'title' is the second argument then we expect the user to input the sorting method and the search string or just the search string
        arguments['method'] = sys.argv[1]
        if len(sys.argv) == 2:
            arguments['search_string'] = None
            arguments['[-t | -y]'] = '-t'
        elif len(sys.argv) == 3:
            if sys.argv[2] == '-t' or sys.argv[2] == '-y':
                arguments['[-t | -y]'] = sys.argv[2]
                arguments['search_string'] = None
            else:
                arguments['search_string'] = sys.argv[2]
                arguments['[-t | -y]'] = '-t'
        elif len(sys.argv) == 4:
            if sys.argv[2] == '-t' or sys.argv[2] == '-y':
                arguments['[-t | -y]'] = sys.argv[2]
                arguments['search_string'] = sys.argv[3]
            else:
                print_error()
        else:
            print_error()

    elif sys.argv[1] == 'author': #If 'author' is the second argument then we expect the user to just type in the search string
        arguments['method'] = sys.argv[1]
        if len (sys.argv) == 2:
            arguments['search_string'] = None
        elif len(sys.argv) == 3:
            arguments['search_string'] = sys.argv[2]
        else:
            print_error()

    elif sys.argv[1] == 'years': #If 'years' is the second argument then we expect the user to input the start year/none and the end year/none
        if len (sys.argv) < 4:
            print_error()
        elif len(sys.argv) == 4:
            arguments['method'] = sys.argv[1]
            if (sys.argv[2] == 'none') or sys.argv[2].isnumeric():
                arguments['start_date'] = sys.argv[2]
            else:
                print_error()
            if (sys.argv[3] == 'none') or sys.argv[3].isnumeric():
                arguments['end_date'] = sys.argv[3]
            else:
                print_error()  
        else:
            print_error()
    elif sys.argv[1] == '-h': #Prints the usage.txt file to the user
        f = open('usage.txt', 'r')
        content = f.read()
        print(content)
        exit()

    return arguments

def main(arguments):
    '''Reads the arguments from the command-line and uses the BooksDataSource methods to 
    print the necessary information needed by the user'''

    booksource = booksdatasource.BooksDataSource('books1.csv')
    method = arguments['method']
    if method == 'title':
        options = arguments['[-t | -y]']
        search = arguments['search_string']
        if options == '-t':
            title_books = booksource.books(search_text = search)
        else:
            title_books = booksource.books(search_text = search, sort_by = 'year')
        
        for book in title_books:
            print(book.title + ", " + book.publication_year)

    elif method == 'author':
        search = arguments['search_string']
        author_books = booksource.authors(search_text = search)
        for author in author_books:
            print()
            print(author.surname + ", " + author.given_name)
            for book in booksource.books():
                multiple_authors = book.authors.split(' and ') #If a book has multiple authors then separate the two
                for a in multiple_authors:
                    names = a.split()
                    if len(names) == 3: #Author has one surname and then print books assocaited with that author
                        if author.given_name == names[0] and author.surname == names[1]:
                            print (book.title)
                    else: #Author has two surnames and then print books assocaited with that author
                        if author.given_name == names[0] and author.surname == (names[1] + " " + names[2]):
                            print(book.title)
            
    elif method == 'years':
        start_date = arguments['start_date']
        end_date = arguments['end_date']
        year_books = booksource.books_between_years(start_year = start_date, end_year = end_date)
        for book in year_books:
            print(book.title + ", " + book.publication_year)
    
    


arguments = parse_command_line()

main(arguments)
    
