# !/usr/bin/python
# Assignment : File parsing assignment to find longest and smallest line

def main():
	fileName = input("Enter File Name : ")
	fd = open(fileName)
	
	max = 0
	min = 10000
	maxline=""
	minline=""
	line=fd.readline()
	
	while(line!=''):
		if(max<len(line)):
			max=len(line)
			maxline = line
		if(min>len(line)):
			if(line == "\n"):
				line=fd.readline()
				continue
			min=len(line)
			minline = line
		
		line=fd.readline()
		
	print("Line with Max length is ---> {}".format(maxline))
	print("Line with Max length is ---> {}".format(minline))


if __name__=='__main__':
	main()