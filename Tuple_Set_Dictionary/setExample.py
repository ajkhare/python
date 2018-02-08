# !/usr/bin/python
# Assignment : Set example

def main():
	x=set([1,2,3,4,5])
	y=set([4,5,6,7,8])
	
	print(x.difference(y))
	print(y.difference(x))
	
	# Original x and y are not changed
	print(x)
	print(y)
	
	# Original x is updated
	print(x.difference_update(y))
	print(x)
	
	
	
if __name__=='__main__':
	main()
	
	