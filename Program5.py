#WAP to print right angle traiangle pattern with * symbol

rows = eval(input("Enter number of rows"))

for i in range(rows):
    print((i+1) * '* ')


'''
Enter number of rows5
* 
* * 
* * * 
* * * * 
* * * * * 
'''