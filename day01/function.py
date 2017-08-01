# -*- coding: utf-8 -*-

# n1 = 255
# n2 = 1000
# n3=hex(n2)
# print (str(n3))


import math
def qua(a,b,c):
	m=math.sqrt(b**2-4*a*c)
	x1 =(-m-b)/(2*a)
	x2 =(m-b)/(2*a)
	return x1,x2
x1, x2 =qua(1,3,-4)
print (x1,x2)