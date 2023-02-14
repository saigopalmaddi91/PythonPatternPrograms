# WAP  to print square pattern with alphabet symbols

rows = eval(input("Enter number of rows:"))

for i in range(rows):
    print((chr(i+ 65) + ' ') * rows)

''' Sample Output
Enter number of rows:6
A A A A A A 
B B B B B B 
C C C C C C 
D D D D D D 
E E E E E E 
F F F F F F 
'''