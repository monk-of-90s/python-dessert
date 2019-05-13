import turtle


def draw_cesaro(tess: turtle.Turtle, order: int, size: float, angle: float):
    if order == 0:
        tess.forward(size)
    else:
        size = size / 2 / (1 + math.sin(math.radians(angle / 2)))
        for turn_angle in [90 - angle / 2, angle - 180, 90 - angle / 2, 0]:
            draw_cesaro(tess, order - 1, size, angle)
            tess.right(turn_angle)


def draw_cesaro_square(tess: turtle.Turtle, order: int, size: float, angle: float):
    for _ in range(4):
        draw_cesaro(tess, order, size, angle)
        tess.right(90)


window = turtle.Screen()
alex = turtle.Turtle()
alex.speed(0)

for _ in range(4):
    draw_cesaro_square(alex, _, 50, 20)
    alex.penup()
    alex.forward(55)
    alex.pendown()

window.mainloop()
