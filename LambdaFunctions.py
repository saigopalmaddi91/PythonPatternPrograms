# Syntax -- lambda input_args:Expression
from functools import reduce

square = lambda n: n * n

n = eval(input("Enter a number : "))
print(f"The Square of {n} is", square(n))

bigger = lambda a, b, c: a if a > b and a > c else b if b > c else c

print(bigger(10, 20, 30))

# Filter filter(function, sequence) python inbuilt

l = [x for x in range(11)]


def isEven(n):
    if n % 2 == 0:
        return True
    return False


l1 = list(filter(isEven, l))

print(l1)

even = list(filter(lambda n: n%2==0, l))
print(even)

odd = list(filter(lambda n:n%2!=0, l))
print(odd)

# Numbers divisible by 3 and Odd

l3 = list(filter(lambda n: n%3==0 and n%2!=0, l))

print(l3)

# Map map(function, sequence) python inbuilt

l4 = list(map(lambda n: n**2, l))
print(l4)


l5 = list(map(lambda x,y: x*y, l, l))
print(l5)

l6 = list(map(lambda x,y,z: x+y+z, l,l,l))
print(l6)

# Reduce Function reduce(function, sequence)

result = reduce(lambda x,y:x+y, l)
print(result)

result = reduce(lambda x,y:x*y, odd)
print(result)

result = reduce(lambda x,y:x+y, range(101))
print(result)