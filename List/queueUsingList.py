# !/usr/bin/python
# Assignment : Implement Queue using List

def printQueue(queue):
	print(queue)
	
def isFull(queue):
	if(len(queue)>=100):
		print("Queue is full, cannot insert new element")
		return True
	return False

def isEmpty(queue):
	if(len(queue)==0):
		print("Queue is empty, cannot remove any element")
		return True
	return False

# if(!isFull(queue))    -> This does not work, why
def insertElement(queue,element):
	if(not isFull(queue)):
		queue.append(element)

def removeElement(queue):
	if(not isEmpty(queue)):
		return queue.pop(0)

def main():
	choice=1
	queue = []
	while(True):
		print("*********** Menu *********** \
			\n1) Add Element\
			\n2) Remove Element\
			\n3) Print Queue\
			\n4) Exit")
		choice = eval(input("Enter Choise : "))
		if(choice==1):
			element=input("Enter element to push : ")
			insertElement(queue,element)
			
		elif(choice==2):
			print(removeElement(queue))
			
		elif(choice==3):
			printQueue(queue)
			
		else:
			break
		

if __name__=='__main__':
	main()