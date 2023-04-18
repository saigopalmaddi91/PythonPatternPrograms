def smart_division(function):
    def inner(x, y):
        if y == 0:
            print("The divisor cannot be zero, value undefined!!!")
        else:
            print("The Value is : ", end='')
            function(x, y)

    return inner


@smart_division
def division(a, b):
    print(a / b)


division(10, 0)
division(10, 20)
