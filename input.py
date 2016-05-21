# Arthur Yawe Makumbi	
# Fall 2015
# CS 151 Project 10
#
# creating a more interactive simulation:

# import necessary modules
import graphics as gr
import random
import graphics

win = gr.GraphWin(500, 500)

while True:
	cm = win.checkMouse()
	if cm != None:
		print cm
		break
	kp = win.checkKey()
	if kp != "":
		print kp