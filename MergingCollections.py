l1 = [10,20,30]
l2 = [40,50,60]

l = l1 + l2
print(l)

l3 = [*l1, *l2]# * represents variable length arguments which here refers to consider all objects present in the list

print(l3)

# Tuple Merging

t1 = (10,20,30)
t2 = 40,50,60

t = t1 + t2

print(t)

t3 = (*t1, *t2)

print(t3)


# Set Merging

s1 = {10,20,30}
s2 = {40,50,60}

# + operator does not work in sets

s3 = {*s1, *s2}

print(s3)

s1.update(s2)
print(s1)

# Dict Merging

d1 = {100:'A', 200:'B', 300:'C'}
d2 = {400:'D', 500:'E', 600:'F', 100:'G'}

# + operator does not work in dict

d = {**d1, **d2} # ** denotes variable length keyword arguments

print(d)

