# !/usr/bin/python
# Assignment : List comprehension to generate tables for given range
	
def main():
	lb=10
	ub=20
	
	print([[x*i for i in range(1,11)] for x in range(lb,ub+1)])
	
	
if __name__=='__main__':
	main()
	