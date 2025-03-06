# module matematika 

def tambah(*args):
    total = 0
    for arg in args:
        total += arg
    return total

def kali(*args):
    total = 1
    for arg in args:
        total *= arg
    return total

def pangkat(n: int):
    return lambda x: x ** n