import turtle


def koch(tess: turtle.Turtle, order: int, size: float) -> None:
    if order == 0:
        tess.forward(size)
    else:
        for angle in [-60, 120, -60, 0]:
            koch(tess, order - 1, size / 3)
            tess.left(angle)


def snowflake(tess: turtle.Turtle, order: int, size: float):
    for _ in range(3):
        koch(tess, order, size)
        tess.left(120)


window = turtle.Screen()
alex = turtle.Turtle()
alex.speed(0)
snowflake(alex, 3, 300)
window.mainloop()
