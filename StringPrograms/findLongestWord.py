# !/usr/bin/python
# Assignment : Write a Python function that takes a string containing many words and returns the length of the longest one.

def main():
	main_str = input("Enter a big string : ")
	longestWord = 0
	counter = 0
	for x in main_str:
		if(x != ' ' ):
			counter += 1
		elif(counter >= longestWord):
			longestWord = counter
			counter = 0
	
	# Exclusive logic for last word in the string
	if(counter >= longestWord):
		longestWord = counter

	print("Length of longest word is {}".format(longestWord))

if __name__=='__main__':
	main()