# !/usr/bin/python
# Assignment : parameter passing, add n numbers

def addn(*args):
	print(type(args))
	sum = 0
	for x in args:
		sum += x
	
	return sum

def main():
	print(addn(1,2,3,4,5,6,7,8,9,10))
	print(addn(2,2,2,2))
	print(addn(1,1,1,1,1))
	print(addn(2))
	print(addn(2,2))
	
if __name__=='__main__':
	main()