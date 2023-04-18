def decorator(function: object) -> object:
    print("This is the decorator function!!!")
    def inner():
        print("This is the inner function of a decorator function!!!")

    return inner

@decorator
def display():
    print("This is the display function!!!")

display()