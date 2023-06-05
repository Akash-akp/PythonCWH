class Library:
    def __init__(self):
        self.noBooks = 0
        self.Books = []

    def addBooks(self,Name):
        self.Books.append(Name)
        self.noBooks += 1

    def info(self):
        print(f"This library has {self.noBooks} Books. The Books are")
        ibook = 1
        for book in self.Books:
            print(ibook,book)
            ibook+=1


a = Library()
a.addBooks("C")
a.addBooks("Java")
a.addBooks("Python")
a.addBooks("JS")
a.info()

