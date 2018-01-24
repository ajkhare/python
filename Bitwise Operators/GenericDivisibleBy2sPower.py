# !/usr/bin/python
# Assignment : Check number is divisible by 2's power

def count1sBits(divisor):
	x = 1
	one_cnt = 0

	while(divisor > 0):
		if (divisor & x):
			one_cnt+=1
		divisor = divisor >> 1
	
	return one_cnt
	
	
def findIfNumberIs2sPower(divisor):
	if(count1sBits(divisor)):
		return True
	else:
		return False

def Generic2sPowerDivisibilityTest(no,divisor):
	if(no&(divisor-1)==0):
		return True
	else:
		return False

def main():
	print("Check 32 is power of 2 : {}".format(findIfNumberIs2sPower(32)))
	print("Check 64 is divisible by 8 : {}".format(Generic2sPowerDivisibilityTest(64,8)))
	print("Check 60 is divisible by 16 : {}".format(Generic2sPowerDivisibilityTest(60,16)))
	print("Check 256 is divisible by 64 : {}".format(Generic2sPowerDivisibilityTest(256,64)))
	print("Check 2201 is divisible by 64 : {}".format(Generic2sPowerDivisibilityTest(2201,64)))
	print("Check 304 is divisible by 128 : {}".format(Generic2sPowerDivisibilityTest(304,128)))
	
if __name__ == '__main__':
	main()