# WAP for following requirement  Input : aaaabbbcc and Output : 4a3b2c

s = input("Enter Input String : ")
output = ''
count, index = 1, 1
prev = s[0]

while index<len(s):
    if s[index] == prev:
        count+=1
    else:
        output += str(count) + prev
        prev = s[index]
        count = 1

    if index == len(s) - 1 :
        output += str(count) + prev

    index+=1

print("The final output is  ", output)

'''
Enter Input String : aaaaaabbbbbbccccc
The final output is   6a6b5c
'''