import turtle


def hilbert_curve(tur: turtle.Turtle, point1: tuple, point2: tuple) -> None:
    # base case
    tur.penup()
    tur.goto(*point1)
    tur.setheading(tur.towards(*point2))
    # 丈量距离
    length = tur.distance(*point2)  # 至此乌龟在左上角，指向右上角，未放下画笔
    # 绘制长度下限
    minlength = 20
    if length < minlength:
        # 绘制开放的正方形
        tur.pendown()
        tur.right(90)
        for i in range(3):
            tur.forward(length)
            tur.left(90)
        tur.left(180)
    else:
        # 计算下级间隔宽度
        n = 1
        interval = length
        while interval >= minlength:
            n = 2 * n + 1
            interval = length / n
        # 准备绘制左上角下级
        nextp2 = point1
        nextp1 = ()
        tur.right(90)
        tur.forward((length - interval) / 2)
        nextp1 = tur.pos()
        hilbert_curve(tur, nextp1, nextp2)
        # 绘制间隔
        tur.penup()
        tur.left(180)
        tur.goto(*nextp1)
        tur.pendown()
        tur.forward(interval)
        # 准备绘制左下角下级
        nextp1 = tur.pos()
        tur.left(90)
        tur.penup()
        tur.forward((length - interval) / 2)
        nextp2 = tur.pos()
        # 绘制下级
        hilbert_curve(tur, nextp1, nextp2)
        # 绘制下部间隔
        tur.pendown()
        tur.forward(interval)
        # 准备绘制右下角下级
        nextp1 = tur.pos()
        tur.penup()
        tur.forward((length - interval) / 2)
        nextp2 = tur.pos()
        # 绘制下级
        hilbert_curve(tur, nextp1, nextp2)
        # 绘制右侧间隔
        tur.left(90)
        tur.pendown()
        tur.forward(interval)
        # 准备绘制右上角下级
        nextp2 = tur.pos()
        tur.penup()
        tur.forward((length - interval) / 2)
        nextp1 = tur.pos()
        # 绘制下级
        hilbert_curve(tur, nextp1, nextp2)
        # 固定最终状态
        tur.penup()
        tur.goto(point2)
        tur.setheading(tur.towards(*point1))
        tur.left(180)


alex = turtle.Turtle()
alex.speed(0)

win = turtle.Screen()
hilbert_curve(alex, (-100, 100), (100, 100))
win.mainloop()
