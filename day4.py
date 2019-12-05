#136818-685979
in1 = 136818
in2 = 685979


def nodecrease(a):
    while a > 9:
        if a % 10 < int(a / 10) % 10:
            return False
        a = int(a / 10)
    return True


def hasdoub(a):
    while a > 9:
        if a % 10 == int(a / 10) % 10:
            return True
        a = int(a / 10)
    return False


def hasdoub2(a):
    a = str(a)
    b = dict.fromkeys(a, 0)
    for c in a:
        b[c] += 1
    if 2 in b.values():
        return True
    return False


'''q = 0
for i in range(in1, in2 + 1):
    if hasdoub(i) and nodecrease(i):
        q += 1

print(q)'''

q = 0
for i in range(in1, in2 + 1):
    if nodecrease(i) and hasdoub2(i):
        q += 1

print(q)
