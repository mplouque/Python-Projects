######################################################################################################################
# Name: Matthew Louque
# Date: 3/14/2016
# Description: A simple point class that can find midpoints and distances between points.
######################################################################################################################
#import math for pow and sqrt
import math
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

##########################################################
# ***DO NOT MODIFY OR REMOVE ANYTHING BELOW THIS POINT!***
# create some points
p1 = Point()
p2 = Point(3, 0)
p3 = Point(3, 4)
# display them
print "p1:", p1
print "p2:", p2
print "p3:", p3

# calculate and display some distances
print "distance from p1 to p2:", p1.dist(p2)
print "distance from p2 to p3:", p2.dist(p3)
print "distance from p1 to p3:", p1.dist(p3)

# calculate and display some midpoints
print "midpt of p1 and p2:", p1.midpt(p2)
print "midpt of p2 and p3:", p2.midpt(p3)
print "midpt of p1 and p3:", p1.midpt(p3)
