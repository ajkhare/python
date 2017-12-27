# !/usr/bin/python
# Assignment : Accept 2 strings and Swap first two characters from each
#				e.g. "India" "Great" => "Grdia" "Ineat"

def main():
	main_str1 = input("Enter String : ")
	main_str2 = input("Enter String : ")
	
	ans_str1 = main_str2[0:2]+main_str1[2:len(main_str1)]
	ans_str2 = main_str1[0:2]+main_str2[2:len(main_str2)]

	print(ans_str1,ans_str2)
	
if __name__=='__main__':
	main()