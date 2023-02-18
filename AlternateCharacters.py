# WAP to merge characters of 2 input strings into a single string by taking characters alternatively

s1 = input("Enter First String : ")
s2 = input("Enter Second String : ")

s = ''
i, j =0, 0

while i < len(s1) or j < len(s2):
    s += s1[i] + s2[j]
    i+=1
    j+=1
    if(i >= len(s1)):
        s+=s2[j:len(s2)]
        break
    elif(j >=len(s2)):
        s+=s1[i:len(s1)]
        break

print(s)

'''
Enter First String : Saigopal
Enter Second String : Maddi
SMaaidgdoipal

'''