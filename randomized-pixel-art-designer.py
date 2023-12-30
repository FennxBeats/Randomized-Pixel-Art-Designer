import turtle
import random

t = turtle.Turtle()
wn = turtle.Screen()
wn.title("Randomized Pixel Art Designer")
t.speed("fastest")  # Use a string for predefined speed

def pixel(x, y):
    print(x,y)
    t.penup()
    t.goto(x, y)
    
    t.begin_fill()
    for _ in range(4):
        t.pendown()
        t.forward(20)
        t.right(90)
    t.end_fill()
    t.penup()

def get_random_color():
    # Generate a random RGB color
    r = random.random()
    g = random.random()
    b = random.random()
    return (r, g, b)

def change_color(x, y):
    t.pencolor(get_random_color())
    pen_fillcolor = t.pencolor()
    t.fillcolor(pen_fillcolor)


wn.onscreenclick(pixel, 1)  # Bind the pixel function to the right mouse click event
wn.onscreenclick(change_color, 3)    # Bind the change_color function to the scroll event

wn.mainloop()
