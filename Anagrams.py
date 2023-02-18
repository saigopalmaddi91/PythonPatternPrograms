# WAP to check whether given two strings are anagrams or not

s1 = input("Enter first input string : ")
s2 = input("Enter second input string : ")

if sorted(s1) == sorted(s2):
    print("Given strings are anagrams")
else:
    print("Given strings are not anagrams")

'''
Enter first input string : triangle
Enter second input string : integral
Given strings are anagrams
'''