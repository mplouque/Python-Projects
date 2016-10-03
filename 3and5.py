num3 = 0
sum3 = 0
num5 = 0
sum5 = 0
finalSum=0
#increment num3 by 3 repeatidly to increase it by multiples of three
while (num3 < 1000):
	global num3 
	#if num 3 ends in a 5 or 0 take it out of the addition to the sum3 because it will be added during the calculations of multiples of 5
	if (num3 % 5 !=0):
		global sum3 
		sum3 += num3
		
	else:
		
		#print("you made it here")
	#increment num3
	num3 += 3
else: 
	#not sure if i need this, better be safe
	donewith3= True
#increment num5 by 5 repeatidly to increase it by multiples of five
while (num5 < 1000):
	global num5 
	global sum5 
	sum5 += num5
	num5 +=5
else:
	donewith5 = True
#if the while loops are done calculate the sum
if (donewith3 == True and donewith5 == True):
	global finalSum 
	finalSum = sum3 + sum5
	print finalSum