from things import readfile1


def part1():
    a = readfile1('6.txt')
    b = dict.fromkeys([x.split(')')[1].strip() for x in a] + ['COM'], 0)
    a = [x.strip().split(')') for x in a]
    indyk = ['COM']
    while indyk:
        kurak = []
        for x, y in a:
            if x in indyk:
                kurak.append(y)
                b[y] = 1 + b[x]
        indyk = kurak

    print(sum(b.values()))


def part2():
    a = readfile1('6.txt')
    a = [x.strip().split(')') for x in a]
    indyk = ['YOU']
    i = 0
    while 'SAN' not in indyk:
        indyk = [x for x, y in a if y in indyk] + [y for x, y in a if x in indyk]
        i += 1
    print(i - 2)


part2()
