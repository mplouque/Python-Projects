###########################################################################################
# Name: 
# Date: 
# Description: 
###########################################################################################
from datetime import datetime
startTime= 0
# it may help to make use of some math functions (which you can import)
import math, time
# it may also help to define other "helper" functions (i.e., delegate tasks!)
def isPrime(n):
	#check if prime
	#if prime return true
	#if not prime return false
	for i in xrange(3, int(math.sqrt(n)) + 1, 2):
		if (n % i == 0):	
			return False
	return True
def isPalindrome(num):
	forwards = num
	backwards = 0
	#creates the inverse of a number. 123 become 321, and then assigns it to backwards. 
	while num > 0:
		backwards = (backwards * 10) + (num % 10)
		num = num / 10
	#if the
	if (forwards == backwards):
		return True
	else:
		return False
# solves problem 3
def problem3():
	#num=600851475143
	num = input()
	global startTime
	startTime = time.time()
	i =1
	biggest_Prime=3
	while (i < math.sqrt(num)):
		#print "you got here3"
		#check for factors
		if (num % i == 0):
			#its a factor
			
			if (i > biggest_Prime and isPrime(i) == True):
				biggest_Prime = i
				i += 2
			if (num/i > biggest_Prime and isPrime(num/i) == True):
				biggest_Prime = num/i
				i += 2
			else:
				i +=2
		else:
			#skips checking even numbers
			i +=2
	else:
		return biggest_Prime
# solves problem 4
def problem4():
	# write your code below for this problem (and remove this comment...)
	return True

# the main part of the program

sol3 = problem3()
print time.time()- startTime
print "The largest prime factor of the number 600851475143 is {}".format(sol3)
sol4 = problem4()
print "The largest palindrome made from the product of two 3-digit numbers is {}".format(sol4)
