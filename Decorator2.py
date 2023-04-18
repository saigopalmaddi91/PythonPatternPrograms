def add_decorator(function):
    def inner_dec(x, y):
        print("#" * 30)
        print("The Sum : ", end='')
        function(x, y)
        print("#" * 30)

    return inner_dec


@add_decorator
def add(a, b):
    print(a + b)


add(10, 20)
