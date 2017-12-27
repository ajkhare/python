# !/usr/bin/python
# Assignment : Sum of all odd numbers from given range


def checkOdd(number):
	if(number & 1):
		return True
	else:
		return False

def main():
	start = eval(input("Enter starting range : "))
	end = eval(input("Enter ending range : "))
	sum = 0
	
	while (start != end+1):
		if(checkOdd(start)):
			sum += start
		start += 1
	
	print("Sum of all odd numbers in given range is : {}".format(sum))
	
if __name__=='__main__':
	main()