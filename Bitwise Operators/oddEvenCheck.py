#!/usr/bin/python
# Assignment : Check number is odd or even without using mod operator

def main():
	number = eval(input("Enter number to be checked : "))
	if (number & 1):
		print("Odd Number")
	else:
		print("Even Number")

if __name__=='__main__':
	main()