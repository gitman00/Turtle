import pygame as py
import sys 
import random
import math

py.init()

WIDTH, HEIGHT, GRAVITY= 1100, 2000, 1
screen=py.display.set_mode((WIDTH, HEIGHT))
clock=py.time.Clock()


BLACK=((0,0,0))
WHITE=((255,255,255))
GREEN=((0,255,0))
BLUE=((0,0,255))
RED=((255,0,0))


class Sprite():
	def __init__(self,x, y, width, height):
		self.x=x
		self.y=y
		self.dx=0
		self.dy=0
		self.width=width
		self.height=height
		self.color=WHITE
		self.friction=0.9
		
	def goto(self, x, y):
		self.x=x
		self.y=y
		
	def render(self,camera):
		py.draw.rect(screen,self.color,(int(self.x-self.width/2.0-camera.x+WIDTH/2.0),int(self.y-self.height/2.0-camera.y+HEIGHT/2.0),self.width,self.height))
		
	
		
	def is_collision(self, other):
		x_collision=(math.fabs(self.x-other.x)*2) <(self.width + other.width)
		y_collision=(math.fabs(self.y-other.y)*2) <(self.height + other.height)
		return(x_collision and y_collision)
		
class Player(Sprite):
	def __init__(self,x, y, width, height):
		Sprite.__init__(self,x, y, width, height)
		self.color=GREEN
		
	def move(self):
		self.x += self.dx
		self.y += self.dy
		self.dy += GRAVITY
		
	def jump(self):
		self.dy -= 30
		
	def left(self):
		self.dx -= 5
		if self.dx < -10:
			self.dx=10
		
	def right(self):
		self.dx += 5
		if self.dx > 10:
			self.dx=10
		
class Camera():
	def __init__(self,side):
		self.x=side.x
		self.y=side.y
		
	def update(self,side):
		self.x=side.x
		self.y=side.y	
				
player=Player(500,0,40,100)

camera=Camera(player)

blocks=[]
blocks.append(Sprite(500,200,200,20))
blocks.append(Sprite(200,400,200,20))
blocks.append(Sprite(400,600,200,20))
blocks.append(Sprite(700,700,200,20))
blocks.append(Sprite(500,1180,800,40))
blocks.append(Sprite(950,1050,200,300))
blocks.append(Sprite(100,1050,200,300))


		
while True:
		screen.fill((BLACK))
		
		for event in py.event.get():
			if event.type==py.QUIT:
				sys.exit()
			if event.type==py.KEYDOWN:
				if event.key == py.K_l:
					player.left()
				elif event.key==py.K_r:
					player.right()
				elif event.key==py.K_SPACE:
					for block in blocks:
						if player.is_collision(block):
							player.jump()
							break
			
		
		# Moving the player
		player.move()
		camera.update(player)
		
		# DIsplaying blocks and collision
		for block in blocks:
			if player.is_collision(block):
				
				if player.x < block.x - block.width/2.0 and player.dx > 0:
					player.dx=0
					player.x=block.x-block.width/2.0-player.width/2.0
					
				elif player.x > block.x + block.width/2.0 and player.dx < 0:
					player.dx=0
					player.x=block.x+block.width/2.0+player.width/2.0
					
				elif player.y < block.y:
					player.dy=0
					player.y=block.y-block.height/2.0-player.height/2.0 + 1
					player.dx *= block.friction
				elif player.y > block.y:
					player.dy=0
					player.y=block.y+block.height/2.0+player.height/2.0
				
		# render the blocks
		for block in blocks:
			block.render(camera)
			
		# render the player
		player.render(camera)
		
		if player.y > 2000:
			player.goto(500,0)
			
		
		# updating the window
		py.display.flip()
		
		clock.tick(60)