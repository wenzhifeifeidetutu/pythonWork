import math

def my_sqrt(a, b):
	number = a**(2) + b**(2)
	return(math.sqrt(number))


def E(a, b):
	number_a = a/my_sqrt(a, b)
	number_b = b/my_sqrt(a, b)

	print("a is "+ a + ", b is " +b)


	
