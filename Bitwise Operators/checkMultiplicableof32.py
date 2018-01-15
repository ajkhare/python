#!/usr/bin/python
# Assignment : Check number is multiplicable of 32 without using multiplication

def checkDivisibleof32(no):
	return (no & 31)

def main():
	no1 = eval(input("Enter a number : "))
	if(checkDivisibleof32(no1) == 0):
		print("Ohh! You have entered multiplier of 32")
	else:
		print("Sorry not a multiplier of 32")

if __name__=='__main__':
	main()