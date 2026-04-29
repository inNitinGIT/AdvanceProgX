from models.book import Book
from models.dvd import DVD
from models.library_item import LibraryItem

def main():
    items = [
        Book("Python Basics", 2020, "John Doe"),
        DVD("Inception", 2010, 148, "Sci-Fi"),
        Book("Data Structures", 2022, "Jane Smith"),
    ]

    for item in items:
        item.displayInfo()

    print("\nTotal items:", LibraryItem.item_count)

if __name__ == "__main__":
    main()