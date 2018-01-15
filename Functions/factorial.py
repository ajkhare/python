# !/usr/bin/python
# Assignment : Factorial of number

def factorial(number):
	result = 1
	while(number != 1):
		result = result * number
		number -= 1
	return result

def recursiveFactorial(number):
	if(number != 1):
		return number * recursiveFactorial(number - 1)
	else:
		return 1
	
def main():
	number = eval(input("Enter a number : "))
	print(factorial(number))

	number = eval(input("Enter a number : "))
	print(recursiveFactorial(number))

if __name__=='__main__':
	main()

