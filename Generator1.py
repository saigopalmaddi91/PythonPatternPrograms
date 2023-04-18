choice = eval(input("Enter n value"))


def n_values_generator(n):
    i = 1
    while i <= n:
        yield i
        i += 1


g = n_values_generator(choice)

for value in g:
    print(value)
