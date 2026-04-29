
from .library_item import LibraryItem

class Book(LibraryItem):
    def __init__(self, title, year, author):
        super().__init__(title, year)
        self.author = author

    def displayInfo(self):
        print(f"[BOOK] {self.title} ({self.year}) - Author: {self.author}")