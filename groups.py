n = input()

def G(n):
	if (n==1):
		return 0
	else: 
		return (n-1)+G(n-1)
print G(n)
print "students\tgroups"
for i in range (1, n+1):
	print "{}\t\t{}".format(i, G(i))
	