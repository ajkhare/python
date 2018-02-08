# !/usr/bin/python
# Assignment : Display file content in reverse order without any loop

def readLastChar(fd,cnt):
	while(fd.tell()!=0):
		print(fd.read1(1).decode('ascii'),end="")
		fd.seek(cnt-1,2)
		return readLastChar(fd,cnt-1)

def main():
	fileName = input("Enter File Name : ")
	fd = open(fileName,"rb")
	fd.seek(0,2)
	readLastChar(fd,0)


if __name__=='__main__':
	main()