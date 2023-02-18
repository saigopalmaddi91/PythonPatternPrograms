# WAP to print following input:ABAABBCA output:4A3B1C

s = input("Enter Input String : ")

d = {}
s1 = ''

for char in s:
    d[char] = d.get(char,0) + 1

for key, value in d.items():
    print(value,key, sep='', end='')

'''
Enter Input String : ABABABABSBSBDBDBFBBDBS
4A11B3S3D1F
'''