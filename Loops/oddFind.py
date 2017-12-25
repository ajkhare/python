#!/usr/bin/python
# Assignment : Find odd numbers from given range

def oddFinder(start,end):
	oddCount = 0
	while(start != end):
		if (start & 1):		#answer is 1 if number is odd
			oddCount += 1
			print("odd number is : {}".format(start))
		start += 1
	
	print("total Odd numbers are : {}".format(oddCount))


def main():
	start = eval(input("Enter start range : "))
	end = eval(input("Enter end range : "))
	
	# Validate start and end values
	if(end < start):
		print("Invalid start and end")
		return
	oddFinder(start,end)
	

if __name__=='__main__':
	main()