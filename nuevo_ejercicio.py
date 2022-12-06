import turtle
import math

wn = turtle.Screen()
wn.bgcolor("lightgreen")        # set the window background color

luis =turtle.Turtle()
luis.color("red")
luis.pensize(5)

bob= turtle.Turtle()
bob.color("white")
bob.pensize(4)

luis.left(45)
luis.forward(45)
luis.left(45)
luis.right(180)

elan = turtle.Turtle()

tess = turtle.Turtle()
tess.color("blue")              # make tess blue
tess.pensize(3)                 # set the width of her pen
tess.shape("turtle")

tess.left(90)
tess.forward(150)
tess.left(90)
tess.forward(75)

def cuadricula():
    distance = 50
    for _ in range(10):
         elan.forward(distance)
         elan.right(90)
         distance = distance + 10
cuadricula()

def espiral():
    distance= 60
    angulo=45
    for _ in range(11):
        luis.forward(distance)
        luis.right(angulo)
        distance=distance+5
espiral()        

def ranaSaltando():
    dist = 5
    tess.up()                     # this is new
    for _ in range(30):    # start with size = 5 and grow by 2
        tess.stamp()                # leave an impression on the canvas
        tess.forward(dist)          # move tess along
        tess.right(24)              # and turn her
        dist = dist + 2
ranaSaltando()        

def hacer_casa():
    bob.right(90)
    bob.forward(50)
    bob.left(90)
    bob.forward(50)

# Add your code below!
    bob.left(90)
    bob.forward(50)
    bob.left(90)
    bob.forward(50)
    bob.right(135)
    dist = math.sqrt(50*50/2)
    bob.forward(dist)
    bob.right(90)
    bob.forward(dist)
    wn.exitonclick()
hacer_casa()


wn.exitonclick()                # wait for a user click on the canvas
