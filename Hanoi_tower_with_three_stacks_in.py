from pythonds import Stack


def hanoi(n: int, from_stack: Stack, assist_stack: Stack, to_stack: Stack):
    if n == 1:
        to_stack.push(from_stack.pop())
        print(from_stack, '==>', to_stack)
    else:
        hanoi(n - 1, from_stack, to_stack, assist_stack)
        to_stack.push(from_stack.pop())
        print(from_stack, '==>', to_stack)
        hanoi(n - 1, assist_stack, from_stack, to_stack)


# 重新定义Stack方法，使其可以打印名字
def __init__(self, name: str):
    self.items = []
    self.name = name


Stack.__init__ = __init__


def __str__(self):
    return self.name


Stack.__str__ = __str__

from_stack = Stack('From Stack')
for i in range(64):
    from_stack.push('disk')
assist_satck = Stack('Assist Satck')
to_stack = Stack('To Stack')
hanoi(from_stack.size(), from_stack, assist_satck, to_stack)
