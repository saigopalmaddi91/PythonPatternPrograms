# WAP to print inverted right angle triangle pattern

rows = eval(input("Enter number of rows"))

for i in range(rows-1, -1, -1):
    print((i+1) * '* ')

'''
Enter number of rows5
* * * * * 
* * * * 
* * * 
* * 
* 
'''