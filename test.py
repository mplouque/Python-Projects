#######################################
# Name: Pablo Johnson
# Date: 2.1.2016
# Description: Project Euler Solution 7
#######################################
import time, math
t = time.time()
            
def S():
    global list1
    list1 = [2]
    i = 3
    while True:
        if all(((i % x) != 0) for x in list1):
             list1.append(i)
        i += 2
        if (len(list1) == 10001):
            return list1[-1]

sol1 = S()
print sol1
#print list1
print time.time() - t