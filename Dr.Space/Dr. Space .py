import turtle as t
import random
import os
import pygame
from pygame import mixer
pygame.init()

# Value stored variables
width=500
height=1100
crashed=False

 
 # Game Screen
screen=t.Screen()
screen.setup(width,height)
screen.bgcolor("black")
screen.tracer(0)

t.register_shape('logo.gif')
t.register_shape('pl.gif')
t.register_shape('player.gif')

def Game_starts():
	
	
	mixer.music.load('space.mp3')
	mixer.music.play(-1)
	
	# Player
	Player=t.Turtle()
	Player.speed(0)
	Player.color("lime")
	Player.shape("player.gif")
	Player.shapesize(15)
	Player.penup()
	Player.lt(90)
	Player.goto(-200,-900)

	# Road lines
	Line_1=t.Turtle()
	Line_1.speed(0)
	Line_1.color("black")
	Line_1.shape("square")
	Line_1.shapesize(stretch_len=2,stretch_wid=15)
	Line_1.penup()
	Line_1.goto(0,0)
	Line_1_speed=30
	
	Line_2=t.Turtle()
	Line_2.speed(0)
	Line_2.color("black")
	Line_2.shape("square")
	Line_2.shapesize(stretch_len=2,stretch_wid=15)
	Line_2.penup()
	Line_2.goto(0,500)
	Line_2_speed=30
	
	Line_3=t.Turtle()
	Line_3.speed(0)
	Line_3.color("black")
	Line_3.shape("square")
	Line_3.shapesize(stretch_len=2,stretch_wid=15)
	Line_3.penup()
	Line_3.goto(0,950)
	Line_3_speed=30
	
	Line_4=t.Turtle()
	Line_4.speed(0)
	Line_4.color("black")
	Line_4.shape("square")
	Line_4.shapesize(stretch_len=2,stretch_wid=15)
	Line_4.penup()
	Line_4.goto(0,-500)
	Line_4_speed=30
	
	Line_5=t.Turtle()
	Line_5.speed(0)
	Line_5.color("black")
	Line_5.shape("square")
	Line_5.shapesize(stretch_len=2,stretch_wid=15)
	Line_5.penup()
	Line_5.goto(0,-900)
	Line_5_speed=30

	def move_up():
		Player.direction="up"
	def move_down():
		Player.direction="down"	
	def move_right():
		Player.direction="right"
	def move_left():
		Player.direction="left"
	
	def move():
		if Player.direction=="up":
			y = Player.ycor()
			Player.sety(y + 20)
		
		if Player.direction=="down":
			y = Player.ycor()
			Player.sety(y - 20)
		
		if Player.direction=="left":
			x = Player.xcor()
			Player.setx(x - 20)
		
		if Player.direction=="right":
			x = Player.xcor()
			Player.setx(x + 20)
			
			
	screen.listen()
	screen.onkeypress(move_up, "u")
	screen.onkeypress(move_down, "d")
	screen.onkeypress(move_left, "l")
	screen.onkeypress(move_right, "r")
	
	
	# Obstacles
	Obstacles=t.Turtle()
	Obstacles.speed(0)
	Obstacles.color("red")
	Obstacles.shape("circle")
	Obstacles.shapesize(15)
	Obstacles.penup()
	Obstacles.goto(-200,900)
	Obstacles_speed=40
		
	scores=0
	# score
	score=t.Turtle()
	score.speed(0)
	score.color("red")
	score.shape("circle")
	score.hideturtle()
	score.shapesize(8)
	score.penup()
	score.goto(-510,900)
	score.write('score: 0',font=("arial",22,"italic bold"))
	
	over=t.Turtle()
	over.speed(0)
	over.color("red")
	over.shape("circle")
	over.hideturtle()
	over.penup()
	over.goto(-450,0)
	
	# Game Loop
	while not crashed:
		
		screen.update()
		# Line_1
		y=Line_1.ycor()
		y -=Line_1_speed
		Line_1.sety(y)
		
			# Line_2
		y=Line_2.ycor()
		y -=Line_2_speed
		Line_2.sety(y)
		
		# Line_3
		y=Line_3.ycor()
		y -=Line_3_speed
		Line_3.sety(y)
		
		 # Line_4
		y=Line_4.ycor()
		y -=Line_4_speed
		Line_4.sety(y)
		
		# Line_5
		y=Line_5.ycor()
		y -=Line_5_speed
		Line_5.sety(y)
		
		if Line_1.ycor() < -1100:
			y=1150
			Line_1.sety(y)
			
		if Line_2.ycor() < -1100:
			y=1150
			Line_2.sety(y)
			
		if Line_3.ycor() < -1100:
			y=1150
			Line_3.sety(y)
			
		if Line_4.ycor() < -1100:
			y=1150
			Line_4.sety(y)
			
		if Line_5.ycor() < -1100:
			y=1150
			Line_5.sety(y)
			
		y=Obstacles.ycor()
		y -=Obstacles_speed
		Obstacles.sety(y)
		
		# if obstacles goes over the border
		if Obstacles.ycor() <-1100:
			x=random.randint(-400,400)
			y=random.randint(1000,1150)
			Obstacles.goto(x,y)
			scores += 10
			score.clear()
			score.write('score:'+ str(scores),font=("arial",22,"italic bold"))
			
		# if obstacles collide with Player	
		if Player.distance(Obstacles)<250:
			mixer.music.load('explosion.wav')
			mixer.music.play(1)
			x=random.randint(-400,400)
			y=random.randint(1000,1150)
			Obstacles.goto(x,y)
			Player.hideturtle()
			Obstacles.hideturtle()
			Obstacles_speed=0
			Line_1.hideturtle()
			Line_2.hideturtle()
			Line_3.hideturtle()
			Line_4.hideturtle()
			Line_5.hideturtle()
			score.clear()
			score.goto(-400,200)
			score.write('score:  '+ str(scores),font=("arial",22,"italic bold"))
			over.write('Game Over',font=("arial",35,"italic bold"))
			
			
			
		# if obstacles collide with Line_1	
		if Obstacles.distance(Line_1)<260:
			x=random.randint(-400,400)
			y=random.randint(1000,1150)
			Obstacles.goto(x,y)
			
		# if obstacles collide with Line_2	
		if Obstacles.distance(Line_2)<260:
			x=random.randint(-400,400)
			y=random.randint(1000,1150)
			Obstacles.goto(x,y)
			
		# if obstacles collide with Line_3	
		if Obstacles.distance(Line_3)<260:
			x=random.randint(-400,400)
			y=random.randint(1000,1150)
			Obstacles.goto(x,y)
			
		# if obstacles collide with Line_4	
		if Obstacles.distance(Line_4)<260:
			x=random.randint(-400,400)
			y=random.randint(1000,1150)
			Obstacles.goto(x,y)
			
		# if obstacles collide with Line_5
		if Obstacles.distance(Line_5)<260:
			x=random.randint(-400,400)
			y=random.randint(1000,1150)
			Obstacles.goto(x,y)
			
		
		
	screen.mainloop()
	
# Loading turtle-part 1
Loading=t.Turtle()
Loading.speed(0)
Loading.color("white")
Loading.shapesize(5)
Loading.write('Loading........',align="center",font=('arial',14,"italic"))
Loading.hideturtle()

# Loading turtle-part 2
L_turtle=t.Turtle()
L_turtle.speed(0)
L_turtle.color("yellow")
L_turtle.shape("classic")
L_turtle.pensize(50)
L_turtle.shapesize(2)
L_turtle.penup()
L_turtle.goto(-500,-50)
L_turtle.pendown()
L_turtle.hideturtle()
L_turtle_speed=10

# Dr.Driving
Driving=t.Turtle()
Driving.speed(0)
Driving.color("#6495ED")
Driving.shape("classic")
Driving.penup()
Driving.goto(-500,70)
Driving.hideturtle()
Driving.write('Dr.Space',font=("arial",40,"italic bold"))



# Log
Logo=t.Turtle()
Logo.speed(0)
Logo.color("lime")
Logo.shape("logo.gif")
Logo.shapesize(15)
Logo.penup()
Logo.goto(0,500)
	

while True:
	screen.update()
	x=L_turtle.xcor()
	x += L_turtle_speed
	
	L_turtle.setx(x)
	
	if L_turtle.xcor()>500:
		L_turtle.clear()
		Loading.clear()
		Logo.shape("square")
		Logo.hideturtle()
		screen.bgcolor('white')
		Driving.clear()
		Game_starts()()
		
screen.mainloop()