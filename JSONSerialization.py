import json

employee = {"ename": "Saigopal", "esal" : 100000, "enum" : 23456, "edept" : "IT", "isMarried" : False}

json_string = json.dumps(employee, indent=4, sort_keys=True)
print(json_string)

with open('emp.json', 'w') as f:
    json.dump(employee, f, indent=4, sort_keys=True)

# De-serialization

employee_dict = json.loads(json_string)
print(type(employee_dict))
# print(employee_string)

for key, value in employee_dict.items():
    print(key, ':', value)


with open("emp.json", 'r') as f:
    employee_dictionary = json.load(f)

# for key, value in employee_dictionary.items():
#     print(key, ':', value)




