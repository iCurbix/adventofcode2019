from readfile import readfile

inpt = readfile('1.txt')
sm = 0
for a in inpt:
    sm += int(float(a[:-1])/3)-2

print(sm)
