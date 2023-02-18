# WAP to find the occurrences of each vowel present in the given string

s = input("Enter Input String : ").lower()

d = {}

for char in s:
    if char in ['a', 'e', 'i', 'o', 'u']:
        d[char] = d.get(char,0) + 1

for key, value in d.items():
    print(f"{key} is present {value} times")

'''
Enter Input String : aedfsgcaknejfnqfonjsamcslkmqwo
a is present 3 times
e is present 2 times
o is present 2 times
'''