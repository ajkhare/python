# !/usr/bin/python
# Assignment : Find result of equation "4+44+444+4444" or "5+55+555+5555+55555"

def menu():
	print("1) Enter number you want to calculate\
			\n2) Enter 2 to Exit")
	choice = input("Enter choice : ")
	return choice
	

def findResult(no):
	cnt = 1
	sum = 0
	while(cnt<=no):
		internalCnt = 0
		while(internalCnt < cnt):
			sum = sum + (no*(10**(internalCnt)))
			internalCnt+=1
		cnt += 1
	return sum
	
	
def main():
	choice=menu()
	while(choice!='2'):
		no = eval(input("Enter number : "))
		result = findResult(no)
		print("Result is : {}".format(result))
		
		choice=menu()
	
if __name__=='__main__':
	main()
