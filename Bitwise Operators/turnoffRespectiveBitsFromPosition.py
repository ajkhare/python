# !/usr/bin/python
# Assignment : Accept number, position, no of bits to be turned off. Turn off respective bits from given position


def turnoffBits(no,pos,noofBits):
	if (noofBits <= pos):
		x=(1<<noofBits)-1
		x = x << (pos-noofBits)
		x = ~x
		return no&x

def turnonBits(no,pos,noofBits):
	if (noofBits <= pos):
		x=(1<<noofBits)-1
		x = x << (pos-noofBits)
		return no|x

def toggleBits(no,pos,noofBits):
	if (noofBits <= pos):
		x=(1<<noofBits)-1
		x = x << (pos-noofBits)
		return no^x

def main():
	number = eval(input("Enter number : "))
	position = eval(input("Enter Position : "))
	noOfBits = eval(input("Enter No of Bits : "))
	
	# 1) 2 ** (no of bits -1)
	x=(2**noOfBits)-1
	#print(x)
	#x=(1<<noOfBits)-1
	
	# 2) x = x << (pos-noOfBits) 
	x = x <<(position-noOfBits)
	#print(x)
	
	# 3) x = ~x
	x = ~ x
	#print(x)
	
	# 4) number = number & x
	number = number & x
	print(number)

	print(turnoffBits(number,position,noOfBits))
	print(turnonBits(number,position,noOfBits))
	print(toggleBits(number,position,noOfBits))
	
if __name__=='__main__':
	main()