class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(f"Hello {self.name}, Your marks are {self.marks}")

    def grade(self):
        if self.marks >= 80:
            print("You got first grade")
        elif self.marks >= 70:
            print("You got second grade")
        else:
            print("You got failed grade")


name = input("Enter your name : ")
marks = eval(input("Enter Marks : "))
s = Student(name, marks)
s.display()
s.grade()
