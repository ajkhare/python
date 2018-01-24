# !/usr/bin/python
# Assignment : Implement Stack using List

def isFull(stack):
	if(stack.__len__() >= 100):				# or len(stack) can be used
		print("Stack is full, cannot insert new element")
		return True
	return False
	
	
def isEmpty(stack):
	if(stack.__len__() == 0):				# or len(stack) can be used
		print("Stack is empty, cannot pop any element")
		return True
	return False


# adding list through extend is not working
# How to accept list in input
def push(stack,element):
	if(isFull(stack)==False):
		if(type(stack) is list):
			stack.extend(element)
		else:
			stack.append(element)
	
	
def pop(stack):
	if(isEmpty(stack)==False):
		return stack.pop()

		
def printStack(stack):
	print(stack)


def dummy(cnt):
	print("Inside dummy : cnt = {}".format(cnt))
	cnt = 100
	print("Inside dummy : cnt = {}".format(cnt))
	
	
def main():
	stack = []
	choice = 1
	cnt = 10
	print("Inside main : cnt = {}".format(cnt))
	dummy(cnt)
	print("Inside main : cnt = {}".format(cnt))
	
	while(True):
		print("************** Menu **************\
			\n1) Push Element\
			\n2) Pop Element\
			\n3) Print Stack\
			\n4) Exit")
		
		choice=eval(input("Enter Choise : "))
		
		if(choice==1):
			element=input("Enter element to push : ")
			push(stack,element)
		elif(choice==2):
			print(pop(stack))
		elif(choice==3):
			printStack(stack)
		else:
			break
		
if __name__=='__main__':
	main()