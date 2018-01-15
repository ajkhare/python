# !/usr/bin/python
# Assignment : Find GCD of 2 number

def findGCD(no1,no2):
	if(no1 != no2):
		if(no1 > no2):
			return findGCD(no1-no2,no2)
		else:
			return findGCD(no1,no2-no1)
	else:
		return no1

def findLCM(no1,no2):
	global orgno1 
	global orgno2
	global cntno1 
	global cntno2
	'''
	orgno1 = no1
	orgno2 = no2
	cntno1 = 2
	cntno2 = 2
	'''
	#print (orgno1,orgno2)
	while(no1 != no2):
		if(no1 < no2):
			no1 = orgno1 * cntno1
			cntno1 += 1
		else:
			no2 = orgno2 * cntno2
			cntno2 += 1
	
	print(no1)
	print(no2)

	
def recursivefindLCM(no1,no2):
	print ("INCOMPELTE PROGRAM")
	global orgno1 
	global orgno2
	global cntno1 
	global cntno2
	'''
	orgno1 = no1
	orgno2 = no2
	cntno1 = 2
	cntno2 = 2
	'''
	#print (orgno1,orgno2)
	while(no1 != no2):
		if(no1 < no2):
			print(no1,no2)
			return recursivefindLCM(orgno1*cntno1,no2)
			cntno1 += 1
		else:
			return recursivefindLCM(no1,orgno2 * cntno2)
			cntno2 += 1
	else:
		return no1
	
	
orgno1 = 1
orgno2 = 1
cntno1 = 2
cntno2 = 2
	
def main():
	global orgno1
	global orgno2
	
	no1 = eval(input("Enter number 1 : "))
	no2 = eval(input("Enter number 2 : "))
	print("GCD of {} , {} is : ".format(no1,no2) + str(findGCD(no1,no2)))
	
	orgno1 = 35
	orgno2 = 14
	findLCM(35,14)
	recursivefindLCM(35,14)
	
if __name__=='__main__':
	main()