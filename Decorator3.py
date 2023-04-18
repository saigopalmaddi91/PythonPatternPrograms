def decorator(function):
    def inner(role):
        if role == 'admin':
            print('*' * 30)
            print(f"You have been given {role} level permissions!!!")
            print('*' * 30)

        else:
            function(role)

    return inner


@decorator
def permissions(role):
    print("You have been given normal user permissions!!!")


permissions('admin')
permissions('user')
