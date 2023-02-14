# WAP to print diamond pattern

rows = eval(input("Enter number of rows : "))

for i in range(rows):
    print(' ' * (rows - i - 1), end='')
    print((i + 1) * '* ')

for i in range(rows-1):
    print((i+1) * ' ', end = '')
    print((rows-i-1) * '* ')


'''
Enter number of rows : 5
    * 
   * * 
  * * * 
 * * * * 
* * * * * 
 * * * * 
  * * * 
   * * 
    * 
'''