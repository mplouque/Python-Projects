###########################################################################################
# Name: Matthew Louque
# Date: 1/23/2016
# Description: Solves Project Euler Problems 1 & 2
###########################################################################################

# solves problem 1
def problem1():
	#declare needed vars
	num3 = 0
	sum3 = 0
	num5 = 0
	sum5 = 0
	finalSum=0
	#increment num3 by 3 repeatedly to increase it by multiples of three
	while (num3 < 1000): 
		#if num 3 ends in a 5 or 0 take it out of the addition to the sum3 because it will be added during the calculations of multiples of 5
		if (num3 % 5 !=0): 
			sum3 += num3			
		#increment num3
		num3 += 3
	#increment num5 by 5 repeatedly to increase it by multiples of five
	while (num5 < 1000): 
		sum5 += num5
		num5 +=5
	finalSum = sum3 + sum5
	return finalSum
# solves problem 2
def problem2():
	fibNum = 1
	fibNumPrev = 0
	fibTemp= 0
	fibSum = 0
	#if the current fibNum is less than 4 mill 
	while (fibNum < 4000000):
		#store the current fib num in fibTemp to set fibNumPrev equal to the original fibNum after calculations
		#ie. fibNum =2, sets fibTemp =2 so i can later set fibNumPrev = the original fibNum, 2 
		fibTemp = fibNum
		#only increase the Sum of the numbers if the current fibNumber is even
		if (fibNum % 2 == 0):
			fibSum +=fibNum
		#this is used to stop the fibNUmber from getting higher than 4 mill after the calculation, otherwise it would go above
		if (fibNum+fibNumPrev < 4000000):
			fibNum= fibNum+fibNumPrev
			#sets fibNumPrev to the previous fibNum which was earlier stored in fibTemp
			fibNumPrev = fibTemp
		#once the fibNum gets above 4 million, return the sum of the even numbers
		else:
			return fibSum
		#print fibNum
	

# the main part of the program
sol1 = problem1()
print "The sum of all the multiples of 3 or 5 below 1000 is {}".format(sol1)
sol2 = problem2()
print "The sum of the even-valued Fibonacci terms not exceeding four million is {}".format(sol2)
