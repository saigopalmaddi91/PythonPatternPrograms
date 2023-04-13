import csv

with open("emp.csv", 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['ENo', 'EName', 'ESal', 'EAddress'])
    while True:
        eno = int(input("Enter Employee Number : "))
        ename = input("Enter Employee Name : ")
        esal = eval(input("Enter Employee Salary : "))
        eaddress = input("Enter Employee Address : ")
        w.writerow([eno,ename,esal,eaddress])
        option = input("Do you want to insert one more record? yes or no : ")
        if option.lower() == 'no':
            break

    print("Data Successfully written to file")

with open("emp.csv", 'r') as f:
    r = csv.reader(f)
    data = list(r)
    print(data)
    for row in data:
        print(row)