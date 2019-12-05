from things import calcfuel, readfile1

inpt = readfile1('1.txt')
sm = 0
for a in inpt:
    sm += calcfuel(float(a[:-1]))

print(sm)


def z2(fuel):
    a = calcfuel(fuel)
    return 0 if a <= 0 else a + z2(a)


sm = 0
for a in inpt:
    sm += z2(float(a[:-1]))

print(sm)
