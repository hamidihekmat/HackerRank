#usr/bin/env python3


fibonacci_cache = {}


def fibonacci(n):
	# If we have the value, then return it
	if n in fibonacci_cache:
		return fibonacci_cache[n]
	# compute the Nth term

	if n == 1:
		value = 1
	elif n == 2:
		value = 1
	elif n > 2:
		value = fibonacci(n-1) + fibonacci(n-2)

	# cache the value and return it

	fibonacci_cache[n] = value
	return value


for n in range(1, 1000):
	print(n, ":", fibonacci(n))