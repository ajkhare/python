# !/usr/bin/python
# Assignment : Variable Argsuments demo

def varArgsDict(a,b,c,*args,**kwargs):
	print(a,b,c)
	print(type(args))
	for x in args:
		print(x)
	
	print(type(kwargs))
	for key in kwargs:
		print(key,kwargs[key])
	
def varArgsDict2(a,b,c,**kwargs):
	print(a,b,c)
	
	print(type(kwargs))
	for key in kwargs:
		print(key,kwargs[key])

def main():
	varArgsDict(1,2,3,4,5,6,name='ajinkya',dept='manufacturing',id='200')
	varArgsDict(1,2,4,name='ramesh',dept='manufacturing',id=200,password='****')
	varArgsDict(1,2,5,name='ramesh',dept='manufacturing',id=200,password='****',country='India')
	
	varArgsDict2(1,2,4,name='ramesh',dept='manufacturing',id=200,password='****')
	varArgsDict290(1,2,5,name='ramesh',dept='manufacturing',id=200,password='****',country='India')
	
if __name__=='__main__':
	main()