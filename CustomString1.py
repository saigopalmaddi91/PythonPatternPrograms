# WAP to print following input:ABAABBCA output:A4B3C1

s = input("Enter Input String : ")

d = {}
s1 = ''

for char in s:
    d[char] = d.get(char,0) + 1

for key, value in d.items():
    print(key,value, sep='', end='')

'''
Enter Input String : ABABABABSBSBDBDBFBBDBS
A4B11S3D3F1
'''