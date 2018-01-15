# !/usr/bin/python
# Assignment : Write a Python program to get a string from a given string where all occurrences of its 
# 			first char have been changed to '$', except the first char itself. Go to the editor 
# Sample String : 'restart'
# Expected Result : 'resta$t'

def main():
	main_str = input ("Enter a String : ")
	first_char = main_str[0]
	result_str = main_str[0]
	
	for x in main_str[1:]:
		if (first_char == x):
			result_str += '$'
		else:
			result_str += x
	
	print(result_str)

if __name__=='__main__':
	main()