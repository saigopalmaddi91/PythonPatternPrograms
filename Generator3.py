import time


def countdown_generator(n):
    while n >= 1:
        yield n
        n -= 1


max_value = eval(input("Enter max timer for countdown : "))

g = countdown_generator(max_value)

for value in g:
    print(value)
    time.sleep(1)
