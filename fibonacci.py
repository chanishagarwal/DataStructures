def fibonacchi(n):
	if n == 0:
		return 0
	elif n == 1:
		return 1

	else:
		return (fibonacchi(n-1) + fibonacchi(n-2))


if __name__ == '__main__':
	# print nth fibonacchi number
	n = input('Enter a number: ')
	print(fibonacchi(n))