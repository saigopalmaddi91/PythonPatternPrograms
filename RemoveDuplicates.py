# WAP to remove duplicate characters of the given string

s = input("Enter Input String : ")

s1 = ''

for char in s:
    if char not in s1:
        s1 += char
    else:
        continue

print("The Final String after removing duplicates is :  ", s1)

'''
Enter Input String : abababacbdbcbdbcbd
The Final String after removing duplicates is :   abcd
'''