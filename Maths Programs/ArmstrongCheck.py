# !/usr/bin/python
# Assignment : Check armstrong number


def main():
	no = eval(input("Enter Number : "))
	arm_sum = 0
	org_no = no
	
	while(no!=0):
		digit = no % 10
		no = no // 10
		arm_sum = arm_sum + (digit*digit*digit)
	
	if(org_no == arm_sum):
		print("Given Number is Armstrong Number")
	else:
		print("Given Number is not Armstrong Number")
		
if __name__=='__main__':
	main()