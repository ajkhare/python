# !/usr/bin/python
# Assignment : parameter passing, add 2,3,4,5 numbers

def addFourParams(a,b,c=0,d=0,e=0):
	return a+b+c+d+e

def varArguments(*args):
	print(type(args))
	for x in args:
		print(x)
	
def main():
	print(addFourParams(10,20))
	print(addFourParams(10,20,30))
	print(addFourParams(10,20,30,40))
	print(addFourParams(10,20,30,40,50))

	print(varArguments(1,2,3,4))
	print(varArguments(1,2,3,4,"hi","bye"))
	
if __name__=='__main__':
	main()