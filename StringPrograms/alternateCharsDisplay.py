# !/usr/bin/python
# Assignment : Display alternate characters from the string

def main():
	main_str = input("Enter a String : ")
	for x in range(0,len(main_str),2):
		print (main_str[x],end=" ")
		

if __name__=='__main__':
	main()