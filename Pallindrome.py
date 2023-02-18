# WAP to find whether given strings are palindrome

s = input("Enter given string : ")

if s == s[::-1]:
    print("given strings are palindrome")

else:
    print("given strings are not palindrome")

'''
Enter given string : level
given strings are palindrome
'''