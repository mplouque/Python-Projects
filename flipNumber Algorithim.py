num =786465432156516551 
forwards = num
backwards = 0

while num > 0:
	backwards = (backwards * 10) + (num % 10)
	num = num / 10

print "{} backwards is {}".format(forwards, backwards)