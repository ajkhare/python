# !/usr/bin/python
# Assignment : Implement readlines(no) function


def readlines(fd,no):
	strBuffer=""
	cnt=1
	while (cnt <= no):
		line=fd.readline()
		#print(line)
		if(line==''):			# Break Loop
			break
		strBuffer = strBuffer + line
		if(cnt==no):
			print("**************** Next 'n' lines are ****************")
			print(strBuffer)
			cnt=1
			strBuffer=""
			#break
		else:
			cnt += 1

			
def openFile(fileName):
	fd=open(fileName)
	return fd

	
def main():
	fileName = input("Enter File Name : ")
	fd=openFile(fileName)
		
	readlines(fd,4)

if __name__=='__main__':
	main()