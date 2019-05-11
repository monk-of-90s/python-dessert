import timeit
import matplotlib.pyplot as plt


class Queue1:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


class Queue2:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)


lengths = []
times1 = []
times2 = []
queue1 = Queue1()
t1 = timeit.Timer('queue1.dequeue()', 'from __main__ import queue1\nqueue1.enqueue(10)')
queue2 = Queue2()
t2 = timeit.Timer('queue2.dequeue()', 'from __main__ import queue2\nqueue2.enqueue(10)')

for length in range(10000, 1000001, 20000):
    lengths.append(length)
    queue1.items = list(range(length))
    time1 = t1.timeit(1000)
    times1.append(time1)

    queue2.items = list(range(length))
    time2 = t2.timeit(1000)
    times2.append(time2)
plt.plot(lengths, times1, 'o', label='queue1')
plt.plot(lengths, times2, 'o', label='queue2')
plt.legend()
plt.show()
print(times1)
print(times2)
