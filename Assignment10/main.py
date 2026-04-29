from address import Address
from student import Student
from scholarship_student import ScholarshipStudent

def main():
    addr = Address("MG Road", "Delhi", "110001")

    s1 = Student("Rahul", 20, addr)
    s1.add_course("Math")
    s1.add_course("Physics")

    print("----- Student -----")
    s1.display()

    print("\n----- Scholarship Student -----")
    s2 = ScholarshipStudent("Anita", 22, addr, 50000)
    s2.add_course("Biology")
    s2.add_course("Chemistry")
    s2.display()


if __name__ == "__main__":
    main()