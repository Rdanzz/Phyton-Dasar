""" Module Math """

def tambah (*args):
    total = 0
    for item in args:
        total += item
    return total

def kali (*args):
    total = 1
    for item in args:
        total *= item
    return total

def pangkat(n):
    return lambda x: x ** n