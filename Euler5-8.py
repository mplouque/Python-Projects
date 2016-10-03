###########################################################################################
# Name: Matthew Louque
# Date: 
# Description: 
###########################################################################################

# it may help to make use of some math functions (which you can import)
import math, time
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

# solves problem 5
def problem5():
	#list of numbers we need to check can be shortened. Numbers that have common factors dont need to be checked.
	#For example, when we check if the number is divisible by 20 then it is also divisible by 10, 5, 4, and 2. As such we do not need to check for them.
	#Also if two numbers lcm is divisble by another number remove that number from the list as well. (15, 12)
	list = [20, 19 , 18, 17, 16, 14, 13, 11,]
	#we can start at 2520 while iterating and step up by 2520 because a number that is evenly divisble by the first 20 nums will also be evenly divisble by the nnumber that is evenly divisble by the first 10 numbers
	for num in xrange(2520, 999999999, 2520):
		# if the current number is evenly divisble by all the numbers in our shortened list return that number. 
		#else iterate up and try again 
		if all(num % f == 0 for f in list):
			return num
	#in case the number doesnt fit within a 32bit integer
	return "Couldnt find a number"
		
# solves problem 6
def problem6():
	#the sum of all the square
	square_num = 0
	#the sum of 1-100
	sum_num = 0
	for i in xrange(1, 101):
		#set square_num = to the curent square num plus the square of the current number in the for loop
		square_num += (i*i)
	
	for i in xrange(1,101):
		#add the current number(i) to sum_num
		sum_num += i
		
	#square the sum of the numbers from 1-100	
	sum_num = sum_num * sum_num
	#return the square of the sum minus the sum of the squares
	return sum_num - square_num
	
# solves problem 7
def problem7():
	#i is the number of primes found so far
	#start i at one because 2 is the first prime number
	i = 1
	#tempnum is going to be the current prime number
	tempNum = 3
	while (i <= 10001):	
		#if the temp number is prime
		if (isPrime(tempNum)):
			i+=1
			#ensures that tempNum is not incremented by 2 if i is the 10001st prime
			if (i >=10001):
				break
			
			#increase the temp number by two to check it again
			tempNum +=2
			
			#a prime was found so increase the number of primes by 1
			
		else:
			#increase the temp number by two to check again
			tempNum+=2
		

	#when you get the 10001 prime return that number
	return tempNum
# solves problem 8
def problem8():
	
	list = []
	#the number im looking through
	stringNum = "7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450"
	#makes each individual char of the string become an int, and then adds it to the empty list 
	for a in stringNum:
		list.append(int(a))
	greatestProduct= 1
	# as long as the length of the list is longer than 13 multiple 13 digits together
	#dont need to check the last 13 because their is a zero so it cannot be the greatest number
	while (len(list) >13):
		#set i = to 1 at the start of each iteration through the list
		i = 1
		#for each element in the first 13 elements in the list
		for a in list[0:13]:
			
			if (a != 0):
				#If none of the 13 digits are zero multiply the current digit times i and set i = to that
				i *= a
			#if one of the digits is zero, break because the number will = zero	
			else:
				break
		# if i is the greatest product found set it to greatest product
		if (i > greatestProduct):
			greatestProduct = i
		#remove the first element from the list
		list.pop(0)
	#when the length of the list is less than 13 return the largest product
	else:
		return greatestProduct
	
	
# the main part of the program
sol5 = problem5()
print "The smallest positive number that is evenly divisible by all of the numbers from 1 to 20 is {}".format(sol5)
sol6 = problem6()
startTime = time.time()
print "The difference between the sum of squares and square of sum of the first 100 natural numbers is {}".format(sol6)
sol7 = problem7()
print "The 10,001st prime number is {}".format(sol7)
sol8 = problem8()
print "The greatest product of thirteen adjacent digits is {}".format(sol8)