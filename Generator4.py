def fibonacci_generator(n):
    a,b = 0,1
    i = 1
    while i <= n:
        yield a
        a,b = b, a+b


g = fibonacci_generator(10)

for i in range(10):
    print(next(g))