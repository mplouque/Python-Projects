list1 = range(1,101)
print list1

def foo (n):
	num = n % 100
	return num
	
list1 = map(foo, list1)
print list1
	#list comprehension
list2 = [x%100 for x in range(1,101)]
print list2

#sets
