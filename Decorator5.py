def decorator(function):
    def inner(role):
        if role == 'admin':
            print('*' * 30)
            print(f"You have been given {role} level permissions!!!")
            print('*' * 30)

        else:
            function(role)

    return inner


def permissions(role):
    print("You have been given normal user permissions!!!")


decorated_permissions = decorator(permissions)
decorated_permissions('admin')
decorated_permissions('user')
