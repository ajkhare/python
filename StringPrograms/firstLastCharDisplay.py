# !/usr/bin/python
# Assignment : Display first 2 and last 2 characters from each word in the string

def main():
	main_str = input("Enter String : ")
	str_list = main_str.split(" ")
	for x in str_list:
		print ("First 2 chars = {}, Last 2 chars = {}".format(x[0:2],x[-2:len(x)]))

if __name__=='__main__':
	main()