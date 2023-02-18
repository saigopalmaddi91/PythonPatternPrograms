# WAP to reverse string content without using inbuilt functions

s = input("Enter input string to be reversed: ")
r = ''
i = len(s) - 1
while i!=-1:
    r += s[i]
    i-=1

print('Reversed String is : ', r)

'''
Enter input string to be reversed: madam
Reversed String is :  madam
'''