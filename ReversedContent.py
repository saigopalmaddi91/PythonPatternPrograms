# WAP to reverse the content of each word internally in a given python string

s = input("Enter Input String : ")

l = s.split()
l1 = []

for i in l:
    l1.append(i[::-1])

#print(l1)

print("Reversed words String is : ", ' '.join(l1))

'''
Enter Input String : I am Learning Python
Reversed words String is :  I ma gninraeL nohtyP
'''

# print(l)
# r = ''
# for i in l:
#     r += i[::-1]
#     r += " "
#
# print(r)