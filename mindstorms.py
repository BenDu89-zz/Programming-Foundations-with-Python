import turtle 
   
def draw_square():
    turtle.color("red")
    turtle.shape("turtle")
    turtle.speed(0)
    for number in range (1,4):
        turtle.fd(160)
        turtle.lt(90)
    turtle.fd(160)
    turtle.lt(93)

def circle():
    turtle.color("blue")
    turtle.shape("arrow")
    turtle.speed(25)
    turtle.circle(200)
    turtle.lt(5)

for number in range(1,121):
    turtle.bgcolor("green")
    draw_square()
    turtle.bgcolor("yellow")
    turtle.bgcolor("blue")

for number in range(1,73):
    turtle.bgcolor("yellow")
    circle()

turtle.exitonclick()
