class Book:
    total_books = 0
    def __init__(self,name):
        self.name = name
        Book.total_books += 1
    
    
    @classmethod
    def increment_book_count(cls):
        print(f"Total books: {cls.total_books}")
        
book1 = Book("Book 1")
book2 = Book("Book 2")
book3 = Book("Book 3")
Book.increment_book_count()         