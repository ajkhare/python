#!/usr/bin/python

def main():
	str1 = input("Enter String : ")
	if(str1 == str1[::-1]):
		print("String is palindrome")
	else:
		print("String is not palindrome")

if __name__=='__main__':
	main()