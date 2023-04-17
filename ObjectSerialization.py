import pickle


class Employee:
    def __init__(self, ename, esal, enum, edept):
        self.ename = ename
        self.esal = esal
        self.enum = enum
        self.edept = edept

    def display(self):
        print(
            f" Employee Name : {self.ename} \n Employee Salary : {self.esal} \n Employee Number : {self.enum} \n"
            f" Employee Dept. : {self.edept}")


employee = Employee("Saigopal", 100000, 12345, "IT")

with open("emp.ser", 'wb') as f:
    pickle.dump(employee, f)
print("employee object serialized successfully!!!")

# Deserialization

with open("emp.ser", 'rb') as f:
    deserialized_object = pickle.load(f)

print("employee object de-serialized successfully and printing it's details using display() method !!!")
deserialized_object.display()

