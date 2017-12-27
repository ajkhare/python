# !/usr/bin/python
# Assignment : Count the occurance of substring in given string

def main():
	main_str = input("Enter the string : ")
	sub_str = input("Enter sub string : ")
	cnt = 0
	occurance = 0
	
	while (cnt != len(main_str)):
		if (main_str[cnt] == sub_str[0]):		# Run inner loop to compare
			#print ("Inside if")
			
			inner_cnt = 0
			for y in sub_str:
				#print ("Inside for")
				if (y != main_str[cnt+inner_cnt]):
					break
				else:
					inner_cnt += 1
					
			if (inner_cnt == len(sub_str)):
				#print ("Inside inner if")
				occurance += 1
		#print("cnt = {}, len = {}".format(cnt,len(main_str)))
		cnt += 1
		
	print("There are {} occurances of sub string".format(occurance))
	
if __name__=='__main__':
	main()

	