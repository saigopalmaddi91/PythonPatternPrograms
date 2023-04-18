def my_generator():
    yield 'A'
    yield 'B'
    yield 'C'


g = my_generator()

# print(next(g))
# print(next(g))
# print(next(g))

for value in g:
    print(value)
