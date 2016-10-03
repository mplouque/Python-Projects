cubes = [x*x*x for x in range(10)]
print cubes

sums = [x+y for x in [1,2,3] for y in [3,1,4] if (x != y)]
print sums

l1 = [1,2,3]
l2 = [3,1,4]
sums2 = [x+y for x in l1 for y in l2 if (x!=y)]
print sums2

#the above give the same output

def f(x,y):
	return x+y
	
sums = [f(x,y) for x in [1,2,3] for y in [3,1,4] if (y!=x)]
print sums
#also the same 
#NEAT^^^

pairs = [[x,y] for x in l1 for y in l2 if (x<y)]
print "pairs: {}".format(pairs)

from math import pi

pi = [round(pi,n) for n in range(2,9)]
print pi

#sets are like lists without duplicates
#sets use {} instead of []
#technically no order to a set
a = {1,2,3,4,}
b = {1,2,3,3,3,4,4,4,5,5,5,6}
c = [3,1,4,1,5,9]

c = set(c)
print c

#the union of the sets a and b represents the elements in either a or b.
d = a | b
print d

#intersection

e = a & b
print e

offices = { "Jones" : 247, "Smith": 121, "Kennedy": 108 }
print offices
offices ["wilkerson"] = 355

loc = offices["Smith"]
print loc

del offices["wilkerson"]
print offices

if ("Smith" in offices): print "smith is in offices"

#also works with OBJECTS
#iteritems() returns the key and the values


dict = {x: x**3 for x in range(1,6)}
print dict


