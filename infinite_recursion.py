import sys


def f():
    f()


sys.setrecursionlimit(200)
print(sys.getrecursionlimit())
f()
