from abc import ABC, abstractmethod

# Storage interface

class Storage(ABC):

    @abstractmethod
    def save_order(self, order):
        pass


# Database storage

class DatabaseStorage(Storage):

    def save_order(self, order):

        print("[DATABASE] Order Saved")


# File storage

class FileStorage(Storage):

    def save_order(self, order):

        print("[FILE] Order Saved")