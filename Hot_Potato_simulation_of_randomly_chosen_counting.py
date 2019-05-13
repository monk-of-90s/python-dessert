import random

from pythonds.basic import Queue


def hotPotato(namelist):
    simqueue = Queue()
    for name in namelist:
        simqueue.enqueue(name)
    length = len(namelist)
    randomor = random.Random()
    while simqueue.size() > 1:
        num = randomor.randrange(length, 2 * length + 1)
        for i in range(num):
            simqueue.enqueue(simqueue.dequeue())

        simqueue.dequeue()

    return simqueue.dequeue()


print(hotPotato(["Bill", "David", "Susan", "Jane", "Kent", "Brad"]))
