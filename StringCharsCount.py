# WAP for following requirement Input : a4b3c2 and Output : aaaabbbcc

s = input("Enter Alphanumeric String : ")
s1 = ''
i = 0
for char in s:
    if char.isdigit():
        s1 += s[i-1] * int(char)
    i+=1

print("The Final Output String is : ", s1)

'''
Enter Alphanumeric String : A4V3Z7Y5
The Final Output String is :  AAAAVVVZZZZZZZYYYYY
'''