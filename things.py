def calcfuel(a):
    return int(a / 3) - 2


def readfile1(file):
    with open(file) as f:
        return f.readlines()
