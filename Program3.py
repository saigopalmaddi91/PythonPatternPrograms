# WAP to print square pattern with provided fixed digit in every row

rows = eval(input("Enter number of rows:"))

for i in range(1, rows+1):
    print((str(i) + ' ') * rows)

''' Sample Output
Enter number of rows:5
1 1 1 1 1 
2 2 2 2 2 
3 3 3 3 3 
4 4 4 4 4 
5 5 5 5 5 '''