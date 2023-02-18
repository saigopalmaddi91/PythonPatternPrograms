# WAP to print as Input: a4k3b2 and Output: aeknbd

s = input("Enter Input String : ")

index = 0
s1 = ''
for char in s:
    if char.isdigit():
        s1 += chr(ord(s[index-1]) + int(char))
    else:
        s1 += char
    index +=1

print("The Final Output String is : ", s1)

'''
Enter Input String : a4k3b2
The Final Output String is :  aeknbd

'''