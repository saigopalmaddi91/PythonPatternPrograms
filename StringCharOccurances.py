# WAP to find the number of occurances of each character present in the given string

s = input("Enter Input String : ")

s1 = ''

for char in s:
    if char not in s1:
        s1 += char
        print("{} is present in the given string {} times".format(char, s.count(char)))

'''
Enter Input String : ababababcbcbcbcbdbdbdbdbdbdb
a is present in the given string 4 times
b is present in the given string 14 times
c is present in the given string 4 times
d is present in the given string 6 times

'''