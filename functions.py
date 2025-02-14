# *args - allows you to pass multiple non-key arguments
# **kwargs - allows you to pass multiple keyword arguments


def hello(greeting, title, first, last):
    print(f"{greeting} {title}{first} {last}")

def add(*args): # z * označimo množico argumentov
    total = 0
    for arg in args:
        total += arg
    return total


def display_name(*args):
    for arg in args:
        print(arg, end=" ")


def print_addres(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_addres(street="Nevlje", stevilka = 17, kraj="Kamnik")