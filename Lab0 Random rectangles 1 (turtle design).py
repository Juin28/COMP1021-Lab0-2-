import random
import turtle

turtle.speed(8)
turtle.shape("turtle")

colorlist = ["red","orange","yellow","green","blue","indigo","purple","pink","gold","silver","cyan","brown"]

i = 0

while i <= 100:
    x = random.randint(-350,350)
    y = random.randint(-250,250)
    l = random.randint(10,100)
    w = random.randint(10,100)
    t = random.randint(0,360)
    h = random.randint(5,15)
    c = random.choice(colorlist)
    turtle.begin_fill()
    turtle.color(c)
    turtle.up()
    turtle.goto(x,y)
    turtle.down()
    turtle.width(h)
    turtle.left(t)
    turtle.forward(l)
    turtle.left(90)
    turtle.forward(w)
    turtle.left(90)
    turtle.forward(l)
    turtle.left(90)
    turtle.forward(w)
    turtle.end_fill()
    i += 1
