# !/usr/bin/python
# Assignment : Implement Stack and check given maths expression do have balance paranthesis

# Stack related functions
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
	
	expr = input("Enter mathematical expression : ")
	for x in expr:
		#print(x)
		if(x in ['(','{','[']):
			push(stack,x)			# push if openeing bracket found
			#print(stack)
		elif(x in [')','}',']']):
			popBracket=pop(stack)
			#print(popBracket)
			if((popBracket == '(' and x != ')') or (popBracket == '[' and x != ']') or (popBracket == '{' and x != '}')):
				print("Given expression is not balanced")
				break
	else:
		print("Given expression is balanced")
	
		
if __name__=='__main__':
	main()