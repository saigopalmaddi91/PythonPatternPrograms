# WAP to reverse the content of every second word in a given input string

s = input("Enter Input String")

l = s.split()
l1 = []
index = 1
for i in l:
    if index % 2 == 0:
        l1.append(i[::-1])
    else:
        l1.append(i)
    index+=1

print("Reversed words String is : ", ' '.join(l1))

'''
Enter Input StringI am Learning Python
Reversed words String is :  I ma Learning nohtyP
'''