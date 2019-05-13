from pythonds import Stack


class Queue:
    def __init__(self):
        self.inbox = Stack()
        self.outbox = Stack()

    def enqueue(self, item):
        while self.outbox.size() != 0:
            self.inbox.push(self.outbox.pop())
        self.inbox.push(item)

    def dequeue(self):
        while self.inbox.size() != 0:
            self.outbox.push(self.inbox.pop())
        return self.outbox.pop()
