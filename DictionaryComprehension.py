l = [x for x in range(20) if x%2==0]
print("List Comprehension : ", l)

s = {x**2 for x in range(20)}
print("Set Comprehension : ",s)

d = {x:x**2 for x in range(20)}
print("Dictionary Comprehension : ",d)

