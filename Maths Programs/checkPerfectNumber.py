# !/usr/bin/python
# Assignment : Check if number is perfect number of not

def factorial(number):
	result = 1
	while(number != 1):
		result = result * number
		number -= 1
	return result

def checkPerfect(number):
	sum=0
	orgNumber = number
	while(number!=0):
		digit = number%10
		sum = sum + factorial(digit)
		number = number//10
	
	print("sum = {}".format(sum))
	if(sum == orgNumber):
		return 1
	else:
		return 0
	

def menu():
	print("1) Enter number you want to check\
			\n2) Enter 2 to Exit")
	choice = input("Enter choice : ")
	return choice
	
def main():
	choice=menu()
	
	while(choice!='2'):
		if(choice=='1'):
			number = eval(input("Enter number : "))
			if(checkPerfect(number)):
				print("It's perfect number")
			else:
				print("Not a perfect number")
		elif(choice=='2'):
			break
		choice=menu()


if __name__=='__main__':
	main()