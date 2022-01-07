#Trailing zero's in factorial of N

import math

def factorial(n):
	value = 1
	for i in range(2, n+1):
		value *= i
	return value

def get_trailing_zero(n):
	#logic breaks for big numbers
	count = 0
	fact = factorial(n)
	print(fact)
	while fact > 0:
		if (fact % 10 == 0):
			count += 1
			fact /= 10
		else:
			break
	return count


def get_trailing_zero_log(n):
	count = 0
	power = 1
	while power < n:
		count += math.floor(n/(5**power))
		power += 1 
	return count


n = 20
print(get_trailing_zero(n))
print(get_trailing_zero_log(n))