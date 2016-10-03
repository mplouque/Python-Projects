###########################################################################################
# Name: Matthew Louque
# Date: 1/11/2016 10:21
# Description: This program calculates the number of zeros written from one to one million.
###########################################################################################

n = 0
count = 0
zeros = 0
#calculate the number of zeros in the current number
def findzeros(n):
    zeros = 0
    while (n != 0):
		if (n % 10 == 0):
			zeros +=1
		n = n/10
    return zeros
#repeat until num > 1mill
while (n < 1000000 ):
	#next number
	n +=1
	#get zeros from current num
	zeros = findzeros(n)
	#add that number to the total number of zeros
	count += zeros
#print count

print "The number of zeroes between 1 and 1 million is {}".format(count)

'''
__author__ = "Abhishek"

import logging, time
logging.basicConfig(level= logging.DEBUG, format = "%(asctime)s- %(levelname)s - %(message)s")
#logging.disable(logging.CRITICAL)
start = time.time()                     # starting point for time

#Main Code
total_zeroes = 0                        # accumulates total number of zeroes
for i in range(1, 1000000 + 1):
    total_zeroes += str(i).count("0")   # counts number of zeros in the number


end = time.time()
logging.debug(end-start)                # prints the time taken to run program 

print "The number of zeros written from 1 to 1 million is %d" % total_zeroes
'''