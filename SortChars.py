# WAP to sort characters of the string, first alphabets and followed by digits

s = input("Enter Input String : ")

alphabets = []
digits = []

for char in s:
    if char.isalpha():
        alphabets.append(char)
    else:
        digits.append(char)

print("Sorted Order is : ",  ''.join(sorted(alphabets) + sorted(digits)))

'''
Enter Input String : Saigopal060895Maddi
Sorted Order is :  MSaaaddgiilop005689
'''