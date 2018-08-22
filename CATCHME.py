from turtle import *
import turtle
import time
import math
import random

sc=turtle.Screen()
sc.bgcolor("yellow")
sc.tracer(2)

t=turtle.Turtle()
t.color("red")
t.shape("turtle")
t.penup()
speed=0



goal=turtle.Turtle()
goal.color("green")
goal.shape("circle")
goal.setposition(0,0)
goal.penup()
goal.setposition(random.randint(-300,300),random.randint(-200,200))
goal.pendown()










def turnleft():
    t.left(30)
def turnright():
    t.right(30)
def incspeed():
    global speed
    speed=speed+0.4
def decspeed():
    global speed
    speed=0


score=0
turtle.listen()
turtle.onkey(turnleft,"Left")
turtle.onkey(turnright,"Right")
turtle.onkey(incspeed,"Up")
turtle.onkey(decspeed,"Down")
maxs=0
t2=Pen()
t2.color("black")
t2.speed(2)
t2.up()
t2.goto(-320,-220)
t2.down()
t2.forward(630)
t2.left(90)
t2.forward(450)
t2.left(90)
t2.forward(630)
t2.left(90)
t2.forward(450)
t2.up()
t2.setposition(-300,240)

t2.write("SCORE : "+str(score),font=("Arial", 10, "normal"))
t3=Pen()
t3.color("black")
t3.up()
t3.setposition(100,240)
t3.hideturtle()
t3.write("MAX SCORE : "+str(maxs),font=("Arial", 10, "normal"))
t2.hideturtle()
while(1):
    t.forward(speed)
    if(t.ycor()<=-220 or t.ycor()>=230 or t.xcor()<=-320 or t.xcor()>=310):
        speed=0
        for i in range(7):
            t.hideturtle()
            time.sleep(0.2)
            t.showturtle()
        t.setposition(0,0)
        speed=0
        t2.undo()
        if(maxs<score):
            maxs=score
            t3.undo()
            t3.up()
            
            t3.write("MAX SCORE : "+str(maxs),font=("Arial", 10, "normal"))
            
        score=0
        t2.undo()
        t2.write("SCORE : "+str(score),font=("Arial", 10, "normal"))
        
    d=math.sqrt(math.pow(t.xcor()-goal.xcor(),2)+math.pow(t.ycor()-goal.ycor(),2))    
    if(d<20):
        goal.penup()
        goal.setposition(random.randint(-300,300),random.randint(-200,200))
        goal.right(random.randint(0,360))
        goal.pendown()
        t2.undo()
        score+=1
        t2.write("SCORE : "+str(score),font=("Arial", 10, "normal"))



        

    if(goal.ycor()<=-210 or goal.ycor()>=220 or goal.xcor()<=-310 or goal.xcor()>=300):
        goal.right(180)
    goal.penup()
    goal.forward(0.8)
    goal.pendown()











