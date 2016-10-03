###########################################################################################
# Name: Matthew Louque
# Date: 2/4/2016
# Description: Solves Project euler problems 3&4
###########################################################################################

# it may help to make use of some math functions (which you can import)
import math
# it may also help to define other "helper" functions (i.e., delegate tasks!)
def isPrime(n):
	#check if prime
	#if prime return true
	#if not prime return false
	if (n <= 2):
		return True
	if (n % 2 == 0 and n > 2): 
		return False
	for i in range(3, int(math.sqrt(n)) + 1, 2):
		if (n % i == 0):	
			return False
	return True
def isPalindrome(num):
	forwards = num
	backwards = 0
	#creates the inverse of a number and assigns it to backwards. 123 become 321 etc.
	while (num > 0):
		backwards = (backwards * 10) + (num % 10)
		num = num / 10
	if (forwards == backwards):
		#its a palindrome
		return True
	else:
		#its not a palindrome
		return False
# solves problem 3
def problem3():
	num=600851475143
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
	maxPalindrome = 0
	#starts at 999 for the first multiple and counts down by one when the other loop reaches 100
	for firstMultiple in xrange(999, 99, -1):
		#starts at 999 for the secondMultiple and counts down by 1 until it reaches 100
		for secondMultiple in xrange(999, 99, -1):
			#generates anumber by multiplying the firstmultiple by the second multiple
			number = firstMultiple * secondMultiple
			#if number is a palindrome set palindrome = to true, else false
			palindrome = isPalindrome(number)
			#if number is a palindrome set it to tempPalindrome then check if tempPalindrome is the largest palindrome so far
			if (palindrome == True):
				tempPalindrome = number
				if (tempPalindrome > maxPalindrome):
					maxPalindrome = tempPalindrome
	return maxPalindrome #when the loops are done, return the largest palindrome found
				

# the main part of the program
sol3 = problem3()
print "The largest prime factor of the number 600851475143 is {}".format(sol3)
sol4 = problem4()
print "The largest palindrome made from the product of two 3-digit numbers is {}".format(sol4)
