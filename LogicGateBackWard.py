class LogicGate:
    def __init__(self, n):
        self.label = n
        self.output = None

    def getLabel(self):
        return self.label

    def getOutput(self):
        self.output = self.performGateLogic()
        return self.output


class Connector:
    def __init__(self, fgate, tgate):
        self.fromgate = fgate
        self.togate = tgate
        tgate.setNextPin(self)

    def getFrom(self):
        return self.fromgate

    def getTo(self):
        return self.togate


class BinaryGate(LogicGate):
    def __init__(self, n):
        super(BinaryGate, self).__init__(n)
        self.pinA = None
        self.pinB = None

    def setNextPin(self, source: Connector):
        if self.pinA == None:
            self.pinA = source
        else:
            if self.pinB == None:
                self.pinB = source
            else:
                raise RuntimeError('Error:NO EMPTY PINS')

    def getPinA(self):
        if self.pinA == None:
            return int(input('Enter Pin A input for gate ' + self.getLabel() + '-->'))
        else:
            return self.pinA.getFrom().getOutput()

    def getPinB(self):
        if self.pinB == None:
            return int(input('Enter Pin B input for gate ' + self.getLabel() + '-->'))
        else:
            return self.pinB.getFrom().getOutput()


class UnaryGate(LogicGate):
    def __init__(self, n):
        super(UnaryGate, self).__init__(n)
        self.pin = None

    def setNextPin(self, source: Connector):
        if self.pin == None:
            self.pin = source
        else:
            raise RuntimeError('Error:NO EMPTY PINS')

    def getPin(self):
        if self.pin == None:
            return int(input('Enter Pin input for gate ' + self.getLabel() + '-->'))
        else:
            return self.pin.getFrom().getOutput()


class OrGate(BinaryGate):
    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        if a == 1 or b == 1:
            return 1
        else:
            return 0


class NotGate(UnaryGate):
    def performGateLogic(self):
        if self.getPin() == 0:
            return 1
        else:
            return 0


class AndGate(BinaryGate):
    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        if a == 1 and b == 1:
            return 1
        else:
            return 0


class NandGate(BinaryGate):
    def performGateLogic(self):
        return 1 - AndGate.performGateLogic(self)


class NorGate(BinaryGate):
    def performGateLogic(self):
        return 1 - OrGate.performGateLogic(self)


class XorGate(BinaryGate):
    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        if a == b:
            return 0
        else:
            return 1


class XnorGate(BinaryGate):
    def performGateLogic(self):
        return 1 - XorGate.performGateLogic(self)


class CopyGate(UnaryGate):
    def performGateLogic(self):
        if self.pin == None:
            self.pin = self.getPin()
        return self.pin


def FullAdder(a: int, b: int):
    if not (0 <= a < 256 and 0 <= b < 256):
        raise ValueError('Arguments must be within list(range(256))')

    def CalCulate4(a4, b4):
        if 0 <= a4 < 16 and 0 <= b4 < 16:
            copygateA = CopyGate('A')
            # copygateA.pin = a4 % 2
            copygateB = CopyGate('B')
            # copygateB.pin = b4 % 2
            copygateCIN = CopyGate('CIN')
            # copygateCIN.pin = 0
            xorgate1 = XorGate('XOR1')
            xorgate2 = XorGate('XOR2')
            andgate1 = AndGate('AND1')
            andgate2 = AndGate('AND2')
            orgate = OrGate('OR')
            c1 = Connector(copygateA, xorgate1)
            c2 = Connector(copygateA, andgate1)
            c3 = Connector(copygateB, xorgate1)
            c4 = Connector(copygateB, andgate1)
            c5 = Connector(copygateCIN, xorgate2)
            c6 = Connector(copygateCIN, andgate2)
            c7 = Connector(andgate1, orgate)
            c8 = Connector(xorgate1, andgate2)
            c9 = Connector(xorgate1, xorgate2)
            c10 = Connector(andgate2, orgate)
            S = 0
            C = 0
            for i in range(4):
                digita = a4 % 2
                digitb = b4 % 2
                copygateA.pin = digita
                copygateB.pin = digitb
                copygateCIN.pin = C
                S += xorgate2.getOutput() * 2 ** i
                C = orgate.getOutput()
                a4 //= 2
                b4 //= 2
        return (C, S)

    a_front4 = a // 16
    b_front4 = b // 16
    a_after4 = a % 16
    b_after4 = b % 16
    atfer_res = CalCulate4(a_after4, b_after4)
    front_res = CalCulate4(a_front4, b_front4)
    front_front = front_res[0]
    front_res = CalCulate4(front_res[1], atfer_res[0])

    return bin(CalCulate4(front_res[0], front_front)[1] * 256 + front_res[1] * 16 + atfer_res[1])


if __name__ == '__main__':
    print(FullAdder(0b10110110, 0b01010100) == bin(sum([0b10101110, 0b01010100])))
# Half Adder
# xorgate = XorGate('XOR')
# andgate = AndGate('AND')
# copygate1 = CopyGate('CG1')
# copygate2 = CopyGate('CG2')
# c1 = Connector(copygate1, xorgate)
# c2 = Connector(copygate2, xorgate)
# c3 = Connector(copygate1, andgate)
# c4 = Connector(copygate2, andgate)
# print(andgate.getOutput(), xorgate.getOutput())
# Full Adder
