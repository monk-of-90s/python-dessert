from pythonds import Stack

import turtle


# 自定义海龟形状
class Disk(turtle.Turtle):
    def __init__(self, length: float):
        super(Disk, self).__init__()
        self.shape('square')
        self.resizemode('user')
        if length == 0:
            length = 1
        self.shapesize(length, 0.5)
        self.speed(2)
        self.left(90)
        self.penup()


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
def __init__(self, name: str, x: float = 0, y: float = 0):
    self.x = x
    self.y = y
    self.items = []
    self.name = name
    tur = turtle.Turtle()
    tur.penup()
    tur.goto(x, y)
    tur.setheading(0)
    tur.pendown()
    tur.forward(20)
    tur.backward(40)
    tur.forward(15)
    tur.left(90)
    tur.forward(150)
    tur.left(-90)
    tur.forward(10)
    tur.left(-90)
    tur.forward(150)
    tur.hideturtle()
    del tur


Stack.__init__ = __init__


def __str__(self):
    return self.name


def push(self, item: Disk):
    if self.items != []:
        last_disk_size = self.peek().shapesize()
    else:
        last_disk_size = None
    self.items.append(item)

    # 设置长度
    if last_disk_size != None:
        length=last_disk_size[0] - 1
        if length<= 0:
            length=1
            for i in self.items:
                i.resizemode('user')
                i.shapesize(i.shapesize()[0] + 1, 0.5)
        item.shapesize(*(length, last_disk_size[1]))
    # 海龟位置y坐标
    index = len(self.items) - 1
    item_y = 20 * 0.5 / 2 + index * 20 * 0.5 + self.y
    # 海龟就位
    self.items[index]: Disk.penup()
    self.items[index].goto(self.x, item_y)


Stack.push = push
Stack.__str__ = __str__

screen = turtle.Screen()

from_stack = Stack('From Stack', -300, -150)
for i in range(6):
    from_stack.push(Disk(0))
assist_satck = Stack('Assist Satck', 0, 100)
to_stack = Stack('To Stack', 300, -150)
hanoi(from_stack.size(), from_stack, assist_satck, to_stack)
screen.mainloop()
