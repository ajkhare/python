#!/usr/bin/python
# Assignment : Check number is divisible by 8 without using division

def checkdivisibleByEight(no):
	return (no&7)
	
def main():
	no1 = eval(input("Enter a Number : "))
	if(checkdivisibleByEight(no1) == 0):
		print("Ohh! You have entered divisor of 8")
	else:
		print("Sorry not a divisor of 8")


if __name__=='__main__':
	main()
