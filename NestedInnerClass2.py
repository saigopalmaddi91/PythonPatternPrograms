class Person:
    def __init__(self, name, dd, mm, yyyy):
        print("Person Object Creation")
        self.name = name
        self.dob = self.DateOfBirth(dd, mm, yyyy)

    def info(self):
        print(f"Name : {self.name}")
        self.dob.display()

    class DateOfBirth:

        def __init__(self, dd, mm, yyyy):
            print("DOB Object Creation")
            self.dd = dd
            self.mm = mm
            self.yyyy = yyyy

        def display(self):
            print(f"Your DOB is {self.mm}/{self.dd}/{self.yyyy}")


person = Person("Saigopal", 6, 8, 1995)
person.info()
