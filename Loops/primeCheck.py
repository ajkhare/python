# !/usr/bin/python
# Assignment : Find prime number or not from given range of numbers
import math

def checkPrime(number):
	
	# Convert negative number to positive
	if(number < 0):
		number *= -1
	
	# Optimization 1
	if (number % 2 == 0):
		return False
		
	uc = int(number/2)
	
	# Optimization 2
	#for x in range(3,uc+1,2):
	#	if (number % x == 0):
	#		return False
	#return True
	
	# Optimization 3
	for x in range(3,int(math.sqrt(number))+1,2):
		if (number % x == 0):
			return False
	return True


def main():
	
	# Enter range from which you want to extract the prime numbers
	lower = eval(input("Enter lower level range : "))
	higher = eval(input("Enter higher level range : "))
	for i in range(lower,higher+1):
		if(checkPrime(i)):
			print("{} is prime number".format(i))
		else:
			print("{} is not prime number".format(i))


if __name__=='__main__':
	main()

