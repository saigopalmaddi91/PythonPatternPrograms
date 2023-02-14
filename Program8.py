# WAP to print inverted pyramid pattern

rows = eval(input("Enter number of rows : "))

for i in range(rows):
    print((i) * ' ', end = '')
    print((rows-i) * '* ')


'''
Enter number of rows : 5
* * * * * 
 * * * * 
  * * * 
   * * 
    * 
'''