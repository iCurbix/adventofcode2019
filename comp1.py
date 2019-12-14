class Computer:
    def __init__(self, inpt):
        self.inpt = inpt
        self.outs = []
        self.running = True
        self.pointer = 0
        self.paramnum = {
            '01': 3,
            '02': 3,
            '03': 1,
            '04': 1,
            '05': 2,
            '06': 2,
            '07': 3,
            '08': 3,
            '99': 0,
        }
        self.instruction = {
            '01': self.code01,
            '02': self.code02,
            '03': self.code03,
            '04': self.code04,
            '05': self.code05,
            '06': self.code06,
            '07': self.code07,
            '08': self.code08,
            '99': self.code99,
        }
    
    def getinstruction(self, a):
        l = len(a)
        if l < 5:
            a = '0' * (5 - l) + a
        return a[-2:], a[2:3], a[1:2], a[0:1], self.paramnum[a[-2:]]
    
    def getval(self, pos, type):
        if type == '0':
            return self.inpt[int(self.inpt[pos])]
        if type == '1':
            return self.inpt[pos]
    
    def writeval(self, pos, val):
        self.inpt[int(self.inpt[pos])] = val
    
    def code01(self, type1, type2, type3):
        a = int(self.getval(self.pointer + 1, type1))
        b = int(self.getval(self.pointer + 2, type2))
        self.writeval(self.pointer + 3, str(a + b))
        return 0
    
    def code02(self, type1, type2, type3):
        a = int(self.getval(self.pointer + 1, type1))
        b = int(self.getval(self.pointer + 2, type2))
        self.writeval(self.pointer + 3, str(a * b))
        return 0
    
    def code03(self, type1, type2, type3):
        a = input()
        self.writeval(self.pointer + 1, a)
        return 0
    
    def code04(self, type1, type2, type3):
        self.outs.append(self.getval(self.pointer + 1, '0'))
        return 0
    
    def code05(self, t1, t2, t3):
        if self.getval(self.pointer + 1, t1) != '0':
            self.pointer = int(self.getval(self.pointer + 2, t2))
            return 1
        return 0
    
    def code06(self, t1, t2, t3):
        if self.getval(self.pointer + 1, t1) == '0':
            self.pointer = int(self.getval(self.pointer + 2, t2))
            return 1
        return 0
    
    def code07(self, t1, t2, t3):
        a = self.getval(self.pointer + 1, t1)
        b = self.getval(self.pointer + 2, t2)
        if a < b:
            self.writeval(self.pointer + 3, '1')
        else:
            self.writeval(self.pointer + 3, '0')
        return 0
    
    def code08(self, t1, t2, t3):
        a = self.getval(self.pointer + 1, t1)
        b = self.getval(self.pointer + 2, t2)
        if a == b:
            self.writeval(self.pointer + 3, '1')
        else:
            self.writeval(self.pointer + 3, '0')
        return 0
    
    def code99(self, type1, type2, type3):
        print(self.outs)
        self.running = False
        return 0
    
    def run(self):
        self.pointer = 0
        self.running = True
        while self.running:
            opcode, type1, type2, type3, pnum = self.getinstruction(self.inpt[self.pointer])
            if self.instruction[opcode](type1, type2, type3) == 0:
                self.pointer += pnum + 1


class Computerday7(Computer):
    def __init__(self, inpt):
        super().__init__(inpt)
        self.wherein = 0
        self.in1 = []

    def code03(self, type1, type2, type3):
        self.writeval(self.pointer + 1, self.in1[0])
        self.in1 = self.in1[1:]
        return 0

    def code99(self, type1, type2, type3):
        self.running = False
        return 0

    def run(self):
        while self.running:
            opcode, type1, type2, type3, pnum = self.getinstruction(self.inpt[self.pointer])
            #print(opcode, type1, type2, type3, pnum)
            if self.instruction[opcode](type1, type2, type3) == 0:
                self.pointer += pnum + 1
            if opcode == '04':
                yield self.outs[-1]
