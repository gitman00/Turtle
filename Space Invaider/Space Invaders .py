import turtle as T
import math
import random

#creating window
wn=T.Screen()
wn.title('space warrior')
wn.setup(width=800,height=800)
wn.bgcolor('white')
wn.bgpic('bgpic.gif')
wn.tracer(0)

# Player image
wn.register_shape("player.gif")

# Enemies image
wn.register_shape("enemies.gif")

# Enemies image


# GAME LOGO
wn.register_shape("bgpic.gif")

# GAME BODY
def game_body():
	
	wn.update()
	#creating player
	player=T.Turtle()
	player.speed(0)
	player.shape("player.gif")
	player.left(90)
	player.shapesize(5)
	player.penup()
	player.setposition(0,-800)
	player.color('#FFF0FF')
	player.direction="stop"
	player_speed=2
	
	
		#enemy
	number_of_enemies=20
	enemies=[]
			

	for i in range(number_of_enemies):
		enemies.append(T.Turtle())
		
	e_s_x_c=-300
	e_s_y_c=1000
	n_e=0
		
	for enemy in enemies:
		
		enemy.speed(0)
		enemy.shape("enemies.gif")
		enemy.rt(90)
		enemy.shapesize(8)
		enemy.penup()
		enemy.color('green')
		x=e_s_x_c + (200 * n_e )
		y=e_s_y_c
		enemy.goto(x,y)
		n_e += 1
		if n_e ==4:
			e_s_y_c -= 150
			n_e=0
		
			
		enemy_speed=2
	
	
	# Weapon
	Weapon=T.Turtle()
	Weapon.speed(11)
	Weapon.shape("triangle")
	Weapon.shapesize(2)
	Weapon.penup()
	Weapon.color('#FF0000')
	Weapon.setheading(90)
	Weapon.hideturtle()
	Weapon_speed=20
	Weapon_state="ready"
	
	
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
		if Weapon_state=="ready":
			x=player.xcor() + 5
			y=player.ycor() + 90
			Weapon.setposition(x,y)
			Weapon.showturtle()
			
			
	def isCollision(t1, t2):
		distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
		if distance < 70:
			return True
		else:
			return False
			
	
				
	# keyboard pressed
	wn.listen()
	wn.onkeypress(move_left, "l")
	wn.onkeypress(move_right, "r")
	wn.onkeypress(firing_weapon, "space")
	
	#score
	scores=0
	score=T.Turtle()
	score.speed(0)
	score.color('lightblue')
	score.penup()
	score.goto(-450,1000)
	score.hideturtle()
	score.write('score: 0',font=("airal",14,"bold"))
	#GAME LOOP#
	while True:
		for enemy in enemies:
		# moving enemy
			x=enemy.xcor()
			x += enemy_speed
			enemy.setx(x)
		
		# Moving all the enemy"
			if enemy.xcor() >450:
				for m in enemies:
					y=m.ycor()
					y -=  100
					m.sety(y)
				
			# moving enemies down
				enemy_speed *= -1
			
		
			if enemy.xcor() <-450:
				for m in enemies:
					y=m.ycor()
					y -=  100
					m.sety(y)
				
			# moving enemies down
				enemy_speed *= -1
			
	#	COLLISION PART
			if isCollision(Weapon, enemy):
				Weapon.hideturtle()
				Weapon_state = "ready"
				Weapon.setposition(0, -400)
				scores += 10
				score.clear()
				score.write('Score:'+str(scores),font=("airal",14,"italic bold"))
			#Reset the enemy
				x=e_s_x_c + (200 * n_e )
				y=e_s_y_c
				enemy.setposition(x, y)
		
			
			if isCollision(player, enemy):
				player.hideturtle()
				enemy.hideturtle()
				print ("Game Over")
				break
				
		
		
        # WEAPON FIRING
		if Weapon_state=="ready":
			y=Weapon.ycor()
			y += Weapon_speed
			Weapon.sety(y)
			
			
		
		move()
		firing_weapon()
		
		
		wn.update()
		
		# Updating display
		


# Loading turtle-part 1
Loading=T.Turtle()
Loading.speed(0)
Loading.color("#000000")
Loading.shapesize(5)
Loading.penup()
Loading.goto(0,-300)
Loading.write('Loading........',align="center",font=('arial',14,"italic"))
Loading.penup()

Loading.hideturtle()

# Loading turtle-part 2
L_turtle=T.Turtle()
L_turtle.speed(0)
L_turtle.color("red")
L_turtle.shape("classic")
L_turtle.pensize(25)
L_turtle.shapesize(2)
L_turtle.penup()
L_turtle.goto(-500,-350)
L_turtle.pendown()
L_turtle.hideturtle()
L_turtle_speed=1

	
while True:
	wn.update()
	x=L_turtle.xcor()
	x += L_turtle_speed
	L_turtle.setx(x)
	
	
	
	if L_turtle.xcor()>500:
		L_turtle.clear()
		Loading.clear()
		wn.bgcolor("black")
		wn.bgpic("tenor.gif")
		game_body()
		
wn.mainloop()
