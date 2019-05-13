import turtle


def draw_Sierpinski_triangle(tess: turtle.Turtle, order: int, size: float, colorChangeDepth: int = -1):
    if order == 0:
        for i in range(3):
            tess.forward(size)
            tess.left(120)
    else:
        if colorChangeDepth == 0:
            tess.color('Red')
        draw_Sierpinski_triangle(tess, order - 1, size / 2, colorChangeDepth - 1)
        tess.penup()
        tess.forward(size / 2)
        tess.pendown()
        if colorChangeDepth == 0:
            tess.color('Blue')
        draw_Sierpinski_triangle(tess, order - 1, size / 2, colorChangeDepth - 1)
        tess.penup()
        tess.left(120)
        tess.forward(size / 2)
        tess.right(120)
        tess.pendown()
        if colorChangeDepth == 0:
            tess.color('Magenta')
        draw_Sierpinski_triangle(tess, order - 1, size / 2, colorChangeDepth - 1)
        tess.penup()
        tess.left(60)
        tess.forward(-size / 2)
        tess.right(60)


window = turtle.Screen()
alex = turtle.Turtle()
alex.speed(0)
draw_Sierpinski_triangle(alex, 4, 200, 2)
window.mainloop()
