# WAP to print square of *'s with given input number of rows

rows = eval(input("Enter number of rows to be printed for the square"))

for i in range(rows):
    print(rows * '* ')

''' Sample Output
 Enter number of rows to be printed for the square6
* * * * * * 
* * * * * * 
* * * * * * 
* * * * * * 
* * * * * * 
* * * * * * 
'''