# !/usr/bin/python
# Assignment : Menu driven calculator
import sys

def add(x,y):
	return x+y

def substraction(x,y):
	return x-y

def multiply(x,y):
	return x*y
	
def division(x,y):
	return x/y
	
def main():
	option = 0
	while(option != 5):
		print("Enter Option\n1 : Add\n2 : Substract\n3 : Multiply\n4 : Divide\n5 : Exit")
		option = eval(input("Enter Value : "))
		if(option == 5):
			sys.exit()
		
		x = eval(input("Enter 1st number : "))
		y = eval(input("Enter 2nd number : "))
		
		if(option == 1):
			print("Sum is = {}".format(add(x,y)))
		elif(option == 2):
			print("Substraction is = {}".format(substraction(x,y)))
		elif(option == 3):
			print("Multiplication is = {}".format(multiply(x,y)))
		elif(option == 4):
			print("Division is = {}".format(division(x,y)))

if __name__=='__main__':
	main()
