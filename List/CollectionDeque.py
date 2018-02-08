# !/usr/bin/python
# Assignment : Implementation on collections on deque, for doubly ended queue

import collections


def appendDeque(x,element):			# Add Element to the right side
	x.append(element)

def extendDeque(x,element):
	x.extend(element)

def appendLeftDeque(x,element):
	x.appendleft(element)
	
def extendLeftDeque(x,element):
	x.extendleft(element)
	
def popDeque(x):
	return x.pop()
	
def popLeftDeque(x):
	return x.popleft()

def main():
	x = collections.deque()
	choice = 1
	while(True):
		print("*********** Menu *********** \
			\n1) Add Element to left\
			\n2) Remove Element to right\
			\n3) Remove Element from left\
			\n4) Remove Element from right\
			\n5) Print\
			\n6) Exit")
		
		choice=eval(input("Enter Choise : "))
		
		if(choice==1):
			element=input("Enter element to push : ")
			appendDeque(x,element)
		elif(choice==2):
			element=input("Enter element to push : ")
			appendLeftDeque(x,element)
		elif(choice==3):
			print(popLeftDeque(x))
		elif(choice==4):
			print(popDeque(x))
		elif(choice==5):
			print(x)
		else:
			break
	
     
if __name__=='__main__':
	main()