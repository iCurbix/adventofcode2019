inpt = '1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,6,19,1,19,6,23,2,23,6,27,2,6,27,31,2,13,31,35,1,9,35,39,2,10,39,43,1,6,43,47,1,13,47,51,2,6,51,55,2,55,6,59,1,59,5,63,2,9,63,67,1,5,67,71,2,10,71,75,1,6,75,79,1,79,5,83,2,83,10,87,1,9,87,91,1,5,91,95,1,95,6,99,2,10,99,103,1,5,103,107,1,107,6,111,1,5,111,115,2,115,6,119,1,119,6,123,1,123,10,127,1,127,13,131,1,131,2,135,1,135,5,0,99,2,14,0,0'
inpt = [int(x) for x in inpt.split(',')]


def part1(a, c, d):
    a[1] = c
    a[2] = d
    for i in range(0, len(a), 4):
        if a[i] == 1:
            a[a[i + 3]] = a[a[i + 1]] + a[a[i + 2]]
        elif a[i] == 2:
            a[a[i + 3]] = a[a[i + 1]] * a[a[i + 2]]
        elif a[i] == 99:
            return a[0]


#print(part1(inpt[:],12,2))

def part2():
    #brute!!!!! >:D
    for i in range(100):
        for j in range(100):
            try:
                if part1(inpt[:], i, j) == 19690720:
                    return 100 * i + j
            except IndexError:
                break



print(part2())
