#define a book class that uses specific magic methods

class Book:
    
    def __init__(self, title: str, author: str, year: int):
        self.title = title #title of the book
        self.author = author #author of the book
        self.year = year #year of publication of the book

    def __del__(self):
        print (f"Deleting {self.title}")    
    
    def __str__(self):

        return f"{self.title} by {self.author}, published in {self.year}" 
    
    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.year})"
        
    