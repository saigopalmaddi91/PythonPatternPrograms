# WAP to generate words from given input strings by taking characters alternatively

s1 = input("Enter first string : ")
s2 = input("Enter second string : ")
s3 = input("Enter third string : ")

i=j=k=0

while i<len(s1) or j<len(s2) or k<len(s3):
    output = ''
    if i<len(s1):
        output += s1[i]
        i +=1
    if j<len(s2):
        output += s2[j]
        j +=1
    if k<len(s3):
        output +=s3[k]
        k +=1
    print(output)


'''
Enter first string : abcdefg
Enter second string : xyz
Enter third string : 12345
ax1
by2
cz3
d4
e5
f
g
'''




