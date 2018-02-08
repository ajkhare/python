# !/usr/bin/python
# Assignment : Implement Binary Search using List

def SelectionSort(list1):
	for x in range(len(list1)):					# x = 0,1,2,3,4,5
		for y in range(x+1,len(list1)):			# y = x+1 to len(list1)
			if(list1[x]>list1[y]):					# Compare and swap if number is less)
				temp=list1[y]
				list1[y]=list1[x]
				list1[x]=temp

				
def binSearch(list1,no,lb,ub):
	if(lb<=ub):
		mid = (ub+lb)//2
		print(list1[mid])
		if(no == list1[mid]):			# Number found
			return 1
		elif(no < list1[mid]):				# number lies in first half
			return binSearch(list1,no,lb,mid-1)
		elif(no > list1[mid]):			# number lies in second half
			return binSearch(list1,no,mid+1,ub)
	else:
		return -1						# Number not found
		
def main():
	list1 = list(eval(input("Enter Integer elements : ")))
	
	
	# Sort the given list
	SelectionSort(list1)
	print(list1)
	
	while(True):
		print("Enter number to search using binary search or type -1 to exit")
		no= eval(input("Enter Number to be search : "))
		if(no==-1):
			break
		found = binSearch(list1,no,0,len(list1)-1)
		if (found == 1):
			print("Number is found")
		else:
			print("Number is not found")
		
	
if __name__=='__main__':
	main()