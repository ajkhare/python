# !/usr/bin/python
# Assignment : Accept range and display all numbers which are not multiple of 2 and 3

def main():
	lower = eval(input("Enter lower range : "))
	higher = eval(input("Enter higher range : "))

	while(lower <= higher):
		if (lower % 2 == 0 or lower % 3 == 0):
			lower += 1
			continue
		print("Number is : {}".format(lower))
		lower += 1

if __name__=='__main__':
	main()