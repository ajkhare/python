# !/usr/bin/python
# Assignment : Print words and characters count from given sentense

def count(s):
	words = 0
	chars = 0
	for x in s:
		if(x != ' '):
			chars+=1
		else:
			words+=1
	return (chars,words+1)

def main():
	main_str = input("Enter a sentense : ")
	chr,wrd = count(main_str)

	print("Words : {}, Characters : {}".format(wrd,chr))
	
if __name__=='__main__':
	main()