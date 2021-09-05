import turtle
import pygame
from pygame import mixer
import random
import time
import os
pygame.init()
dela = 0.1

# Creating the game display
window=turtle.Screen()
window.title("snakey turtle")
window.bgcolor("#000000")
window.setup(width=600,height=600)
window.tracer(0)

# Loading turtle-part 1
Loading=turtle.Turtle()
Loading.speed(0)
Loading.color("#FFFFFF")
Loading.shapesize(5)
Loading.write('Loading........',align="center",font=('arial',14,"italic"))
Loading.hideturtle()

# Loading turtle-part 2
L_turtle=turtle.Turtle()
L_turtle.speed(0)
L_turtle.color("#FFFFFF")
L_turtle.shape("classic")
L_turtle.pensize(25)
L_turtle.shapesize(2)
L_turtle.penup()
L_turtle.goto(-500,-50)
L_turtle.pendown()
L_turtle.hideturtle()
L_turtle_speed=1

# Game loop
def game():
	
	#Food
	Food=turtle.Turtle()
	Food.speed(0)
	Food.shape("square")
	Food.color("red")
	Food.shapesize(2)
	Food.penup()
	Food.goto(100,0)

# snake head
	snake_head=turtle.Turtle()
	snake_head.speed(0)
	snake_head.shape("square")
	snake_head.color("white")
	snake_head.shapesize(2)
	snake_head.penup()
	snake_head.goto(0,0)
	snake_head.direction="stop"
	snake_heads=[]

#score
	scores=0

#displaying score
	score=turtle.Turtle()
	score.speed(0)
	score.color("#FFFAFA")
	score.shapesize()
	score.penup()
	score.hideturtle()
	score.goto(-490,950)
	score.write("Score: 0",font=('arial',24,'italic'))

# displaying game over
	game_over=turtle.Turtle()
	game_over.color("#000000")
	game_over.penup()
	game_over.hideturtle()
	
# Movement of the snake
	def move_up():
		snake_head.direction="up"
	def move_down():
		snake_head.direction="down"	
	def move_right():
		snake_head.direction="right"
	def move_left():
		snake_head.direction="left"
	
	def move():
		if snake_head.direction=="up":
			y = snake_head.ycor()
			snake_head.sety(y + 20)
		
		if snake_head.direction=="down":
			y = snake_head.ycor()
			snake_head.sety(y - 20)
		
		if snake_head.direction=="left":
			x = snake_head.xcor()
			snake_head.setx(x - 20)
		
		if snake_head.direction=="right":
			x = snake_head.xcor()
			snake_head.setx(x + 20)
		
# pressed Keyboard
	window.listen()
	window.onkeypress(move_up, "u")
	window.onkeypress(move_down, "d")
	window.onkeypress(move_left, "l")
	window.onkeypress(move_right, "r")
	
	while True:
	
		window.update()
	# Food movement
		if snake_head.distance(Food) < 20:
			snake_head.direction="up"
			mixer.music.load('hiss.wav')
			mixer.music.play(int(0.1))
			x=random.randint(-290,290)
			y=random.randint(-290,290)
			Food.goto(x,y)
			window.bgcolor(("gray"))
			score.clear()
			scores += 1
			score.write("Score:"+ str(scores),font=('arial',24,'italic'))
		
		# New snake body after eating snake
			new_body=turtle.Turtle()
			new_body.speed(0)
			new_body.shape("square")
			new_body.color("chartreuse")
			new_body.shapesize(2)
			new_body.penup()
			snake_heads.append(new_body)
		
		
	# increase 	the  length
		for index in range(len(snake_heads)-1, 0, -1):
			x=snake_heads[index-1].xcor()
			y=snake_heads[index-1].ycor()
			snake_heads[index].goto(x,y)
		
		if len(snake_heads)> 0:
			x=snake_head.xcor()
			y=snake_head.ycor()
			snake_heads[0].goto(x,y)
		
	# boder collisions		
		if snake_head.ycor()>1090 or snake_head.ycor()<-1090 or snake_head.xcor()>500 or snake_head.xcor()<-500: 
			new_body.color("orangered")
			snake_head.goto(0,1500)
			Food.hideturtle()
			window.bgcolor("orangered")
			score.clear()
			game_over.goto(0,300)
			game_over.write("U Lost!!",align="center",font=('arial',40,"italic"))
			score.write(" Your score:"+ str(scores),align="center",font=('arial',24,'italic'))
			score.goto(0,0)
	
		
		move()
		time.sleep(dela)
		move_right()
	window.mainloop()
	
while True:
	window.update()
	x=L_turtle.xcor()
	x += L_turtle_speed
	L_turtle.setx(x)
	
	if L_turtle.xcor()>500:
		L_turtle.clear()
		Loading.clear()
		game()
		
window.mainloop()
