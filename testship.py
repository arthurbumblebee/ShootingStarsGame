# Arthur Yawe Makumbi	
# Fall 2015
# CS 151 Project 11
# testing the simple ship

# import useful packages
import math
import time
import graphics as gr
import random
import physics_objects as pho
import collision as coll


def main():
# variables 
	key = ''
	dt = 0.02
	frame = 0
	gamma = 100
	delta = 0.5	 
	winWidth = 50
	winHeight = 50 
	counter = 0
# start screen, ie state is 0
	# make a window
	win = gr.GraphWin('Galaxy Impact', 500, 500, False)
	win.setBackground("black")
	quit = False
	state = 0
	if state == 0:
		ship = pho.Ship(win, 8, 40)
		ship1 = pho.Ship(win, 43, 40)		
		ship.setRotVelocity(30)
		ship1.setRotVelocity(30)
		title = gr.Text(gr.Point(250, 100), "Galaxy Impact")
		title.setFill('red')
		title.setSize(36)
	# instruction to start text
		instruction = gr.Text(gr.Point(250, 200), "click start to begin")
		instruction.setFill('orangered')
		instruction.setSize(20)
		begin = pho.Block(win, 25, 25, 10, 6, coloring = 'indianred')
		begins = gr.Text(gr.Point(250, 250), "start")
		begins.setSize(15)
		close = pho.Block(win, 25, 15, 10, 6, coloring = 'indianred')
		closes = gr.Text(gr.Point(250, 350), "close")
		closes.setSize(15)
		instructions = gr.Text(gr.Point(250, 420), " INSTRUCTIONS: \n space to shoot \n up to go up \ left to go left, right to go right \n down to go down")
		instructions.setFill('red')
		starts = [closes,instruction, title, begins, instructions ]
		boxes = [begin, close, ship, ship1]
	# draw all the boxes
		for box in boxes:
			box.draw()
	# draw all the text
		for word in starts:
			word.draw(win)
#wait for a mouse click on start to start
		while True:
			ship.update(dt)
			ship1.update(dt)
			event = win.checkMouse()
			if event != None and event.x < 300 and event.x > 200 and event.y > 220 and event.y < 280:
				state = 1
				break
			elif event != None and event.x < 300 and event.x > 200 and event.y > 320 and event.y < 380:
				win.close()				
### main phase ie state is 1	  
# make ship, draw it, 
	ship = pho.Ship(win, 25, 5)
	bullet = pho.Ball(win, -10,-10)
	ship.setAngle(90)
	old_rotV = ship.getRotVelocity()
	gamma = 100
	delta = 0.5	 
	winWidth = 50
	winHeight = 50 
	bullets = []
	rains = []
	if state == 1:		
	# undraw all from start screen
		for word in starts:
			word.undraw()
	# undraw all the boxes
		for box in boxes:
			box.undraw()
		win.setBackground("gray6")
		# draw objects
		ship.draw()
		while state == 1: 
			#scores
			score = gr.Text(gr.Point(450, 50), "SCORE : %d" % counter)
			score.setSize(18)
			score.setFill("white")		
			key = win.checkKey()
		# raining
			rain = pho.Ball(win, random.randint(0,50),random.randint(45,50),radius = 1 )	
			rain.setVelocity([random.randint(-5,3),random.randint(-10,-5)])			
		# draw 	
			if frame % 50 == 0:
				rain.draw()
				rains.append(rain)
		# check for collisions
			collided = False
#			for item, go in zip(rains, bullets): #thought this could help double loop 
# if the bullet hits rain, undraw both ,and increment score
			for item in rains:	
				if coll.collision( item, bullet, dt ) == True:
					print "S"
					collided == True
					item.undraw()
					bullet.undraw()
# 					counter+=1
# 					score.undraw()
# 				#	win.update()
# 					score.draw(win)
		#	if collided == False:
				#rain.update(dt)
				#bullet.update(dt)
			for item in bullets:	
				if coll.collision( item, rain, dt ) == True:
					print "m"
					collided == True
					item.undraw()
					rain.undraw()
	# 				counter+=1
# 					score.undraw()
# 				#	win.update()
# 					score.draw(win)
			#if collided == False:
				#rain.update(dt)
				#bullet.update(dt)	
	# if rain hits spaceship, then you die
			for item in rains:
				z = item.getPosition()
			# scores if the rain doesnt touch, and goes down, not to the side :(	
				if z[1] < 0:
					counter += 1
				if coll.collision( item, ship, dt ) == True:
					collided == True
			# make ship red
					ship.vis[0].setFill("red")
					ship.setFlickerOn()
					time.sleep(0.001)
					state = 2
				
							
# update world
			ship.update(dt) 
			for x in bullets:
				x.update(dt)
			for x in rains:
				x.update(dt)			
# user interface
			a = ship.getAngle()
			theta = a*math.pi / 180
			cth = math.cos(theta)
			sth = math.sin(theta)
			p = ship.getPosition()	
			v = ship.getVelocity()	
			g = bullet.getPosition()		
		# movement		
			if key == 'Up':
				p[1] += 1
				ship.setPosition(p)
				ship.setFlickerOn()
			if key == 'Down':
				p[1] -= 1
				ship.setPosition(p)
				ship.setFlickerOn()
			if key == 'Left':
				p[0] -= 1
				ship.setPosition(p)
				ship.setFlickerOn()
			if key == 'Right':
				p[0] += 1
				ship.setPosition(p)
				ship.setFlickerOn()
#	shoot bullets		
			if	key == 'space':
				b = 4
				bullet = pho.Ball(win, p[0],p[1], radius = 0.5)
# too much flick...though I could end up using it
				bullet.setVelocity([b*cth, b*sth])
				bullet.draw()
				bullets.append(bullet)
	# end game conditions
			if key == "q":
				state = 2
		# wrap the window
			moveit = False
			p = list(ship.getPosition())
			if p[0] < 0:
				p[0] += winWidth
				moveit = True
			elif p[0] > winWidth:
				p[0] -= winWidth
				moveit = True
			if p[1] < 0:
				p[1] += winHeight
				moveit = True
			elif p[1] > winHeight:
				p[1] -= winHeight
				moveit = True
			if moveit:
				ship.setPosition(p)
				moveit = False
		# update visualization
			if frame % 10 == 0:
				win.update()
				time.sleep(dt*0.5)
			frame += 1
		
# end screen ie state == 2	

	if state == 2:
		win.setBackground("red")   
		ship.undraw()
	# undraw all from main screen
		for rain in rains:
			rain.undraw()
	# undraw all the boxes
		for bullet in bullets:
			bullet.undraw()
	# instruction to start text
		restart = gr.Text(gr.Point(250, 300), "press start to restart")
		restart.setFill('black')
		restart.setSize(20)
	# title of game:
		title = gr.Text(gr.Point(250, 100), "Galaxy Impact")
		title.setFill('black')
		title.setSize(36)
# restart
		begin = pho.Block(win, 25, 25, 10, 6, coloring = 'brown4')
		begins = gr.Text(gr.Point(250, 250), "restart")
		begins.setSize(15)
		begins.setFill('white')
		begin.draw()
		gameover = gr.Text(gr.Point(250, 450), "GAME OVER")
		gameover.setStyle('bold italic') 
		gameover.setSize(30)
		score = gr.Text(gr.Point(250, 350), "SCORE : %d" % counter)
		score.setSize(28)
		score.setStyle('bold')
  # draw everything			
		ending = [restart, begins, title, gameover, score]
		for word in ending:
			word.draw(win)

#wait for a mouse click on start to restart
		while True:
			event = win.checkMouse()
			key = win.checkKey()
			if key == 'q':
				win.close()

			if event != None and event.x < 300 and event.x > 200 and event.y > 220 and event.y < 280:
				state = 0
				win.close()
				main()
				break
	# all done
		if quit == True:	  
			win.close()


if __name__ == "__main__":
	main()
