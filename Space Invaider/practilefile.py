import turtle as T
import math
import random

#creating window
wn=T.Screen()

wn.title('space warrior')
wn.setup(width=800,height=800)
wn.bgcolor('black')


#creating player
player=T.Turtle()
player.speed(0)
player.shape("triangle")
player.left(90)
player.shapesize(5)
player.penup()
player.setposition(0,-800)
player.color('#F0FFFF')
player.direction="right"

#enemy
number_of_enemies=2
enemies=[]		

for i in range(number_of_enemies):
	enemies.append(T.Turtle())
	
for enemy in enemies:
	enemy.speed(0)
	enemy.shape("classic")
	enemy.rt(90)
	enemy.shapesize(8)
	enemy.penup()
	enemy.color('green')
	x=random.randrange(-200,200)
	y=random.randrange(220,250)
	enemy.goto(x,y)
enemy_speed=10

# Weapon
Weapon=T.Turtle()
Weapon.speed(11)
Weapon.shape("triangle")
Weapon.shapesize(2)
Weapon.penup()
Weapon.color('#00FFFF')
Weapon.setheading(90)
Weapon.hideturtle()
Weapon_speed=20

Weapon_state="ready"

pen=T.Turtle()
#functions
	
def move_right():
	player.direction="right"
def move_left():
	player.direction="left"
	
def move():
		
	if player.direction=="left":
		x = player.xcor()
		player.setx(x - 20)
		
	if player.direction=="right":
		x = player.xcor()
		player.setx(x + 20)

def firing_weapon():
	global Weapon_state
	if Weapon_state == "ready":
		x=player.xcor()
		y=player.ycor() + 50
		Weapon.setposition(x,y)
		Weapon.showturtle()

def enemy_roasted(T,T1):
	Distance=math.sqrt(math.pow(T.xcor()-T1.xcor(),2) + math.pow(T.ycor()-T1.ycor(),2))
	if Distance < 15:
		return True
	else:
		return False
			
#keyboard pressed
wn.listen()
wn.onkeypress(move_left, "l")
wn.onkeypress(move_right, "r")
wn.onkeypress(firing_weapon, "space")
#GAME LOOP
while True:
	wn.update()
	for enemy in enemies:
		# moving enemy
		x=enemy.xcor()
		x += enemy_speed
		enemy.setx(x)
	
		if enemy.xcor() >500:
			y=enemy.ycor()
			y -=  100
			enemy_speed *= -1
			enemy.sety(y)
		
		if enemy.xcor() <-500:
			y=enemy.ycor()
			y -=  100
			enemy_speed *= -1
			enemy.sety(y)
		
		# WEAPON FIRING
	if Weapon_state=="ready":
		y=Weapon.ycor()
		y += Weapon_speed
		Weapon.sety(y)
			
	#	COLLISION PART
	if enemy_roasted(Weapon, enemy):
		Weapon.hideturtle()
		Weapon.goto(0,-400)
		enemy.goto(-500,1000)
		
	if enemy_roasted(player, enemy):
		player.goto(0,1500)
		enemy.goto(0,1500)
		
	
wn.mainloop()
