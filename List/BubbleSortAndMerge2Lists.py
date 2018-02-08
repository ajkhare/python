# !/usr/bin/python
# Assignment : Accept 2 lists from user and sort the 2 lists from user.(without using builtin function)
#				Merge the given 2 lists

def SelectionSort(l1):
	for x in range(len(l1)):					# x = 0,1,2,3,4,5
		for y in range(x+1,len(l1)):			# y = x+1 to len(l1)
			if(l1[x]>l1[y]):					# Compare and swap if number is less)
				temp=l1[y]
				l1[y]=l1[x]
				l1[x]=temp

	
def MergeLists(l1,l2):
	l3=[]
	i=0
	j=0
	
	while((i<len(l1)) & (j<len(l2))):
		if (l1[i] < l2[j]):
			l3.append(l1[i])
			i+=1
		else:
			l3.append(l2[j])
			j+=1
	
	if i < len(l1):
		l3.extend(l1[i:])
	if j < len(l2):
		l3.extend(l2[j:])

	print("Merged List = {}".format(l3))


def main():
	# Accept 2 lists from user
	l1 = list(eval(input("Enter List : ")))
	l2 = list(eval(input("Enter List : ")))
	print("Original Lists l1 = {}".format(l1))
	print("Original Lists l2 = {}".format(l2))
	
	# Sort 2 lists
	SelectionSort(l1)
	SelectionSort(l2)
	
	# Print sorted lists
	print("Sorted Lists l1 = {}".format(l1))
	print("Sorted Lists l2 = {}".format(l2))
	
	MergeLists(l1,l2)
	
if __name__=='__main__':
	main()