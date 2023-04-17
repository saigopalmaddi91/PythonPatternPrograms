import json


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
# employee_dict = {"ename" : employee.ename, "esal" : employee.esal,
#                  "enum" : employee.enum, "edept" : employee.edept}

employee_dict = employee.__dict__

# Serializing to JSON String
employee_string = json.dumps(employee_dict, indent=4)
print("Object Serialized to JSON String!!!")

# Serializing to JSON File

with open('employee.json', 'w') as f:
    json.dump(employee_dict, f, indent=4)
    print("Object Serialized to JSON File!!! ")

# De-Serializing from JSON String

employee_dictionary = json.loads(employee_string)
print("Object De-Serialized from JSON String!!! ")

# De-Serializing from JSON File

with open("employee.json", 'r') as f:
    emp_dict = json.load(f)

print("Object De-Serialized from JSON File!!! ")
print('*' * 30)

print("Printing info from de-serialized Json String")
emp1 = Employee(employee_dictionary['ename'], employee_dictionary['esal'], employee_dictionary['enum'], employee_dictionary['edept'])
emp1.display()
print("Printing info from de-serialized Json File")
emp = Employee(emp_dict['ename'], emp_dict['esal'], emp_dict['enum'], emp_dict['edept'])
emp.display()
