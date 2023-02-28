# WAP to read dictonary from the keyboard and return it's sum

d = eval(input("Enter Dictionary : "))

s = 0

for value in d.values():
    s += value

print("The Sum of Values is : ", s)