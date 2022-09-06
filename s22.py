def maximum(a, b, c):

	if (a >= b) and (a >= c):
		greatest = a

	elif (b >= a) and (b >= c):
		greatest = b
	else:
		greatest = c
		
	return greatest



a = 45
b = 34
c = 16
print(maximum(a, b, c))
