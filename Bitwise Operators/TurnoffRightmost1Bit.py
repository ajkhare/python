# !/usr/bin/python
# Assignment : Turn off given number's right most 1 bit to 0

# NOT Working Logic
def turnOffRightMost1Bit(no):
	result=0
	counter=0
	# Check is no != 0
	if(no!=0):
		#While we found result = 1, i.e. Find which right most bit is 1
		# e.g no = 1100, counter = 3 (i.e. 3rd right most bit is first set to 1)
		while(result==0):
			result = no & 1
			no = no >> 1
			counter+=1
		
		#Generate  number 0100, i.e. 2**(3-1)
		temp1 = 2**(counter-1)
		print("temp1 = {}".format(temp1))
		
		#Generate number 1011, i.e. take 1's complement of the above number and and it with original number
		#return (no & ~temp1)
		result = no&~temp1
	else:
		print("Number is not a valid")
	print("Result = {}".format(result))
	return result
	
	
# Working Logic
def turnOffRightMost1Bit2(no):
	result=0
	counter=0
	x=1
	# Check is no != 0
	if(no!=0):
		#While we found 1100 & 1 = 0
		# run the loop till we get the x = 0100 , i.e. x will be 1,2,4,8,16,32,... and so on
		while((no&x)==0):
			#counter+=1
			# Move x to 2,4,8,16 ...
			x = x << 1
		
		print(x)
		
		#Generate number 1011, i.e. take 1's complement of the above number and and it with original number
		#print(~x)
		result = no & ~x
	return result
	
	
# Working Logic	
def main():
	no = eval(input("Enter a number : "))
	counter = 0
	x = 1
	if(no != 0):
		while((no&x)==0):
			counter+=1
			x = (x << 1)
	print("x = {}".format(x))
	result = no & ~x
	print(result)
	
	print(turnOffRightMost1Bit(no))
	#print(turnOffRightMost1Bit2(no))
	
	
	
	
if __name__=='__main__':
	main()