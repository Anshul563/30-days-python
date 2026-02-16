# 1. The Blueprint
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def read(self):
        return f"You are reading '{self.title}' by {self.author}."

# 2. Creating the Objects (Instantiation)
# We assign the new objects to variables so we can use them later
book1 = Book("1984", "George Orwell")
book2 = Book("The Hobbit", "J.R.R. Tolkien")