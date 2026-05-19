from .library_item import LibraryItem

class DVD(LibraryItem):
    def __init__(self, title, year, duration, genre):
        super().__init__(title, year)
        self.duration = duration
        self.genre = genre

    def displayInfo(self):
        print(f"[DVD] {self.title} ({self.year}) - {self.genre}, {self.duration} mins")