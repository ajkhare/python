# !/usr/bin/python
# Assignment : Write a Python program to count the number of characters (character frequency) in a string.
# Ex:	Input: aabbbbbcccddaaaaa
#		Output: a2b4c3d2a5

def main():
	
	print ("INCOMPLETE PROGRAM")
	
	main_str = input("Enter string value : ")
	y = main_str[0]
	count = 1
		
	for x in range(1,len(main_str)):
		if(main_str[x] == main_str[x-1]):
			count+=1
		else:
			result_str = main_str[x]+str(count)
			count=0
			
	print(result_str)

if __name__=='__main__':
	main()
