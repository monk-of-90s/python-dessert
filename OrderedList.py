class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext


class OrderedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        s = ''
        current = self.head
        while current != None:
            s += str(current.getData()) + ' '
            current = current.getNext()
        return s

    def search(self, item):
        current = self.head
        found = False
        stop = False
        while current != None and not found and not stop:
            if current.getData() == item:
                found = True
            else:
                if current.getData() > item:
                    stop = True
                else:
                    current = current.getNext()

        return found

    def index(self, item: int or float):
        current = self.head
        found = False
        stop = False
        series = -1
        while current != None and not found and not stop:
            series += 1
            if current.getData() == item:
                found = True
            else:
                if current.getData() > item:
                    stop = True
                else:
                    current = current.getNext()

        return series if found else -1

    def append(self, item):
        current = self.head
        if current == None:
            self.head = Node(item)
        else:
            while current != None:
                previous = current
                current = current.getNext()
            previous.setNext(Node(item))
        self.num += 1
    def add(self, item):
        current = self.head
        previous = None
        stop = False
        while current != None and not stop:
            if current.getData() > item:
                stop = True
            else:
                previous = current
                current = current.getNext()

        temp = Node(item)
        if previous == None:
            temp.setNext(self.head)
            self.head = temp
        else:
            temp.setNext(current)
            previous.setNext(temp)

    def isEmpty(self):
        return self.head == None

    def remove(self, item: int or float):
        previous: Node = None
        current = self.head
        while current != None:
            if current.getData() == item:
                if previous == None:
                    self.head = current.getNext()
                else:
                    previous.setNext(current.getNext())
                break
            else:
                previous = current
                current = current.getNext()

    def pop(self, index: int = -1):
        previous: Node = None
        current = self.head
        while current != None:
            if current.getNext() == None and index == -1:
                index = 0
            if index == 0:
                if previous == None:
                    self.head = current.getNext()
                else:
                    previous.setNext(current.getNext())
                break
            elif index > 0:
                index -= 1
            previous = current
            current = current.getNext()

        return current.getData()

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()

        return count


mylist = OrderedList()
mylist.add(31)
mylist.add(77)
mylist.add(17)
mylist.add(93)
mylist.add(26)
mylist.add(54)
print(mylist)
print(mylist.pop(3))
print(mylist)
