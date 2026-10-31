import turtle

screen = turtle.Screen()
screen.setup(800, 600)
screen.bgcolor("midnight blue")
screen.title("A Night Under the Stars")

t = turtle.Turtle()
t.speed(0)
t.hideturtle()


def draw_circle(x, y, radius, colour):
    t.penup()
    t.goto(x, y - radius)
    t.pendown()
    t.color(colour)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()


def draw_triangle(x, y, size, colour):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(colour)
    t.begin_fill()

    for i in range(3):
        t.forward(size)
        t.left(120)

    t.end_fill()


def draw_rectangle(x, y, width, height, colour):
    t.penup()
    t.goto(x, y)
    t.setheading(0)
    t.pendown()
    t.color(colour)
    t.begin_fill()

    for i in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)

    t.end_fill()


def draw_star(x, y):
    t.penup()
    t.goto(x, y)
    t.setheading(0)
    t.pendown()
    t.color("white")

    for i in range(5):
        t.forward(15)
        t.right(144)


def draw_tree(x, y):
    draw_rectangle(x + 15, y, 12, 35, "saddlebrown")
    draw_triangle(x, y + 25, 45, "dark green")
    draw_triangle(x + 5, y + 50, 35, "forest green")



draw_circle(-270, 190, 45, "gold")
draw_circle(-250, 205, 40, "midnight blue")


for x, y in [(-150, 200), (-50, 250), (80, 190),
             (180, 240), (280, 170), (320, 260)]:
    draw_star(x, y)


draw_triangle(-350, -170, 250, "purple")
draw_triangle(-180, -170, 300, "indigo")
draw_triangle(50, -170, 280, "purple")


draw_rectangle(-400, -250, 800, 80, "dark green")


draw_rectangle(-70, -170, 140, 100, "saddlebrown")
draw_triangle(-90, -70, 180, "firebrick")


draw_rectangle(-45, -140, 30, 35, "yellow")
draw_rectangle(25, -140, 30, 35, "yellow")
draw_rectangle(-10, -170, 30, 60, "brown")

draw_tree(-300, -240)
draw_tree(220, -240)
draw_tree(300, -240)

t.penup()
t.goto(-120, 270)
t.color("white")
t.write("A Night Under the Stars", font=("Arial", 18, "bold"))

turtle.done()
