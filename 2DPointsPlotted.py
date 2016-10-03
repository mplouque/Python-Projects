######################################################################################################################
# Name: 
# Date: 
# Description: 
######################################################################################################################

# the 2D point class
#import math for pow and sqrt
import math
from Tkinter import *
from random import randint
# the 2D point class
class Point(object):
	# write your code for the point class here (and subsequently remove this comment)
	def __init__(self, x=0,y=0):
		#set the input x and y coordinates to xPoint and yPoint
		#Oh and make the inputs floating point numbers for maths
		self.xPoint = float(x)
		self.yPoint = float(y)
		
	#getter for xPoint
	@property
	def xPoint(self):
		return self._xPoint
	
	#setter for xPoint
	@xPoint.setter
	def xPoint(self, value):
		self._xPoint = value
	
	#getter for yPoint
	@property
	def yPoint(self):
		return self._yPoint
	
	#setter for yPoint
	@yPoint.setter
	def yPoint(self, value):
		self._yPoint = value
	
	#returns a string representation for a Point object
	def __str__(self):
		return "({},{})".format(self.xPoint,self.yPoint)
	
	#the distance formula is sqrt((x2-x1)^2+(y2-y1)^2)
	#point serves as x2,y2 and self serves as x1,y1
	def dist(self, point):
		deltaX = point.xPoint-self.xPoint
		deltaY = point.yPoint-self.yPoint
		
		distance=math.sqrt(math.pow(deltaX, 2)+math.pow(deltaY,2))
		return distance
	
	#midpoint formula is (x1+x2)/2, (y1+y2)/2
	
	def midpt(self, point):
		#create a temporary point object that we will use to return the calculated midpoint
		temp = Point()
		#solve for the xMidpoint
		xMid = (self.xPoint+point.xPoint)/2
		#solve for the yMidpoint
		yMid = (self.yPoint+point.yPoint)/2
		#assign xMid and yMid to temp's xPoint and yPoint
		temp.xPoint=xMid
		temp.yPoint=yMid
		#use the __srt__ method to return a string representation of the temporary Point Object, temp
		return temp

# the coordinate system class: (0,0) is in the top-left corner
# inherits from the Canvas class of Tkinter
class CoordinateSystem(Canvas):
	def __init__(self, master):
		#calls the superclass's constructor
		Canvas.__init__(self, master, bg="white")
		self.pack(fill=BOTH, expand=1)
		
	def plotPoints(self, n):
		#n is the number of points to be plotted
		
		for i in range(n):
			#create a new instance of the point class with the x and y coordinates between 0 and the width/height
			#these coordinates are generated randomly using the randint function
			point = Point(randint(0, WIDTH-1), randint(0,HEIGHT -1))
			#call the plot function telling it to plot at the location of the current point instance
			self.plot(point.xPoint, point.yPoint)
	def plot(self, x, y):
		#randomly picks a color in the colors array
		color = COLORS[randint(0, len(COLORS) -1)]
		#draws the point.
		self.create_oval(x, y, x + POINT_RADIUS * 2, y + POINT_RADIUS *2, outline = color)
##########################################################
# ***DO NOT MODIFY OR REMOVE ANYTHING BELOW THIS POINT!***
# the default size of the canvas is 400x400
WIDTH = 400
HEIGHT = 400
# the default point radius is 0 pixels (i.e., no center to the oval)
POINT_RADIUS = 0
# colors to choose from when plotting points
COLORS = [ "black", "red", "green", "blue", "cyan", "yellow", "magenta" ]
# the number of points to plot
NUM_POINTS = 2500

# create the window
window = Tk()
window.geometry("{}x{}".format(WIDTH, HEIGHT))
window.title("2D Points...Plotted")
# create the coordinate system as a Tkinter canvas inside the window
s = CoordinateSystem(window)
# plot some random points
s.plotPoints(NUM_POINTS)
# wait for the window to close
window.mainloop()