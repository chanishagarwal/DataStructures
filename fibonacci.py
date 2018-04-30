def rec_fibonacchi(n):
	if n == 0:
		return 0
	elif n == 1:
		return 1

	else:
		return (fibonacchi(n-1) + fibonacchi(n-2))


F = [0,1]
def dp_fibonacchi(n):
	global F
	# print(F)
	if n < 0:
		return 'Wrong input'
	elif n < len(F):
		return F[n]
	elif n == len(F):
		sum = F[n-1] + F[n-2]
		F.append(sum)
		return sum
	else:
		return(dp_fibonacchi(n-1) + dp_fibonacchi(n-2))
		# return(dp_fibonacchi(n-1) + dp_fibonacchi(n-2))

	
	# return sum(F)



if __name__ == '__main__':
	# print nth fibonacchi number
	n = int(input('Enter a number: '))
	# print(rec_fibonacchi(n))
	print(dp_fibonacchi(n))
