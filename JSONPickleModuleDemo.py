import jsonpickle


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


employee = Employee("SaigopalMaddi", 100000, 92345, "IT")

# Serializing the Object

json_string = jsonpickle.encode(employee)
print(json_string)

# Serialization to File

with open('emp1.json', 'w') as f:
    f.write(json_string)

# De-serializing from json string

emp = jsonpickle.decode(json_string)
emp.display()

# De-serializing from json file

with open("emp1.json", 'r') as f:
    json_string1 = f.readline()

emp1 = jsonpickle.decode(json_string1)
emp1.display()

