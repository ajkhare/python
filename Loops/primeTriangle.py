# Display tringle of prime numbers
import primeCheck


def getNextPrime(chkNumber):
	while(not (primeCheck.checkPrime(chkNumber))):
		chkNumber += 1
	return chkNumber

	
def main():
	rows = eval(input("Enter Number of Rows : "))
	chkNumber = 1
	for i in range(rows):
		for j in range(i+1):
			# get next prime number
			no = getNextPrime(chkNumber)
			chkNumber = no + 1
			print("{} ".format(no),end='')
		print("\n",end='')


if __name__=='__main__':
	main()


