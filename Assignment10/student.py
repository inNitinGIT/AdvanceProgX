from address import Address

class Student:
    def __init__(self, name, age, address):
        self.name = name
        self._age = None
        self.age = age
        self.address = address   # Composition
        self.courses = []

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if not isinstance(value, int) or value <= 0 or value > 120:
            raise ValueError("Age must be between 1 and 120")
        self._age = value

    def add_course(self, course):
        self.courses.append(course)

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Address: {self.address.display()}")
        print(f"Courses: {', '.join(self.courses) if self.courses else 'None'}")