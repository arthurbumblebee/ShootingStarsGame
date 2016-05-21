# Arthur Yawe Makumbi	
# Fall 2015
# CS 151 Project 10
#
# putt-putt golf

# import necessary modules
import graphics as gr
import physics_objects as pho
import collision as coll
import time
import math

# build the obstacle course
def buildGame(win, x0, y0, height, width):
	
# obstacles: floors, left, right, blocks
	awkwardBLock = pho.Block(win, x0+40, y0+14, height+3, width+10, coloring = 'brown')
	floor_left = pho.Block(win, x0+0, y0+10, height+35, width+3, coloring = 'green')
	floor_right = pho.Block(win, x0+40, y0+10, height+20, width+3, coloring = 'green')
	left = pho.Wall(win, x0+2, y0+10, height+70, width+3, coloring = 'DarkBlue')
	right = pho.Wall(win, x0+48, y0+10, height+70, width+3, coloring = 'DarkBlue')
	block1 = pho.Block(win, x0+15, y0+25, height+3, width+3, coloring = 'brown')
	block2 = pho.Block(win, x0+35, y0+25, height+3, width+3, coloring = 'brown')
	block3 = pho.Block(win, x0+25, y0+25, height+3, width+3, coloring = 'brown')
	top_left = pho.Block(win, x0+0, y0+58, height+35, width+3, coloring = 'brown')
	top_right = pho.Block(win, x0+40, y0+58, height+20, width+3, coloring = 'brown')
 	ball3 = pho.Ball( win, x0+45, y0+56, radius = 3,coloring = 'DarkGoldenrod4' )
 	ball4 = pho.Ball( win, x0+5, y0+55, radius = 3.3,coloring = 'DarkGoldenrod4' )	
	obstacles = [ ball3, ball4, floor_right,block2, floor_left, top_right, top_left, block1, block3, right, left,
					 awkwardBLock]
	for obstacle in obstacles:
		obstacle.draw()
		obstacle.setElasticity(1.01)
	return obstacles

# launch the ball into the scene
def launch( ball, x0, y0, dx, dy, forceMag ):

	d = math.sqrt(dx*dx + dy*dy)
	dx /= d
	dy /= d

	fx = dx * forceMag
	fy = dy * forceMag

	ball.setElasticity( 0.95 )
	ball.setPosition( (x0, y0) )
	ball.setForce( (fx, fy) )

	for i in range(5):
		ball.update(0.02)

	ball.setForce( (0., 0.) )
	ball.setAcceleration( (0., -1.) )

# main code
def main():
# create a GraphWin
	win = gr.GraphWin( "Golf", 500, 600, False)
	win.setBackground('alice blue')
# Assign to obstacles the result of calling buildGame
	obstacles = buildGame(win , 0, 0, 0, 0)
#make launchpad
	launchpad = pho.Triangle(win, 41, 11, 5, 5, coloring = 'orange')
	launchpad.draw()
# Make a Ball object, draw it
	ball = pho.Ball( win, 43, 9.5 )	
	ball.draw()
	
# make rotating blocks
	block = pho.RotatingBlock(win, 40, 45, 3, 7 )
	block1 = pho.RotatingBlock(win, 10, 30, 3, 7 )
	block.draw()
	block1.draw()
# make paddles
	left_paddle = pho.RotatingBlock(win, 19, 8.5, 6.8, 2 )
	left_paddle.setAngle(315)
	right_paddle =	pho.RotatingBlock(win, 29, 8.5, 6.8, 2 )	
	right_paddle.setAngle(45)
	paddles = [left_paddle, right_paddle]	
	for paddle in paddles:
		paddle.draw()
		obstacles.append(paddle)
	dt = 0.03
# start after clicking mouse	
	win.getMouse()	
# assign to frame the value 0
	frame = 0
	while win.checkMouse() == None:
		block.setRotVelocity(200)
		block.update(dt)
		obstacles.append(block)
		block1.setRotVelocity(200)
		block1.update(dt)
		obstacles.append(block1)
		collided = False
		for item in obstacles:
	# if the result of calling the collision function with the ball and the item is True
			if coll.collision( ball, item, dt ) == True:
				collided == True
		if collided == False:
			ball.update(dt)
	# user input to allow interaction
		n = win.checkKey()
		if n == "space":
			print n
			left_paddle.setRotVelocity(400)
			right_paddle.setRotVelocity(-400)			
		if left_paddle.angle > 360:
			left_paddle.setAngle(360)
			left_paddle.setRotVelocity(-300)
		if left_paddle.angle < 315:
			left_paddle.setRotVelocity(0)
			left_paddle.setAngle(315)
		if right_paddle.angle < 0:
			right_paddle.setAngle(0)
			right_paddle.setRotVelocity(300)
		if right_paddle.angle > 45:
			right_paddle.setRotVelocity(0)
			right_paddle.setAngle(45)
		left_paddle.update(dt)
		right_paddle.update(dt)
		p = ball.getPosition()
	# if the ball is out of the window, user launches it
		if p[1] < 10 or p[1]>60 or p[0]<0 or p[0]>50:
			if n == "0":			
				ball.setVelocity([-3,5])
				launch(ball,43, 13, 5, 15, 250)	
		if n == "period":
			ball.setVelocity([0,0])
			ball.setPosition([43,9])
			ball.update(dt)
# check which key		
#		m = win.getKey()
#		print m
		if frame % 10 == 0:
			win.update()
			time.sleep(0.01)
		frame += 1
		
	# wait for a mouse click, then close the window
	win.getMouse()
	win.close()
	
	
if __name__ == "__main__":
	main()
