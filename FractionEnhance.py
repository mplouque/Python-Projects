######################################################################################################################
# Name: Matthew Louque	
# Date: 2/25/2016
# Description: Fraction class. Can add/subtract/multiplay/divide and simplify fractions
######################################################################################################################
#import the gcd (greatest Common Denominator) function
from fractions import gcd
class Fraction(object):
	# write your code for the fraction class here
	def __init__(self, numerator=0, denominator=1):
		#constructor for fraction class, if no input sets num to 0 and den to 1
		self.num = numerator
		self.den = denominator
	
	#num getter
	@property
	def num(self):
		return self._num
	
	@num.setter
	def num(self, numerator):
		#sets the numerator = to the first (non self) argument when creating an instance of the fraction class
		self._num = numerator
		
	#den getter		
	@property
	def den(self):
		return self._den
		
	@den.setter
	def den(self, denominator):
		#denominator can not be zero
		#if it is just override it and set = to zero
		if (denominator != 0):
			self._den= denominator
		else:
			self._den = 1
			
	#function to reduce fraction to its simplest form
	def simplify(self):
		#passes the numerator and denominator of a fraction into the built-in gcd function in python
		#this gives us the greatest common denominator of the num and den
		greatestCommonDenominator = gcd(self.num, self.den)
		#divide the num and den by the greatestCommonDenominator to simplify the fraction
		self.num = self.num/greatestCommonDenominator
		self.den = self.den/greatestCommonDenominator
		#return the new simplified fraction
		return self
	
	#function to print a str representation of a fraction object
	def __str__(self):
		#prints the num over the den, and the the floating point version of that fraction
		return "{}/{}  ({})".format(self.num, self.den, float(self.num)/self.den) 
	
	#function to add two fraction objects using the "+" operator
	def __add__(self, other):
		#creates a new fraction object
		new = Fraction()
		#multiplies the first num times the second den
		temp_numerator = self.num * other.den
		#multiplies the second num by the first num
		temp_numerator2 = other.num * self.den
		#sets the den of the new fraction object to the sum of temp_numerator and temp_numerator2
		new.num = temp_numerator + temp_numerator2
		#if the num is zero, set the den to 1 (most reduced form of 0 is 0/1)
		if (new.num !=0):
			#if the num is not zero set the new fraction den to the first den times the second den
			new.den = self.den * other.den
		else: 
			new.den = 1
		#return the simplified version of the new fraction
		return new.simplify()
		
	#function to subtract two fraction objects using the "-" operator	
	def __sub__(self, other):
		#identical to the __add__ function except for it subtracts temp_numerator2 from temp_numerator
		new = Fraction()
		temp_numerator = self.num * other.den
		temp_numerator2 = other.num * self.den
		new.num = temp_numerator - temp_numerator2
		if (new.num !=0):
			new.den = self.den * other.den
		else: 
			new.den = 1
		return new.simplify()
	
	#function to multiply two fraction objects using the "*" operator
	def __mul__(self, other):
		#creates a new fraction object (default is 0/1)
		new = Fraction()
		#set the new fraction objec's num to the product of the first num * the second num
		new.num = self.num *other.num
		#if the new numerator is 0 then set the new den to 1
		if (new.num !=0):
			#if the new num isnt 0 then set the new den to the product of the first den * the second den
			new.den = self.den * other.den
		else: 
			new.den = 1
		#return the simplified version of the new fraction object
		return new.simplify()
	
	#function to divide two fraction objects using the "/" operator
	def __div__ (self, other):
		#creates a new fraction object (default is 0/1)
		new = Fraction()
		#cross multiply
		#set the new fraction objec's num to the product of the first num * the second den
		new.num = self.num * other.den
		#if the new numerator is 0 then set the new den to 1
		if (new.num !=0):
			#if the new num isnt 0 then set the new den to the product of the first den * the second num
			new.den = self.den * other.num
		else: 
			new.den = 1
		#return the simplified version of the new fraction object
		return new.simplify()
		
	

		
# ***DO NOT MODIFY OR REMOVE ANYTHING BELOW THIS POINT!***
# the main part of the program
# create some fractions
f1 = Fraction()
f2 = Fraction(5, 8)
f3 = Fraction(3, 4)
f4 = Fraction(1, 0)

# display them
print "f1:", f1
print "f2:", f2
print "f3:", f3
print "f4:", f4

# play asimplify
f3.num = 5
f3.den = 8
f1 = f2 + f3
f4.den = 88
f2 = f1 - f1
f3 = f1 * f1
f4 = f4 / f3

# display them again
print
print "f1:", f1
print "f2:", f2
print "f3:", f3
print "f4:", f4
