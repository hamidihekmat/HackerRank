def binary(n):
	stack = ""
	while n > 0:
		remainder = n % 2
		stack += str(remainder)
		n = n//2
		if remainder < 0:
			break
	stack_list = stack.split('0')
	return max(map(len,stack_list))

if __name__ == "__main__":
	n = int(input())
	print(binary(n))
