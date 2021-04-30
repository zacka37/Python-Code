import random
from turtle import Turtle

def circle_repeat(turtle, angle, number, forward, radius):
    colors = ["blue", "purple", "green", "red", "orange"]
    color = random.choice(colors)
    turtle.color(color)
    turtle.right(angle)
    turtle.forward(forward)
    turn = 100/number
    for x in range(number):
        turtle.circle(radius)
        turtle.left(turn)
    radius = radius - forward
    if (radius > 0):
        circle_repeat(turtle, number, angle, forward, radius)
        

def main():
    animation_speed = 10
    leonardo = Turtle()
    leonardo.speed(animation_speed)
    circle_repeat(leonardo, 2, 50, 2, 50)
main()
