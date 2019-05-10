class Connector:
    def __init__(self, fgate, tgate):
        self.fromgate = fgate
        self.togate = tgate
        fgate.setNextConnector(self)

    def getFrom(self):
        return self.fromgate

    def getTo(self):
        return self.togate


class LogicGate:
    def __init__(self, n):
        self.label = n
        self.output = None

    def getLabel(self):
        return self.label

    def setNextConnector(self):
        pass

    def performGateLogic(self):
        pass


class BinaryGate(LogicGate):
    def __init__(self, n):
        super(BinaryGate, self).__init__(n)
        self.inputA = None
        self.inputB = None
        self.NextConnector = None

    def setNextConnector(self, conn):
        self.NextConnector = conn

    def getNextInputToProduce(self, n=None):
        if self.inputA == None:
            if n == None:
                n = int(input('Enter ' + self.getLabel() + ' first inputs:'))
                self.inputA = n
                self.getNextInputToProduce()
            else:
                self.inputA = n
        elif self.inputB == None:
            if n == None:
                n = int(input('Enter ' + self.getLabel() + ' second inputs:'))
            self.inputB = n
            res = self.performGateLogic()
            self.inputA = None
            self.inputB = None
            if self.NextConnector == None:
                print(res)
            else:
                self.NextConnector.getTo().getNextInputToProduce(res)
        else:
            raise RuntimeError('Full inputs')


class AndGate(BinaryGate):
    def performGateLogic(self):
        return int(self.inputA == 1 and self.inputB == 1)


andgate1 = AndGate('AND1')
andgate2 = AndGate('AND2')
andgate3 = AndGate('AND3')
c1 = Connector(andgate1, andgate3)
c2 = Connector(andgate2, andgate3)
andgate1.getNextInputToProduce()
andgate2.getNextInputToProduce()
