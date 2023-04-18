import random


def decorator1(function):
    def inner1():
        x = function()
        return x * x

    return inner1


def decorator2(function):
    def inner2():
        x = function()
        return 2*x
    return inner2

@decorator2
@decorator1
def num():
    return random.randint(1, 11)


print(num())
