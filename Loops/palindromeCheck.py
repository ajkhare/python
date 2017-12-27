# !/usr/bin/python
# Assignment : Check if entered number is Palindrome or not, positional check

def main():
	number = eval(input("enter a number : "))
	str_number=str(number)
	
	low = 0
	high = len(str_number)-1
		
	while(low != high or low < high):
		if(str_number[low] != str_number[high]):
			break
		low+=1
		high-=1
	
	if (low == high or low < high):
		print("Congratulation you got a Palindrome")


if __name__=='__main__':
	main()

