# !/usr/bin/python
# Assignment : File parsing assignment

def menu():
	print("1) Enter search String\
			\n2) Exit")
	choice = eval(input("Enter choice : "))
	return choice
	

def countLines(fd,subStr):
	line=fd.readline()
	cnt=0
	
	if(subStr[0] == '^'):
		print("Inside ^")
		while(line!=''):
			line=fd.readline()
			if(line.startswith(subStr[1:])):
				cnt+=1
			
	elif(subStr.endswith('$')):
		print("Inside $")
		while(line!=''):
			line=fd.readline()
			if(line.endswith(subStr[:len(subStr)-1]+"\n")):
				cnt+=1
	
	else:
		print("Inside else")
		while(line!=''):
			#print(line)
			line=fd.readline()
			if(line.__contains__(subStr)):
				cnt+=1
	
	fd.seek(0)
	print(cnt)
	
	return cnt
	
def main():
	fileName = input("Enter file name : ")
	fd=open(fileName)
	
	choice = menu()
	while(choice!=2):
		if (choice==1):
			subStr = input("Enter search string : ")
			if(subStr[0] == '^'):
				print("Lines starts with {} are {}".format(subStr,countLines(fd,subStr)))
			elif(subStr.endswith == '$'):
				print("Lines ends with {} are {}".format(subStr,countLines(fd,subStr)))
			else:
				print("Lines containing sub String {} are {}".format(subStr,countLines(fd,subStr)))
		
		choice=menu()
	

if __name__=='__main__':
	main()