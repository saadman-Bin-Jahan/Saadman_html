class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def borrow(self):
        self.is_borrowed = True
        print(self.title, "has been borrowed.")

    def return_book(self):
        self.is_borrowed = False
        print(self.title, "has been returned.")

book1 = Book("Around The World in 80 Days", "Jules Verne")
book2 = Book("Treasure Island", "Robert Louis Stevenson")
book3 = Book("The Adventures of Tintin", "Herge")

book1.borrow()
book1.return_book()

book2.borrow()
book2.return_book()

book3.borrow()
book3.return_book()
