import turtle
import os
import random

screen=turtle.Screen()
screen.bgcolor("black")
turtle.tracer(0)


 #Making class of the player
class Ship(turtle.Turtle):
	def __init__(self,shipshape,color,startx,starty):
		turtle.Turtle.__init__(self,shape=shipshape)
		self.speed(0)
		self.penup()
		self.shapesize(stretch_len=6,stretch_wid=4)
		self.color(color)
		self.fd(0)
		self.goto(startx,starty)
		self.speed=1
		
		
	def move(self):
		self.fd(self.speed)
		
	# reflecting player while touching to boundary
		if self.xcor() > 500:
			self.setx(500)
			self.rt(120)
			
		if self.xcor() < -500:
			self.setx(-500)
			self.rt(60)
			
		if self.ycor() > 1050:
			self.sety(1050)
			self.rt(120)
			
		if self.ycor() < -1050:
			self.sety(-1050)
			self.rt(120)
			
	def explode(self, other):
		if (self.xcor() >= (other.xcor()-40)) and \
		(self.xcor() <= (other.xcor()+40)) and \
		(self.ycor() >= (other.ycor()-40)) and \
		(self.ycor() <= (other.ycor()+40)):
			return True
		else:
			return False
		
class Player(Ship):
    def __init__(self,shipshape,color,startx,starty):
    	Ship.__init__(self,shipshape,color,startx,starty)
    	self.speed=8
    	self.lives=3
    	
    	
    def turn_right(self):
    	self.rt(45)
    	
    def turn_left(self):
    	self.lt(45)
    
    def accelerate(self):
    	self.speed += 1
    	
    def d_accelerate(self):
    	self.speed -= 1
    	
    	
class Game_body():
	def __init__(self):
		self.level=1
		self.score=0
		self.state="playing"
		self.pen=turtle.Turtle()
		self.lives=3
	
	
		
class Bomb(Ship):
    def __init__(self,shipshape,color,startx,starty):
    	Ship.__init__(self,shipshape,color,startx,starty)
    	self.speed=25
    	self.shapesize(stretch_len=2,stretch_wid=1,outline=None)
    	
    	self.status='ready'
    	
    def fire(self):
    	if self.status=='ready':
    		self.goto(player.xcor(),player.ycor())
    		self.setheading(player.heading())
    		self.hideturtle()
    		self.status='launching_bomb'
    		
    def launched(self):
    	if self.status=='launching_bomb':
    		self.showturtle()
    		self.fd(self.speed)
    		
    		
    	if self.xcor()<-490 or self.xcor()>490 or \
    	self.ycor()<-1030 or self.ycor()>1030:
    		self.status="ready"
		
class Alien(Ship):
    def __init__(self,shipshape,color,startx,starty):
    	Ship.__init__(self,shipshape,color,startx,starty)
    	self.speed=8
    	self.setheading(random.randint(0,500))
    	self.shapesize(5)
    	
class Team(Ship):
    def __init__(self,shipshape,color,startx,starty):
    	Ship.__init__(self,shipshape,color,startx,starty)
    	self.speed=5
    	self.setheading(random.randint(0,500))
    	self.shapesize(2)
    	
    def move(self):
    	self.fd(self.speed)
    	
    	if self.xcor() > 500:
    		self.setx(470)
    		self.lt(65)
    		
    	if self.xcor() < -500:
    		self.setx(-470)
    		self.lt(65)
    		
    	if self.ycor() > 1050:
    		self.sety(1050)
    		self.lt(65)
    		
    	if self.ycor() < -1050:
    		self.sety(-1050)
    		self.lt(65)
class particle(Ship):
    def __init__(self,shipshape,color,startx,starty):
    	Ship.__init__(self,shipshape,color,startx,starty)
    	self.shapesize(stretch_len=0.1,stretch_wid=0.1,outline=None)
    	self.goto(-1000,-4000)
    	self.frame=0
    	    	
    def explosion(self,startx,starty):
    	self.goto(startx,starty)
    	self.setheading(random.randint(0,800))
    	self.frame=1
    	
    def move(self):
    	if self.frame>0:
    		self.fd(10)
    		self.frame += 1
    		
    	if self.frame>20:
    		self.goto(-1000,-10000)
    	
# Game_body
game=Game_body()

score=0
pen=turtle.Turtle()
pen.speed(0)
pen.color("gray")
pen.shape("classic")
pen.penup()
pen.goto(-450,1000)
pen.write('score: 0',font=("arial",14,"italic"))

# player text
pen1=turtle.Turtle()
pen1.speed(0)
pen1.color("gray")
pen1.shape("classic")
pen1.penup()
pen1.goto(360,1000)
pen1.hideturtle()
pen1.write('player:',font=("arial",7,"italic bold"))

# player powerup
powerup=turtle.Turtle()
powerup.speed()
powerup.color("green")
powerup.shape("circle")
powerup.pensize(30)
powerup.penup()
powerup.goto(350,1075)
powerup.hideturtle()
powerup.pendown()
powerup.speed=10

# powerlow
powerlow=turtle.Turtle()
powerlow.speed()
powerlow.color("red")
powerlow.shape("square")
powerlow.pensize(30)
powerlow.penup()
powerlow.goto(350,1075)
powerlow.hideturtle()
powerlow.pendown()
powerlow.speed=10

# game_over
game_over=turtle.Turtle()
game_over.speed()
game_over.color("white")
game_over.shape("square")
game_over.penup()
game_over.goto(-250,0)
game_over.hideturtle()





#keyboard
screen.listen()
screen.onkeypress(Player.turn_right, "Right")
screen.onkeypress(Player.turn_left, "Left")	
screen.onkeypress(Player.accelerate, "Up")
screen.onkeypress(Player.d_accelerate, "Down")	
screen.onkeypress(Bomb.fire, "space")

# Player	
player=Player("triangle","royalblue",0,0)

# Aliens
aliens=[]
for i in range(4):
	aliens.append(Alien("turtle","red",-100,0))


# Bomb
bomb=Bomb("triangle","yellow",0,0)

#  TEAM players
teams=[]
for j in range(6):
	teams.append(Team("square","white",100,0))
particles=[]

for n in range(40):
	particles.append(particle("circle","orange",0 ,0))
while True:
	
	screen.update()
	# initialing  movements
	player.move()
	bomb.fire()
	bomb.launched()
	
	x=powerup.xcor()
	x+=powerup.speed
	powerup.setx(x)
	
	if powerup.xcor()>500:
		x=powerup.xcor()
		x = 500	
		powerup.setx(x)	
		
	
	
	for alien in aliens:
		alien.move()
		if bomb.explode(alien):
			x = random.randint(-500,800)
			y = random.randint(-790,800)
			alien.goto(x,y)
			
			score+=10
			pen.clear()
			pen.write('score:'+str(score),font=("arial",14,"italic"))
			bomb.status="ready"
			for particle in particles:
				particle.explosion(bomb.xcor(),bomb.ycor())
				
			
		if player.explode(alien):
			x = random.randint(-500,800)
			y = random.randint(-790,800)
			alien.goto(x,y)
			score-=10
			pen.clear()
			pen.write('score:'+str(score),font=("arial",14,"italic"))
			x=powerlow.xcor()
			x+=powerlow.speed
			powerlow.setx(x)
					
	for players in teams:
		players.move()
		
	if powerlow.xcor()>480:
		game_over.write('''GAME
OVER''',font=("arial",29,"italic bold"))
		player.goto(0,90000)
		bomb.hideturtle()
		
	for particle in particles:
		particle.move()
		
		
	
screen.mainloop()