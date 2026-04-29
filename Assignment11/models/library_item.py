from abc import ABC, abstractmethod

class LibraryItem(ABC):
    item_count = 0

    def __init__(self, title, year):
        self.title = title
        self.year = year
        LibraryItem.item_count += 1

    @abstractmethod
    def displayInfo(self):
        pass