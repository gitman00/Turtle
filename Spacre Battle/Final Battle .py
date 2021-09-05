import turtle as t
import math
import pygame
from pygame import mixer
import random
import time
pygame.init()

display_width,display_height=1000,1000

game_display=t.Screen()
game_display.setup(display_width,display_height)
game_display.title("Space Battle")
game_display.bgcolor("black")
#game_display.tracer(0)




def Game():
	
	display_width,display_height=1000,1000

	game_display=t.Screen()
	game_display.setup(display_width,display_height)
	game_display.title("Space Battle")
	game_display.bgcolor("black")
	
	t.register_shape("normal.gif")
	t.register_shape("destroyer.gif")
	t.register_shape("powerup.gif")
	
	pens=t.Turtle()
	pens.speed(0)
	pens.color("navy")
	pens.shape("turtle")
	pens.penup()
	pens.hideturtle()

	#mixer.music.load('space.mp3')
#	mixer.music.play(-1)
	
	
	class Game_part():
		def __init__(self, width, height):
			self.width=width
			self.height=height
			self.level=1
			
		def start_level(self):
			sprites.clear()
			
			# creating player
			sprites.append(player)
			
			# creating weapon
			for weapon in weapons:
				sprites.append(weapon)
			
			for _ in range(self.level):
				x=random.randint(-self.width/2,self.width/2)
				y=random.randint(-self.height/2,self.height/2)
				dx=random.randint(-2,2)
				dy=random.randint(-2,-2)
				sprites.append(Enemy(x,y,"red","circle"))
				sprites[-1].dx=dx
				sprites[-1].dy=dy
				
			for _ in range(self.level):
				x=random.randint(-self.width/2,self.width/2)
				y=random.randint(-self.height/2,self.height/2)
				dx=random.randint(-2,2)
				dy=random.randint(-2,-2)
				sprites.append(Powerup(x,y,"blue","powerup.gif"))
				sprites[-1].dx=dx
				sprites[-1].dy=dy
		
		def render_border(self, pens, x_offset, y_offset):
			pens.color('red')
			pens.width(3)
			pens.penup()
		
			left=-self.width/2.0 - x_offset
			right=self.width/2.0 - x_offset
			top=self.height/2.0 - y_offset
			bottom=-self.height/2.0 - y_offset
		
			pens.goto(left, top)
			pens.pendown()
			pens.goto(right, top)
			pens.goto(right, bottom)
			pens.goto(left, bottom)
			pens.goto(left, top)
			pens.penup()
			
		def render_info(self, pens, score, living_enemies=0):
			pens.color('black')
			pens.penup()
			pens.goto(-500,-900)
			pens.shape("square")
			pens.setheading(0)
			pens.shapesize(35,110)
			pens.penup()
			pens.stamp()
			
			pens.color("white")
			
			pens.goto(-540,-550)
			pens.penup()
			pens.pendown()
			pens.goto(540,-550)
			
			pens.penup()
			pens.color("green")
			text.scale=3
			text.write_words(pens ,"FINAL BATTLE", 0, -610)
			text.write_words(pens ,"Score {}".format(player.score), -350, -710)
			text.write_words(pens ,"Enemy {}".format(living_enemies), -350, -810)
			text.write_words(pens ,"Lives {}".format(player.lives), -350, -910)
			text.write_words(pens ,"Level {}".format(border.level), -350, -1010)
			
	
	class text_pen():
			def  __init__(self, color, scale):
					self.color=color
					self.scale=scale
					
					
					self.characters = {}
					self.characters["1"] = ((-5, 10), (0, 10), (0, -10), (-5, -10), (5, -10))
					self.characters["2"] = ((-5, 10),(5, 10),(5, 0), (-5, 0), (-5, -10), (5, -10))
					self.characters["3"] = ((-5, 10),(5, 10),(5, 0), (0, 0), (5, 0), (5,-10), (-5, -10))
					self.characters["4"] = ((-5, 10), (-5, 0), (5, 0), (2,0), (2, 5), (2, -10))
					self.characters["5"] = ((5, 10), (-5, 10), (-5, 0), (5,0), (5,-10), (-5, -10))
					self.characters["6"] = ((5, 10), (-5, 10), (-5, -10), (5, -10), (5, 0), (-5, 0))
					self.characters["7"] = ((-5, 10), (5, 10), (0, -10))
					self.characters["8"] = ((-5, 0), (5, 0), (5, 10), (-5, 10), (-5, -10), (5, -10), (5, 0))
					self.characters["9"] = ((5, -10), (5, 10), (-5, 10), (-5, 0), (5, 0))
					self.characters["0"] = ((-5, 10), (5, 10), (5, -10), (-5, -10), (-5, 10))
					self.characters["A"] = ((-5, -10), (-5, 10), (5, 10), (5, -10), (5, 0), (-5, 0))
					self.characters["B"] = ((-5, -10), (-5, 10), (3, 10), (3, 0), (-5, 0), (5,0), (5, -10), (-5, -10))
					self.characters["C"] = ((5, 10), (-5, 10), (-5, -10), (5, -10))
					self.characters["D"] = ((-5, 10), (-5, -10), (5, -8), (5, 8), (-5, 10))
					self.characters["E"] = ((5, 10), (-5, 10), (-5, 0), (0, 0), (-5, 0), (-5, -10), (5, -10))
					self.characters["F"] = ((5, 10), (-5, 10), (-5, 0), (5, 0), (-5, 0), (-5, -10))
					self.characters["G"] = ((5, 10), (-5, 10), (-5, -10), (5, -10), (5, 0), (0, 0))
					self.characters["H"] = ((-5, 10), (-5, -10), (-5, 0), (5, 0), (5, 10), (5, -10))
					self.characters["I"] = ((-5, 10), (5, 10), (0, 10), (0, -10), (-5, -10), (5, -10))
					self.characters["J"] = ((5, 10), (5, -10), (-5, -10), (-5, 0))   
					self.characters["K"] = ((-5, 10), (-5, -10), (-5, 0), (5, 10), (-5, 0), (5, -10))
					self.characters["L"] = ((-5, 10), (-5, -10), (5, -10))
					self.characters["M"] = ((-5, -10), (-3, 10), (0, 0), (3, 10), (5, -10))
					self.characters["N"] = ((-5, -10), (-5, 10), (5, -10), (5, 10))
					self.characters["O"] = ((-5, 10), (5, 10), (5, -10), (-5, -10), (-5, 10))
					self.characters["P"] = ((-5, -10), (-5, 10), (5, 10), (5, 0), (-5, 0))
					self.characters["Q"] = ((5, -10), (-5, -10), (-5, 10), (5, 10), (5, -10), (2, -7), (6, -11))
					self.characters["R"] = ((-5, -10), (-5, 10), (5, 10), (5, 0), (-5, 0), (5, -10))
					self.characters["S"] = ((5, 8), (5, 10), (-5, 10), (-5, 0), (5, 0), (5, -10), (-5, -10), (-5, -8))
					self.characters["T"] = ((-5, 10), (5, 10), (0, 10), (0, -10)) 
					self.characters["V"] = ((-5, 10), (0, -10), (5, 10)) 
					self.characters["U"] = ((-5, 10), (-5, -10), (5, -10), (5, 10)) 
					self.characters["W"] = ((-5, 10), (-3, -10), (0, 0), (3, -10), (5, 10))  
					self.characters["X"] = ((-5, 10), (5, -10), (0, 0), (-5, -10), (5, 10))
					self.characters["Y"] = ((-5, 10), (0, 0), (5, 10), (0,0), (0, -10))   
					self.characters["Z"] = ((-5, 10), (5, 10), (-5, -10), (5, -10))
					self.characters["="] = ((0,10),(0,10))
					
			def write_words(self,pens, words, x, y):
					pens.width(10)
					pens.color("#00FFFF")
					
					x -= 15 * self.scale * ((len(words) -1 ) / 2)
					for character in words:
						self.draw_text(pens, character, x, y)
						x += 15 * self.scale
					
			def draw_text(self, pens, character, x, y):
			     scale=self.scale
			     if character in "abcdefghijklmnopqrstuvwxyz":
			     	scale *= 1
			     	pens.width(5)
			     	
			     character=character.upper()
			     if character in self.characters:
			     	pens.penup()
			     	xy=self.characters[character][0]
			     	pens.goto(x + xy[0] * scale, y + xy[1] * scale)
			     	pens.pendown()
			     	for i in range(1, len(self.characters[character])):
			     		xy=self.characters[character][i]
			     		pens.goto(x + xy[0] * scale, y + xy[1] * scale)
			     	pens.penup()
			     	
			     	
	
	
	text=text_pen("#00FFFF",3.0)
	text.scale=5.5
	text.write_words(pens,"FINAL BATTLE",0,400)   
	
	text.scale=2
	text.write_words(pens,"by @Manish ghimire",0,280)   
	
	pens.color("white")
	pens.shapesize(2)
	pens.goto(-400,0)
	pens.shape("triangle")
	pens.stamp()
	text.write_words(pens,"Player",-400,-50)
	
	pens.color("red")
	pens.shapesize(2)
	pens.goto(0,0)
	pens.shape("square")
	pens.stamp()
	text.write_words(pens,"Enemy",0,-50)
	
	pens.color("blue")
	pens.shapesize(2)
	pens.goto(400,0)
	pens.shape("circle")
	pens.stamp()
	text.write_words(pens,"Powerup",400,-50)    
	text.scale=2.5
	text.write_words(pens,"up arrow",-250,-250)    
	text.write_words(pens,"accelerate",290,-250)
	
	text.write_words(pens,"Right Arrow",-250,-350)    
	text.write_words(pens,"rotate right",290,-350)
	             
	text.write_words(pens,"Left Arrow",-250,-450)    
	text.write_words(pens,"rotate left",290,-450)
	
	text.write_words(pens,"Space",-250,-550)    
	text.write_words(pens,"fire",290,-550)
	
	text.write_words(pens,"starting game  in 3 seconds ",0,-850)
	      
	time.sleep(3)
	
	game_display.tracer(0)
	class Sprite():
		def __init__(self, x, y, color, shape):
			self.x= x
			self.y= y
			self.color= color
			self.shape= shape
			self.dx=0
			self.dy=0
			self.heading=0
			self.da=0
			self.thrust=0.0
			self.acceleration=0.002
			self.health=100
			self.max_health=100
			self.width=40
			self.height=40
			self.state="living"
			self.radar= 500
			self.max_dx=5
			self.max_dy=5
		
		def update(self):
			self.heading += self.da
			self.heading %=360
		
			self.dx += math.cos(math.radians(self.heading)) * self.thrust
			self.dy += math.sin(math.radians(self.heading)) * self.thrust
			self.x += self.dx
			self.y += self.dy
			
			self.border_check()
			
		def bounce(self, other):
			temp_dx=self.dx
			temp_dy=self.dy
			
			self.dx=other.dx
			self.dy=other.dy
			
			other.dx=temp_dx
			other.dy=temp_dy
			
		def is_collision(self, other):
			if self.x < other.x + other.width and\
				self.x + self.width > other.x and\
				self.y < other.y + other.height and\
				self.y + self.height > other.y:
				return True
			else:
				return False
				
		def border_check(self):
			if self.x > border.width/2.0-20:
				self.x =border.width/2.0-20
				self.dx *= -1
				self.da=1.5
				player.deaccelerate()
				
			
			if self.x < -border.width/2.0+20:
				self.x =-border.width/2.0+20
				self.dx *= -1
				self.da=1.5
				player.deaccelerate()
				
			if self.y > border.height/2.0-20:
				self.y =border.height/2.0-20
				self.dy *= -1
				self.da=1.5
				player.deaccelerate()

			
			if self.y < -border.height/2.0+40:
				self.y =-border.height/2.0+40
				self.dy *= -1
				self.da=1.5
				player.deaccelerate()
		
		def render(self, pens, x_offset, y_offset):
			if self.state=="living":
				pens.goto(self.x - x_offset, self.y - y_offset)
				pens.setheading(self.heading)
				pens.color(self.color)
				pens.shape(self.shape)
				pens.stamp()
				self.render_health_meter(pens, x_offset, y_offset)
		
		
		def render_health_meter(self, pens, x_offset, y_offset):
			# Draw a power meter
			pens.goto(self.x - x_offset- 20, self.y - y_offset +50)
			pens.width(6)
			pens.pendown()
			pens.setheading(0)
		
			if self.health/self.max_health < 0.3: 
				pens.color("red")
			elif self.health/self.max_health < 0.7:
				pens.color("yellow")
			else:
				pens.color("green")
			
			pens.fd(40 * (self.health/self.max_health))
			pens.color("orange")
			pens.fd(40 * ((self.max_health-self.health)/self.max_health))
			pens.penup()
		
	class Player(Sprite):
			def __init__(self, x, y, shape, color):
				Sprite.__init__(self, x, y , shape, color)
				self.lives=3
				self.score=0
				self.heading=180
				self.da=0
				
				
			
			def rotate_left(self):
				self.da=1
			
			def rotate_right(self):
				self.da=-1
			
			def stop_rotation(self):
				self.da=0
			
			def accelerate(self):
				self.thrust += self.acceleration
			
			def deaccelerate(self):
				self.thrust=0
				
			def fire(self):
				for weapon in weapons:
					num_of_bullet = 0
					if weapon.state=="ready":
						num_of_bullet += 1
						
				for weapon in weapons:
					if num_of_bullet == 1:
						print("1")
						directions=[0,5,-5,]
						for weapon in weapons:
							 if weapon.state=="ready":
							 	weapon.fire(self.x, self.y, self.heading + directions.pop(), self.dx, self.dy)
						
					if num_of_bullet == 2:
						print("2")
						directions=[0,5,-5,]
						for weapon in weapons:
							if weapon.state=="ready":
								weapon.fire(self.x, self.y, self.heading + directions.pop(), self.dx, self.dy)
					
					if num_of_bullet == 3:
						print("3")
						directions=[0,5,-5,]
						for weapon in weapons:
							if weapon.state=="ready":
								weapon.fire(self.x, self.y, self.heading + directions.pop(), self.dx, self.dy)
						
				
				
			def update(self):
				if self.state=="living":
					self.heading += self.da
					self.heading %=360
		
					self.dx += math.cos(math.radians(self.heading)) * self.thrust
					self.dy += math.sin(math.radians(self.heading)) * self.thrust
					self.x += self.dx
					self.y += self.dy
			
					self.border_check()
				
				if self.health<=0:
					self.reset()
					
					
			def reset(self):
				self.x=200
				self.y=0
				self.health=self.max_health
				self.dx=0
				self.dy=0
				self.lives-= 1
					
			def render(self, pens, x_offset, y_offset):
				pens.shapesize(2,3,None)
				pens.goto(self.x - x_offset, self.y - y_offset)
				pens.setheading(self.heading)
				pens.color(self.color)
				pens.shape(self.shape)
				pens.stamp()
				pens.shapesize(1.5,1.5,None)
			
				self.render_health_meter(pens, x_offset, y_offset)
				
	class Missile(Sprite):
			def __init__(self, x, y, shape, color):
				Sprite.__init__(self, x, y , shape, color)
				self.state="ready"
				self.thrust=30
				self.max_fuel=350
				self.fuel=self.max_fuel
				self.height=5
				self.width=5
				
				
			def fire(self, x, y, heading, dx, dy):
				if self.state=="ready":
					self.state="active"
					self.x=x
					self.y=y
					self.heading=heading
					self.dx=dx
					self.dy=dy
					self.dx += math.cos(math.radians(self.heading)) * self.thrust
					self.dy += math.sin(math.radians(self.heading)) * self.thrust
				
				
			def update(self):
				if self.state=="active": 
					self.fuel-=self.thrust
					if self.fuel<=0:
						self.reset()
						
					self.heading += self.da
					self.heading %=360
					self.x += self.dx
					self.y += self.dy
					
					self.border_check()	
				
			def render(self, pens, x_offset, y_offset):
				if self.state=="active":
					pens.shapesize(0.9,0.9,None)
					pens.goto(self.x - x_offset, self.y - y_offset)
					pens.setheading(self.heading)
					pens.color(self.color)
					pens.shape(self.shape)
					pens.stamp()
					pens.shapesize(1.5,1.5,None)
					
			def reset(self):
				self.fuel=self.max_fuel
				self.dx=0
				self.dy=0
				self.state="ready"
				
	class Enemy(Sprite):
			def __init__(self, x, y, shape, color):
				Sprite.__init__(self, x, y , shape, color)
				self.max_health=40
				self.health=self.max_health
				self.type=random.choice(["Normal", "Hunter", "Destroyer"])
				
				if self.type=="Normal":
					self.color="lightgreen"
					self.shape="normal.gif"
					
				if self.type=="Hunter":
					self.color="orangered"
					self.shape="circle"
					
				if self.type=="Destroyer":
					self.color="red"
					self.shape="destroyer.gif"		
					
				
			def update(self):
				if self.state=="living":
					self.heading += self.da
					self.heading %=360
		
					self.dx += math.cos(math.radians(self.heading)) * self.thrust
					self.dy += math.sin(math.radians(self.heading)) * self.thrust
				self.x += self.dx
				self.y += self.dy
			
				self.border_check()
				
				if self.type=="Normal":
					if self.x < player.x:
						self.dx += 0.5	
					else:
						self.dx -= 0.5
					if self.y < player.y:
						self.dy -= 0.5
					else:
						self.dy += 0.5
						
				elif self.type=="Hunter":
					self.dx=0
					self.dy=0
					
				elif self.type=="Destroyer":
					if self.x > player.x:
						self.dx -= 0.5	
					else:
						self.dx -= 0.5
					if self.y > player.y:
						self.dy -= 0.5
					else:
						self.dy += 0.5
						
						
				if self.dx > self.max_dx:
					self.dx=self.max_dx
				elif self.dx < -self.max_dx:
					self.dx=-self.max_dx
					
				if self.dy > self.max_dy:
					self.dy=self.max_dy
				elif self.dy < -self.max_dy:
					self.dy=-self.max_dy
				
				if self.health<=0:
					self.reset()
					
			def reset(self):
				self.state="dead"
				
				
			 
	class Powerup(Sprite):
			def __init__(self, x, y, shape, color):
				Sprite.__init__(self, x, y , shape, color)
				
	class Camera():
			def __init__(self, x, y):
				self.x=x
				self.y=y
				
			def update(self, x, y):
				self.x=x
				self.y=y
				
	class Radar():
			def __init__(self, x, y, width, height):
				self.x=x
				self.y=y
				self.width=width
				self.height=height
				
			def render(self, pens, sprites):
				# drawing the rader
				pens.color("white")
				pens.setheading(90)
				pens.goto(self.x + self.width/ 2.0, self.y)
				pens.pendown()
				pens.circle(self.width/2.0)
				pens.penup()
				
				
				for sprite in sprites:
					if sprite.state=="living":
						radar_x=self.x + (sprite.x - player.x) * (self.width/border.width)
						radar_y=self.y + (sprite.y - player.y) * (self.height/border.height)
						pens.goto(radar_x, radar_y)
						pens.color(sprite.color)
						pens.shape(sprite.shape)
						pens.shapesize(0.3,0.3,None)
						distance=((player.x - sprite.x)**2 + (player.y - sprite.y)**2)**0.5
						if distance < player.radar:
							pens.stamp()
						

	# creating border
	border=Game_part(1500,1500)	
	
	text=text_pen("green", 10.0)
	
	#drawing radar
	radar=Radar(330,-890,380,380)
	# Creating Player
	player=Player(200,0,"white","triangle")
	
	camera=Camera(player.x, player.y)
	
	#multiple weapons
	weapons=[]
	for _ in range(3):
		weapons.append(Missile(0,-500,"yellow","classic"))
	
	sprites=[]
	
	border.start_level()
	
	
	# key pressed
	game_display.onkeypress(player.rotate_left, "Left")	
	game_display.onkeypress(player.rotate_left, "Right")
	game_display.onkeypress(player.accelerate, "Up")
	game_display.onkeypress(player.fire, "space")

	# key rekeased	
	game_display.onkeyrelease(player.stop_rotation, "Left")	
	game_display.onkeyrelease(player.stop_rotation, "Right")
	game_display.onkeyrelease(player.deaccelerate, "Up")
	
	# Game Main Loop
	while True:
		pens.clear()
		player.accelerate()
		player.fire()
		
		
		
		
	# Updating the sprites
		for sprite in sprites:
			sprite.update()
			
		for sprite in sprites:
			if isinstance(sprite, Enemy):
				if player.is_collision(sprite) and sprite.state=="living":
					sprite.health -= 10
					player.health-= 10
					player.bounce(sprite)
					
				for weapon in weapons:	
					if weapon.state=="active" and weapon.is_collision(sprite):
						sprite.health-=30
						weapon.reset()
				
			if isinstance(sprite, Powerup):
				if  player.is_collision(sprite):
					sprite.x=0
					sprite.y=200
					
				for weapon in weapons:	
					if weapon.state=="active" and weapon.is_collision(sprite):
						sprite.x=20
						sprite.y=500
						weapon.reset()
			
	
	
	# Render the sprites
		for sprite in sprites:
			sprite.render(pens, camera.x  , camera.y)
			
		border.render_border(pens, camera.x  , camera.y)
		
		end_of_level=True
		for sprite in sprites:
			if isinstance(sprite, Enemy) and sprite.state=="living":
				end_of_level=False
			
		if end_of_level:
			border.level+=1
			border.start_level()
			
		# updating the camera
		camera.update(player.x, player.y)
		
		#text.write_words(pens, "MANISH", 0,0)
		border.render_info(pens, 0, 0)
		radar.render(pens, sprites)
		
				
		
		# Updating game_display
		game_display.update()
		
			


    				     	
#Game()
Game()


