# !/usr/bin/python
# Assignment : swapped given bits between x and y

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
		#x = ~x	
		return no|x
		
def myFunction(x,y,pos,nob):
	'''	e.g. x = 011011001, y=011000110, pos=5, nob=4
	
		Step 1) find xpart and ypart	
		then xpart = 000011000, ypart = 000000110
		
		To find xpart,
	'''
	xon = turnonBits(x,pos,nob)
	yon = turnonBits(y,pos,nob)
	
	#to Find xpart, ypart we need 
	# x1 = 000011110, y1=000011110
	if (nob <= pos):
		x1 = (1<<nob)-1
		x1 = x1 << (pos-nob)
	
	xpart = x & x1
	
	if (nob <= pos):
		y1=(1<<nob)-1
		y1 = y1 << (pos-nob)

	ypart = y & y1
	
	# TurnOff bits
	xoff = turnoffBits(x,pos,nob)
	yoff = turnoffBits(y,pos,nob)
	
	# Swap xpart and ypart with actual x and y&turnonBits
	xresult = xon | ypart
	yresult = yon | xpart
	
	print("xresult = : {}".format(xresult))
	print("yresult = : {}".format(yresult))
	

def main():
	x = eval(input("Enter value X : "))
	y = eval(input("Enter value Y : "))
	position = eval(input("Enter Position : "))
	noOfBits = eval(input("Enter No of Bits : "))
	
	x = turnoffBits(x,position,noOfBits)
	y = turnoffBits(y,position,noOfBits)
	
	xpart=x&turnonBits(x,position,noOfBits)
	ypart=y&turnonBits(y,position,noOfBits)
	
	x = x&ypart
	y = y&xpart
	
	print(x)
	print(y)
	
	myFunction(x,y,position,noOfBits)
	
if __name__=='__main__':
	main()