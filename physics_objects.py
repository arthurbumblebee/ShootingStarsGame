# Arthur Yawe Makumbi   
# Fall 2015
# CS 151 Project 11
#
# Inheritance:
    # Sharing the capabilities of one class with one or more other classes.


# import necessary modules
import graphics as gr
import random
import math


# parent class
class Thing:
    def __init__( self, win, the_type, x0, y0 , radius, mass ):
    # physical attributes
        self.x0 = x0
        self.y0 = y0
        self.type = the_type
        self.mass = mass
        self.radius = radius
        self.position = [ self.x0,self.y0 ] 
        self.velocity = [0,0]
        self.acceleration = [0,0]
        self.force = [0,0]
        self.elasticity = 0.9
        self.color = ['alice blue',  'AliceBlue',  'aquamarine',  'aquamarine1',  'aquamarine2',  'aquamarine3',  'aquamarine4',  'azure',  'azure1',  'azure2',  'azure3',  'azure4',  'beige',  'bisque',  'bisque1',  'bisque2',  'bisque3',  'bisque4',  'black',  'blanched almond',  'BlanchedAlmond',  'blue',  'blue1',  'blue2',  'blue3',  'blue4',  'blue violet',  'BlueViolet',  'brown',  'brown1',  'brown2',  'brown3',  'brown4',  'burlywood',  'burlywood1',  'burlywood2',  'burlywood3',  'burlywood4',  'cadet blue',  'CadetBlue',  'CadetBlue1',  'CadetBlue2',  'CadetBlue3',  'CadetBlue4',  'chartreuse',  'chartreuse1',  'chartreuse2',  'chartreuse3',  'chartreuse4',  'chocolate',  'chocolate1',  'chocolate2',  'chocolate3',  'chocolate4',  'coral',  'coral1',  'coral2',  'coral3',  'coral4',  'cornflower blue',  'CornflowerBlue',  'cornsilk',  'cornsilk1',  'cornsilk2',  'cornsilk3',  'cornsilk4',  'cyan',  'cyan1',  'cyan2',  'cyan3',  'cyan4',  'dark blue',  'DarkBlue',  'dark cyan',  'DarkCyan',  'dark goldenrod',  'DarkGoldenrod',  'DarkGoldenrod1',  'DarkGoldenrod2',  'DarkGoldenrod3',  'DarkGoldenrod4',  'dark gray',  'DarkGray',  'dark green',  'DarkGreen',  'dark grey',  'DarkGrey',  'dark khaki',  'DarkKhaki',  'dark magenta',  'DarkMagenta',  'dark olive green',  'DarkOliveGreen',  'DarkOliveGreen1',  'DarkOliveGreen2',  'DarkOliveGreen3',  'DarkOliveGreen4',  'dark orange',  'DarkOrange',  'DarkOrange1',  'DarkOrange2',  'DarkOrange3',  'DarkOrange4',  'dark orchid',  'DarkOrchid',  'DarkOrchid1',  'DarkOrchid2',  'DarkOrchid3',  'DarkOrchid4',  'dark red',  'DarkRed',  'dark salmon',  'DarkSalmon',  'dark sea green',  'DarkSeaGreen',  'DarkSeaGreen1',  'DarkSeaGreen2',  'DarkSeaGreen3',  'DarkSeaGreen4',  'dark slate blue',  'DarkSlateBlue',  'dark slate gray',  'DarkSlateGray',  'DarkSlateGray1',  'DarkSlateGray2',  'DarkSlateGray3',  'DarkSlateGray4',  'dark slate grey',  'DarkSlateGrey',  'dark turquoise',  'DarkTurquoise',  'dark violet',  'DarkViolet',  'deep pink',  'DeepPink',  'DeepPink1',  'DeepPink2',  'DeepPink3',  'DeepPink4',  'deep sky blue',  'DeepSkyBlue',  'DeepSkyBlue1',  'DeepSkyBlue2',  'DeepSkyBlue3',  'DeepSkyBlue4',  'dim gray',  'DimGray',  'dim grey',  'DimGrey',  'dodger blue',  'DodgerBlue',  'DodgerBlue1',  'DodgerBlue2',  'DodgerBlue3',  'DodgerBlue4',  'firebrick',  'firebrick1',  'firebrick2',  'firebrick3',  'firebrick4',   'forest green',  'ForestGreen',  'gainsboro',  'gold',  'gold1',  'gold2',  'gold3',  'gold4',  'goldenrod',  'goldenrod1',  'goldenrod2',  'goldenrod3',  'goldenrod4',  'gray',  'gray0',  'gray1',  'gray10',  'gray100',  'gray11',  'gray12',  'gray13',  'gray14',  'gray15',  'gray16',  'gray17',  'gray18',  'gray19',  'gray2',  'gray20',  'gray21',  'gray22',  'gray23',  'gray24',  'gray25',  'gray26',  'gray27',  'gray28',  'gray29',  'gray3',  'gray30',  'gray31',  'gray32',  'gray33',  'gray34',  'gray35',  'gray36',  'gray37',  'gray38',  'gray39',  'gray4',  'gray40',  'gray41',  'gray42',  'gray43',  'gray44',  'gray45',  'gray46',  'gray47',  'gray48',  'gray49',  'gray5',  'gray50',  'gray51',  'gray52',  'gray53',  'gray54',  'gray55',  'gray56',  'gray57',  'gray58',  'gray59',  'gray6',  'gray60',  'gray61',  'gray62',  'gray63',  'gray64',  'gray65',  'gray66',  'gray67',  'gray68',  'gray69',  'gray7',  'gray70',  'gray71',  'gray72',  'gray73',  'gray74',  'gray75',  'gray76',  'gray77',  'gray78',  'gray79',  'gray8',  'gray80',  'gray81',  'gray82',  'gray83',  'gray84',  'gray85',  'gray86',  'gray87',  'gray88',  'gray89',  'gray9',  'gray90',  'gray91',  'gray92',  'gray93',  'gray94',  'gray95',  'gray96',  'gray97',  'gray98',  'gray99',  'green',  'green1',  'green2',  'green3',  'green4',  'green yellow',  'GreenYellow',  'grey',  'grey0',  'grey1',  'grey10',  'grey100',  'grey11',  'grey12',  'grey13',  'grey14',  'grey15',  'grey16',  'grey17',  'grey18',  'grey19',  'grey2',  'grey20',  'grey21',  'grey22',  'grey23',  'grey24',  'grey25',  'grey26',  'grey27',  'grey28',  'grey29',  'grey3',  'grey30',  'grey31',  'grey32',  'grey33',  'grey34',  'grey35',  'grey36',  'grey37',  'grey38',  'grey39',  'grey4',  'grey40',  'grey41',  'grey42',  'grey43',  'grey44',  'grey45',  'grey46',  'grey47',  'grey48',  'grey49',  'grey5',  'grey50',  'grey51',  'grey52',  'grey53',  'grey54',  'grey55',  'grey56',  'grey57',  'grey58',  'grey59',  'grey6',  'grey60',  'grey61',  'grey62',  'grey63',  'grey64',  'grey65',  'grey66',  'grey67',  'grey68',  'grey69',  'grey7',  'grey70',  'grey71',  'grey72',  'grey73',  'grey74',  'grey75',  'grey76',  'grey77',  'grey78',  'grey79',  'grey8',  'grey80',  'grey81',  'grey82',  'grey83',  'grey84',  'grey85',  'grey86',  'grey87',  'grey88',  'grey89',  'grey9',  'grey90',  'grey91',  'grey92',  'grey93',  'grey94',  'grey95',  'grey96',  'grey97',  'grey98',  'grey99',  'honeydew',  'honeydew1',  'honeydew2',  'honeydew3',  'honeydew4',  'hot pink',  'HotPink',  'HotPink1',  'HotPink2',  'HotPink3',  'HotPink4',  'indian red',  'IndianRed',  'IndianRed1',  'IndianRed2',  'IndianRed3',  'IndianRed4',  'ivory',  'ivory1',  'ivory2',  'ivory3',  'ivory4',  'khaki',  'khaki1',  'khaki2',  'khaki3',  'khaki4',  'lavender',  'lavender blush',  'LavenderBlush',  'LavenderBlush1',  'LavenderBlush2',  'LavenderBlush3',  'LavenderBlush4',  'lawn green',  'LawnGreen',  'lemon chiffon',  'LemonChiffon',  'LemonChiffon1',  'LemonChiffon2',  'LemonChiffon3',  'LemonChiffon4',  'light blue',  'LightBlue',  'LightBlue1',  'LightBlue2',  'LightBlue3',  'LightBlue4',  'light coral',  'LightCoral',  'light cyan',  'LightCyan',  'LightCyan1',  'LightCyan2',  'LightCyan3',  'LightCyan4',  'light goldenrod',  'LightGoldenrod',  'LightGoldenrod1',  'LightGoldenrod2',  'LightGoldenrod3',  'LightGoldenrod4',  'light goldenrod yellow',  'LightGoldenrodYellow',  'light gray',  'LightGray',  'light green',  'LightGreen',  'light grey',  'LightGrey',  'light pink',  'LightPink',  'LightPink1',  'LightPink2',  'LightPink3',  'LightPink4',  'light salmon',  'LightSalmon',  'LightSalmon1',  'LightSalmon2',  'LightSalmon3',  'LightSalmon4',  'light sea green',  'LightSeaGreen',  'light sky blue',  'LightSkyBlue',  'LightSkyBlue1',  'LightSkyBlue2',  'LightSkyBlue3',  'LightSkyBlue4',  'light slate blue',  'LightSlateBlue',  'light slate gray',  'LightSlateGray',  'light slate grey',  'LightSlateGrey',  'light steel blue',  'LightSteelBlue',  'LightSteelBlue1',  'LightSteelBlue2',  'LightSteelBlue3',  'LightSteelBlue4',  'light yellow',  'LightYellow',  'LightYellow1',  'LightYellow2',  'LightYellow3',  'LightYellow4',  'lime green',  'LimeGreen',  'linen',  'magenta',  'magenta1',  'magenta2',  'magenta3',  'magenta4',  'maroon',  'maroon1',  'maroon2',  'maroon3',  'maroon4',  'medium aquamarine',  'MediumAquamarine',  'medium blue',  'MediumBlue',  'medium orchid',  'MediumOrchid',  'MediumOrchid1',  'MediumOrchid2',  'MediumOrchid3',  'MediumOrchid4',  'medium purple',  'MediumPurple',  'MediumPurple1',  'MediumPurple2',  'MediumPurple3',  'MediumPurple4',  'medium sea green',  'MediumSeaGreen',  'medium slate blue',  'MediumSlateBlue',  'medium spring green',  'MediumSpringGreen',  'medium turquoise',  'MediumTurquoise',  'medium violet red',  'MediumVioletRed',  'midnight blue',  'MidnightBlue',  'mint cream',  'MintCream',  'misty rose',  'MistyRose',  'MistyRose1',  'MistyRose2',  'MistyRose3',  'MistyRose4',  'moccasin', 'navy',  'navy blue',  'NavyBlue',  'old lace',  'OldLace',  'olive drab',  'OliveDrab',  'OliveDrab1',  'OliveDrab2',  'OliveDrab3',  'OliveDrab4',  'orange',  'orange1',  'orange2',  'orange3',  'orange4',  'orange red',  'OrangeRed',  'OrangeRed1',  'OrangeRed2',  'OrangeRed3',  'OrangeRed4',  'orchid',  'orchid1',  'orchid2',  'orchid3',  'orchid4',  'pale goldenrod',  'PaleGoldenrod',  'pale green',  'PaleGreen',  'PaleGreen1',  'PaleGreen2',  'PaleGreen3',  'PaleGreen4',  'pale turquoise',  'PaleTurquoise',  'PaleTurquoise1',  'PaleTurquoise2',  'PaleTurquoise3',  'PaleTurquoise4',  'pale violet red',  'PaleVioletRed',  'PaleVioletRed1',  'PaleVioletRed2',  'PaleVioletRed3',  'PaleVioletRed4',  'papaya whip',  'PapayaWhip',  'peach puff',  'PeachPuff',  'PeachPuff1',  'PeachPuff2',  'PeachPuff3',  'PeachPuff4',  'peru',  'pink',  'pink1',  'pink2',  'pink3',  'pink4',  'plum',  'plum1',  'plum2',  'plum3',  'plum4',  'powder blue',  'PowderBlue',  'purple',  'purple1',  'purple2',  'purple3',  'purple4',  'red',  'red1',  'red2',  'red3',  'red4',  'rosy brown',  'RosyBrown',  'RosyBrown1',  'RosyBrown2',  'RosyBrown3',  'RosyBrown4',  'royal blue',  'RoyalBlue',  'RoyalBlue1',  'RoyalBlue2',  'RoyalBlue3',  'RoyalBlue4',  'saddle brown',  'SaddleBrown',  'salmon',  'salmon1',  'salmon2',  'salmon3',  'salmon4',  'sandy brown',  'SandyBrown',  'sea green',  'SeaGreen',  'SeaGreen1',  'SeaGreen2',  'SeaGreen3',  'SeaGreen4',  'seashell',  'seashell1',  'seashell2',  'seashell3',  'seashell4',  'sienna',  'sienna1',  'sienna2',  'sienna3',  'sienna4',  'sky blue',  'SkyBlue',  'SkyBlue1',  'SkyBlue2',  'SkyBlue3',  'SkyBlue4',  'slate blue',  'SlateBlue',  'SlateBlue1',  'SlateBlue2',  'SlateBlue3',  'SlateBlue4' ,  'snow',  'snow1',  'snow2',  'snow3',  'snow4',  'spring green',  'SpringGreen',  'SpringGreen1',  'SpringGreen2',  'SpringGreen3',  'SpringGreen4',  'steel blue',  'SteelBlue',  'SteelBlue1',  'SteelBlue2',  'SteelBlue3',  'SteelBlue4',  'tan',  'tan1',  'tan2',  'tan3',  'tan4',  'thistle',  'thistle1',  'thistle2',  'thistle3',  'thistle4',  'tomato',  'tomato1',  'tomato2',  'tomato3',  'tomato4',  'turquoise',  'turquoise1',  'turquoise2',  'turquoise3',  'turquoise4',  'violet',  'violet red',  'VioletRed',  'VioletRed1',  'VioletRed2',  'VioletRed3',  'VioletRed4',  'wheat',  'wheat1',  'wheat2',  'wheat3',  'wheat4', 'yellow',  'yellow1',  'yellow2',  'yellow3',  'yellow4',  'yellow green',  'YellowGreen'] 
        self.win = win
        self.scale = 10
        self.vis = []
        
# get methods   
    def getX0 (self):
        return self.x0
    
    def getY0 (self):
        return self.y0
    
    def getType (self):
        return self.type
                                  
    def getMass (self):
        return self.mass
        
    def getRadius (self):
        return self.radius
        
    def getPosition (self):
        return self.position[:]
        
    def getVelocity (self):
        return self.velocity[:]
        
    def getAcceleration (self):
        return self.acceleration[:]
        
    def getForce (self):
        return self.force
        
    def getElasticity (self):
        return self.elasticity
        
    def getScale (self):
        return self.scale
        
# set methods 
    def setType (self, a):
        self.type = a
                                
    def setMass (self, m):
        self.mass = m
        
    def setRadius (self, r):
        self.radius = r
                                
    def setPosition (self , p):
        # new position - current position
        dx_screen = (p[0]-self.position[0]) *self.scale
        dy_screen = (p[1]-self.position[1])*self.scale
        for object in self.vis:
            object.move( dx_screen, -dy_screen) 
        self.position = [p[0], p[1]]
        
    def setVelocity (self, v):
        self.velocity = v[:]
        
    def setAcceleration (self, a):
        self.acceleration = a[:]
        
    def setForce (self, f):
        self.force = f
        
    def setElasticity (self, a):
        self.elasticity = a
    
    def setScale (self, f):
        self.scale = f
        
     # draw method  
    def draw(self):
        for item in self.vis:
            item.draw(self.win) 
            
     # draw method  
    def undraw(self):
        for item in self.vis:
            item.undraw() 
    
    # adjusts the internal position and velocity values based on current accelerations and forces.      
    def update (self, dt):
        self.position[0] += self.velocity[0]*dt
        self.position[1] += self.velocity[1]*dt
        
        dx = (self.velocity[0]*dt) * self.scale     
        dy = -(self.velocity[1]*dt) * self.scale
        
        for item in self.vis:
            item.move(dx , dy)
            
        self.velocity[0] += self.acceleration[0] * dt
    #   self.velocity[0] = 0
        self.velocity[1] += self.acceleration[1] * dt
        
        self.velocity[0] += dt * self.force[0] / self.mass
        self.velocity[1] += dt * self.force[1] / self.mass
        
#       self.velocity[0] *= 0.998
#       self.velocity[1] *= 0.998
        
# a new Ball class that inherits the Thing class        
class Ball(Thing):
    def __init__( self, win, x0, y0, radius = 1.3, mass = 1, coloring = 'blue'):
        Thing.__init__(self, win, "ball", x0, y0,  radius = radius, mass = mass)
        self.vis = [ gr.Circle( gr.Point(self.x0*self.scale, win.getHeight()-self.y0*self.scale), 
                             self.radius * self.scale ) ]
        self.coloring = coloring    
        for ball in self.vis:
            ball.setFill( self.coloring )

            
class Floor(Thing):
    def __init__( self, win, x0, y0, length = 1, thickness = 1, coloring = 'green'):
        #assign
        self.width = length
        self.height = thickness
        self.coloring = coloring
        Thing.__init__(self, win, "floor", x0, y0, mass=0, radius =0)
        self.vis = [ gr.Rectangle( gr.Point(self.x0*self.scale, self.win.getHeight()-(self.y0+self.height/2)*self.scale), 
                            gr.Point((self.x0+self.width)*self.scale, self.win.getHeight() - (self.y0 - self.height/2)*self.scale)) ]
        for object in self.vis:
            object.setFill( self.coloring )
            
    def getHeight( self):
        return self.height
        
    def getWidth( self):
        return self.width
        

class Wall(Thing):
    def __init__( self, win, x0, y0 , height , width, coloring = 'blue'):
    #assign
        self.width = width
        self.height = height
        self.coloring = coloring    
        Thing.__init__(self, win, "wall", x0, y0, mass=0, radius =0)
        self.vis = [ gr.Rectangle(gr.Point((self.x0 - width/2)*self.scale, self.win.getHeight()-(self.y0*self.scale)),
                                    gr.Point((self.x0+width/2)*self.scale , self.win.getHeight()-(self.y0+self.height)*self.scale)) ]
        for ball in self.vis:
            ball.setFill( self.coloring )
            
    def getHeight( self):
        return self.height
        
    def getWidth( self):
        return self.width
        
        
class Block(Thing):
    def __init__( self, win, x0, y0 , width , height, coloring = 'blue'):
    #assign
        self.width = width
        self.height = height
        self.coloring = coloring
        Thing.__init__(self, win, "block", x0, y0, mass=0, radius =0)
        self.vis = [ gr.Rectangle( gr.Point((self.x0-self.width/2)*self.scale, self.win.getHeight()-(self.y0-self.height/2)*self.scale), 
                        gr.Point((self.x0+self.width/2)*self.scale, self.win.getHeight() - (self.y0+ self.height/2)*self.scale)) ]
        for ball in self.vis:
            ball.setFill( self.coloring )
            
    def getHeight( self):
        return self.height
        
    def getWidth( self):
        return self.width


class Triangle(Thing):
    def __init__( self, win, x0, y0 , width , height, coloring = 'blue'):
    #assign
        self.width = width
        self.height = height
        self.coloring = coloring
        Thing.__init__(self, win, "block", x0, y0, mass=0, radius =0)
        self.vis = [ gr.Polygon( gr.Point(self.x0*self.scale, self.win.getHeight()-self.y0*self.scale), 
                        gr.Point((self.x0+self.width/2)*self.scale, self.win.getHeight() - (self.y0+ self.height)*self.scale),
                        gr.Point((self.x0+self.width)*self.scale , self.win.getHeight()- self.y0*self.scale)) ]
        for ball in self.vis:
            ball.setFill( self.coloring )
            
    def getHeight( self):
        return self.height
        
    def getWidth( self):
        return self.width
        
class Hexagon(Thing):
    def __init__( self, win, x0, y0 , width , height, coloring = 'blue'):
    #assign
        self.width = width
        self.height = height
        self.coloring = coloring
        Thing.__init__(self, win, "block", x0, y0, mass=0, radius =0)
        self.vis = [ gr.Polygon( gr.Point(self.x0*self.scale, self.win.getHeight()-(self.y0+self.height/2)*self.scale),
                        gr.Point((self.x0+self.width/4)*self.scale, self.win.getHeight() - (self.y0+ self.height)*self.scale),
                        gr.Point((self.x0+self.width*0.75)*self.scale , self.win.getHeight()- (self.y0+self.height)*self.scale), 
                        gr.Point((self.x0+self.width)*self.scale, self.win.getHeight() - (self.y0+self.height/2)*self.scale),
                        gr.Point((self.x0+self.width*0.75)*self.scale, self.win.getHeight() - self.y0*self.scale),
                        gr.Point((self.x0+self.width/4)*self.scale, self.win.getHeight() - self.y0*self.scale))]
        for ball in self.vis:
            ball.setFill( self.coloring )
            
    def getHeight( self):
        return self.height
        
    def getWidth( self):
        return self.width
        
        
class RotatingBlock(Thing):
    def __init__(self, win, x0, y0 , width , height, coloring = 'blue', Ax = None, Ay = None):
        self.width = width
        self.height = height
        self.coloring = coloring
        Thing.__init__(self, win, "rotating block", x0, y0, mass=1, radius =0)
        self.points = [[-self.width/2 , -self.height/2] , [self.width/2 , -self.height/2] ,
                         [self.width/2 , self.height/2] , [-self.width/2 , self.height/2]]
        self.Ax = Ax
        self.Ay = Ay
        if self.Ax != None and self.Ay != None:
            self.anchor = [Ax, Ay]
        else:
            self.anchor = [x0, y0]
        self.angle = 0.0
        self.pos = [x0,y0]
        self.rvel = 0.0
        self.win = win
        self.drawn = False      

    def draw(self):
        for element in self.vis:
            element.undraw()
        self.render()
        for element in self.vis:
            element.draw(self.win)
        self.drawn = True
        
    def getAngle(self):
        return self.angle
        
    def setAngle(self, val):
        self.angle = val
        if self.drawn == True:
            self.draw()
    
    def getAnchor(self):
        return self.anchor
        
    def setAnchor(self, val):
        self.anchor = val
        
    def getRotVelocity(self):
        return self.rvel
        
    def setRotVelocity(self, val):
        self.rvel = val
            
    def rotate(self, val):
        self.angle += val
        if self.drawn == True:
            self.draw()
    def render(self):
        theta = math.pi*self.angle / 180.0
        cth = math.cos(theta)
        sth = math.sin(theta)
        
        pts = []
        for vertex in self.points:
            # subtract the anchor the vertices
            xt = (vertex[0] + self.pos[0]) - self.anchor[0]
            yt = (vertex[1] + self.pos[1]) - self.anchor[1] 
            # rotate the points around the Z-axis
            xtt = cth * xt - sth * yt
            ytt = sth * xt + cth * yt
            # add the anchor point back
            xf = xtt +  self.anchor[0]
            yf = ytt +  self.anchor[1]
        # handle the screen coordinates while making a zelle point obj
            pts.append(gr.Point(self.scale* xf, self.win.getHeight() - self.scale *yf))
            
        self.vis = [gr.Polygon(pts[0], pts[1], pts[2], pts[3])]
        for ball in self.vis:
            ball.setFill( self.coloring )
    def update(self, dt):
        da = self.rvel * dt
        if da != 0:
            self.rotate(da)
        #   rotate(da)
            Thing.update(self, dt)
                        
            
# make a ship object, treat it as a ball
# but it needs to be able to rotate
# should probably have a parent rotator class that does most of this for you
class Ship(Thing):
    def __init__(self, win, x0=0, y0=0, mass=1, radius=3):
        Thing.__init__(self, win, "ball", x0, y0, mass=mass, radius=radius)

        # anchor point is by default the center of the ship/circle so we don't need it
        self.angle = 0.
        self.dangle = 0.
     #   pos=[x0, y0]

        # visualization properties
        # This is a two-part visualization
        # the ship is a triangle
        self.bodypts = [ (radius, 0),
                         (- radius*0.5,   1.732*radius*0.5),
                         (- radius*0.5, - 1.732*radius*0.5) ]
        # the exhaust is another triangle
        self.flamepts = [ (- radius*0.5,   0.5*radius),
                          (- radius*0.5, - 0.5*radius),
                          (- radius*1.732, 0) ]

        self.scale = 10.
        self.vis = []
        self.drawn = False

        # these are for handling the flicker of the exhaust
        self.flickertime = 6
        self.flicker = False
        self.countdown = 0

    #########
    # these functions are identical to the rotating block
    # a smart coder would make a parent rotator class

    # draw the object into the window
    def draw(self):
        for item in self.vis:
            item.undraw()
        self.render()
        for item in self.vis:
            item.draw(self.win)
        self.drawn = True

    # undraw the object from the window
    def undraw(self):
        for item in self.vis:
            item.undraw()
        self.drawn = False

    # get and set the angle of the object
    # these are unique to rotators
    def getAngle(self):
        return self.angle

    # setAngle has to update the visualization
    def setAngle(self, a):
        self.angle = a
        if self.drawn:
            self.draw()

    # get and set rotational velocity
    def setRotVelocity(self, rv):
        self.dangle = rv # degrees per second

    def getRotVelocity(self):
        return self.dangle

    # incrementally rotate by da (in degrees)
    # has to update the visualization
    def rotate(self, da):
        self.angle += da
        if self.drawn:
            self.draw()

    # special ship methods
    def setFlickerOn(self, countdown = 50):
        self.flicker = True
        self.countdown = countdown

    def setFlickerOff(self):
        self.countdown = 0
        self.flicker = False
        
    # simplified render function since the ship always rotates around its center
    def render(self):

        # get the cos and sin of the current orientation
        theta = math.pi * self.angle / 180.
        cth = math.cos(theta)
        sth = math.sin(theta)

        # rotate each point around the object's center
        pts = []
        for vertex in self.bodypts + self.flamepts:
            # move the object's center to 0, 0, which it is already in model coordinates
            xt = vertex[0]
            yt = vertex[1]

            # rotate the vertex by theta around the Z axis
            xtt = cth*xt - sth*yt
            ytt = sth*xt + cth*yt

            # move the object's center back to its original location
            xf = xtt + self.position[0]
            yf = ytt + self.position[1]

            # create a point with the screen space coordinates
            pts.append( gr.Point(self.scale * xf, self.win.getHeight() - self.scale * yf) )

        # make the two objects
        self.vis = [ gr.Polygon( pts[:3] ), gr.Polygon( pts[3:] ) ]
        self.vis[0].setFill("dark blue")
        self.vis[0].setOutline("dark red")
        self.vis[1].setOutline("yellow")

    # update the various state variables
    # add a unique flicker touch
    def update(self, dt):
        # update the angle based on rotational velocity
        da = self.dangle * dt
        if da != 0.0: # don't bother updating if we don't have to
            self.rotate( da )
            
        # flicker the flames
        # this should be a field of the object
        if self.flicker and self.countdown > 0:
            if self.countdown % self.flickertime < self.flickertime/2:
                self.vis[1].setFill( 'yellow' )
            else:
                self.vis[1].setFill( 'orange' )
            self.countdown -= 1
        else:
            self.vis[1].setFill( 'white' )

        # call the parent update for the rest of it
        Thing.update(self, dt)
