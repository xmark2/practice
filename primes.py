import math

def is_prime(n):
	if n%2==0 and n>2:
		return False
	return all(n%x for x in range(3,int(math.sqrt(n))+1,2))

if __name__=="__main__":

	num = 9
	print(is_prime(num))
	# List all the primes till the given number
	primes = [x for x in range(1,20) if is_prime(x)]
	print(primes)

