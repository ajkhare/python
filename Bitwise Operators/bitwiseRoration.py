#!/usr/bin/python
# Assignment : Right/Left Rotation in bitwise operators

def main():
	no1 = eval(input("Enter any number :"))
	option = eval(input("For Right Rotation enter 1, For Left Rotation enter 0 : "))
	count = eval(input("Enter rotation value : "))
	
	if(option == 1):
		print("After right roration answer is : %d " % (rightRotation(no1,count)))
	else:
		print("After left roration answer is : %d " % (leftRotation(no1,count)))

def rightRotation(number,counter):
	return (number >> counter)

def leftRotation(number,counter):
	return (number << counter)
	
if __name__=='__main__':
	main()