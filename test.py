# Arthur 
# testing 

import math
import time
import graphics as gr
import physics_objects as pho

# Fall 2015
# CS 151 HW 12
#

def robotCars():
    autos = {}
    autos['Tesla'] = 'hey try it out'
    autos['Subaru'] = 'watching ahead'
    autos['Mercedes'] = 'in stereo where possible'
    autos['Google'] = 'spinning sensors'
    autos['Apple'] = 'secret'
    autos['Uber'] = 'underdog'
    autos['Samsung'] = 'new player'
    autos['Nissan'] = 'by 2020'
    autos['Microsoft'] = 'what?'

    players = autos.keys()
    players.sort()

    s = players[0] + ' wants to keep it a ' + autos[players[0]]
    t = players[-1] + ' is the ' + autos[players[-1]]

    del autos['Microsoft']
    players.remove('Microsoft')

    u = players[-2] + ' is pushing the field'
    autos['Tesla'] = 'hopes you are paying attention'

    # mark 1
    return s + "\n" + t + "\n" + u

print robotCars()