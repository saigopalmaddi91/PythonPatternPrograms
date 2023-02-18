#  WAP to find number of occurances of each character present in the given string without using count() method

s = input("Enter Input String : ")

d = {}

for char in s:
    d[char] = d.get(char,0) + 1

for key, value in d.items():
    print(f"{key} is present in the given string {value} times ")

'''
Enter Input String : abababababcbcbcbcbdbdbdbfbfbfbgbgbg
a is present in the given string 5 times
b is present in the given string 17 times
c is present in the given string 4 times
d is present in the given string 3 times
f is present in the given string 3 times
g is present in the given string 3 times
'''