def decorator1(function):
    def inner1():
        print("Decorator 1 execution!!!")
        function()

    return inner1


def decorator2(function):
    def inner2():
        print("Decorator 2 execution!!!")
        function()

    return inner2


def decorator3(function):
    def inner3():
        print("Decorator 3 Execution!!!")
        function()

    return inner3


@decorator3
@decorator2
@decorator1
def function():
    print("Actual function!!!")


function()
