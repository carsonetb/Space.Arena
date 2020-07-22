# Space Arena
# Python 3.x Compatible
# Windows, MacOSX, and Linux Compatible
# by Carson Bates

import turtle

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

wn =turtle.Screen()
wn.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
wn.title("Space Arena - Game")
wn.bgcolor("black")
wn.tracer(0)

pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()

class Sprite():
	def __init__(self, x, y, shape, color):
		self.x = x
		self.y = y
		self.shape = shape
		self.color = color
		self.dx = 0
		self.dy = 0

	def update(self):
		self.x += self.dx
		self.y += self.dy

	def render(self, pen):
		pen.goto(self.x, self.y)
		pen.shape(self.shape)
		pen.color(self.color)
		pen.stamp()

class Player(Sprite):
	def __init__(self, x, y, shape, color):
		Sprite.__init__(self, 0, 0, shape, color)
		self.lives = 3
		self.score = 0
		self.heading = 90
		self.da = 0

	def update(self):
		self.x += self.dx
		self.y += self.dy
		self.heading += self.da

	def render(self, pen):
		pen.goto(self.x, self.y)
		pen.setheading(self.heading)
		pen.shape(self.shape)
		pen.color(self.color)
		pen.stamp()

# Create player sprite
player = Player(0, 0, "triangle", "white")
player.dx = 0.1

enemy = Sprite(0, 100, "square", "red")
enemy.dx = -0.1

powerup = Sprite(0, -100, "circle", "blue")
powerup.dy = 0.1

# Sprites list
sprites = []
sprites.append(player)
sprites.append(enemy)
sprites.append(powerup)

# Main Loop
while True:
	# Clear screen
	pen.clear()

	# Do game stuff
	# Render sprites
	for sprite in sprites:
		sprite.update()

	# Update sprites
	for sprite in sprites:
		sprite.render(pen)

	# Update the screen
	wn.update()
