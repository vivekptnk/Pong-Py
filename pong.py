# simple pong in python

import turtle

wn = turtle.Screen()
wn.title('Pong by Ya boi')
wn.bgcolor("orange")
wn.setup(width = 800  ,height=600)
wn.tracer(0)

# bat A
bat_a = turtle.Turtle()
bat_a.speed(0)
bat_a.shape("square")
bat_a.color("black")
bat_a.shapesize(stretch_wid=5, stretch_len=1)
bat_a.penup()
bat_a.goto(-350, 0)

# bat B
bat_b = turtle.Turtle()
bat_b.speed(0)
bat_b.shape("square")
bat_b.color("black")
bat_b.shapesize(stretch_wid=5, stretch_len=1)
bat_b.penup()
bat_b.goto(350, 0)

# gend(ball in hindi)
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("black")
ball.penup()
ball.goto(0, 0)

# Game Loop
while True:
    wn.update()
