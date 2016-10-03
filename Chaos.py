######################################################################################################################
# Name: 
# Date: 
# Description: 
######################################################################################################################

from Tkinter import *
from random import randint

# the 2D point class
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

# the chaos game class
# inherits from the Canvas class of Tkinter
# the coordinate system class: (0,0) is in the top-left corner
# inherits from the Canvas class of Tkinter
class ChaosGame(Canvas):
	def __init__(self, master):
		#calls the superclass's constructor
		Canvas.__init__(self, master, bg="white")
		self.pack(fill=BOTH, expand=1)
	
	def play(self, n):
		#n is the number of points to be plotted
		#creates a point for each vertex of the triangle
		topVertex = Point(WIDTH/2 , VERTEX_RADIUS*2)
		leftVertex = Point(VERTEX_RADIUS*2, HEIGHT- VERTEX_RADIUS*2)
		rightVertex = Point(WIDTH - VERTEX_RADIUS*2 , HEIGHT- VERTEX_RADIUS*2)
		midVertex = Point(WIDTH/2, HEIGHT * 2/3)
		#creates a list containing each vertex
		vertexList = [topVertex, rightVertex, leftVertex, midVertex]
		#plots each vertex as a red circle
		self.plotVertex(topVertex.xPoint, topVertex.yPoint)
		self.plotVertex(leftVertex.xPoint, leftVertex.yPoint)
		self.plotVertex(rightVertex.xPoint, leftVertex.yPoint)
		
		#picks a random vertex to use as a vertex for the first midpoint that will be plotted
		startingPoint = vertexList[randint(0, len(vertexList)-1)]
		#removes that point from the list so the same vertex can not be picked twice
		vertexList.remove(startingPoint)
		#picks another vertex from the list containing the two vertices that have not been picked yet
		secondPoint = vertexList[randint(0, len(vertexList)-1)]
		#reinsert the first vertex that was removed back into the list
		vertexList.append(startingPoint)
		#plot the first mid point between the two randomly picked vertices 
		startingMidpoint = startingPoint.midpt(secondPoint)
		self.plot(startingMidpoint.xPoint, startingMidpoint.yPoint)
		#do the following one time for each point until we reach the max number of points we wanted plotted.
		for i in range(n):
			#pick a random vertex from the list of vertices
			destVertex = vertexList[randint(0, len(vertexList) -1)]
			#create a point that is halfway between the previously plotted point and the randomly picked vertex
			chaosPoint = startingMidpoint.midpt(destVertex)
			#plot that point
			self.plot(chaosPoint.xPoint, chaosPoint.yPoint)
			#the point that was just plotted now becomes the reference point 
			startingMidpoint = chaosPoint
			#rinse and repeat n times
			
			
	def plotVertex(self, x, y):
		#sets the color of the vertex to red
		color = VERTEX_COLOR
		
		#plots a point with a radius of 2 and a color outline and fill of red.
		self.create_oval(x,y, x + VERTEX_RADIUS * 2, y + VERTEX_RADIUS *2, outline = color, fill = color)
		
	def plot(self, x, y):
		#randomly picks a color in the colors array
		color = POINT_COLOR
		COLORS = [ "black", "red", "green", "blue", "cyan", "yellow", "magenta" ]
		color = COLORS[randint(0, len(COLORS)-1)]
		#draws the point.
		self.create_oval(x, y, x + POINT_RADIUS * 2, y + POINT_RADIUS *2, outline = color)

##########################################################
# ***DO NOT MODIFY OR REMOVE ANYTHING BELOW THIS POINT!***
# the default size of the canvas is 600x520
WIDTH = 600
HEIGHT = 520
# the default vertex radius is 2 pixels and color is red
VERTEX_RADIUS = 2
VERTEX_COLOR = "red"
# the default point radius is 0 pixels and color is black
POINT_RADIUS = 0
POINT_COLOR = "black"
# the number of midpoints to plot
NUM_POINTS = 500000

# create the window
window = Tk()
window.geometry("{}x{}".format(WIDTH, HEIGHT))
window.title("The Chaos Game")
# create the chaos game as a Tkinter canvas inside the window
s = ChaosGame(window)
# play the chaos game with at least 50000 points
s.play(NUM_POINTS)
# wait for the window to close
window.mainloop()