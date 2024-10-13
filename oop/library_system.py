class Book:
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author
        print(f'Book: {self.title} by {self.author}')

class EBook(Book):
    def __init__(self, title: str, author: str, file_size: int):
        super().__init__(title, author)
        self.file_size = file_size
        print (f'EBook: {self.title} by {self.author}, File Size: {file_size}')

class PrintBook (Book):  
    def __init__(self, title: str, author: str, page_count: int):
        super().__init__(title, author)
        self.page_count = page_count
        print (f'PrintBook: {self.title} by {self.author}, Page Count: {page_count}')

class Library:
    def __init__(self):
        self.books = []
    
    def add_book(self, book: Book):
        self.books.append(book)
        
    def list_books(self):
        for book in self.books:
            print(book)
        
    
        