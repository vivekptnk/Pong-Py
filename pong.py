# simple pong in python

import turtle
import winsound

wn = turtle.Screen()
wn.title('Pong by Yaboi')
wn.bgcolor("orange")
wn.setup(width = 800  ,height=600)
wn.tracer(0)

# score keeper
score_a = 0
score_b = 0

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
ball.dx = 0.5
ball.dy = 0.5

# pen score
pen = turtle.Turtle()
pen.speed(0)
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A : 0     Player B : 0", align = "center", font = {"Courier", 24, "bold"})

# functions of the gaming hell
def bat_a_up():
    y = bat_a.ycor()
    y +=  20
    bat_a.sety(y)

def bat_a_down():
    y = bat_a.ycor()
    y -= 20
    bat_a.sety(y)

def bat_b_up():
    y = bat_b.ycor()
    y +=  20
    bat_b.sety(y)

def bat_b_down():
    y = bat_b.ycor()
    y -= 20
    bat_b.sety(y)

# key bindingsz
wn.listen()
wn.onkeypress(bat_a_up,"w")
wn.onkeypress(bat_a_down,"s")
wn.onkeypress(bat_b_up,"Up")
wn.onkeypress(bat_b_down,"Down")

# Game Loop
while True:
    wn.update()

    # ball movement 
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # border control
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)
    
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)
    
    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A : {}     Player B : {}".format(score_a, score_b) , align = "center", font = {"Courier", 24, "bold"})
    
    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A : {}     Player B : {}".format(score_a, score_b) , align = "center", font = {"Courier", 24, "bold"})

    # ball n boll collision
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < bat_b.ycor() + 40 and ball.ycor() > bat_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < bat_a.ycor() + 40 and ball.ycor() > bat_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)