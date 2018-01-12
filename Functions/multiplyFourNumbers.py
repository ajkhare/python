# !/usr/bin/python
# Assignment : parameter passing, multiply 2,3,4,5 numbers

def mult(a,b,c=1,d=1,e=1):
	return (a*b*c*d*e)
	
def main():
	print(mult(2,3))
	print(mult(2,3,4))
	print(mult(2,3,4,5))
	print(mult(2,2,2,2,2))
	
if __name__=='__main__':
	main()