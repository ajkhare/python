# !/usr/bin/python
# Assignment : List comprehension to generate unique numbers from given list

'''
def isUniqueElement(list1,x)
	if(list1.count(x) == 1):
		return x
	else:
		return 
'''
	
def main():
	list1=[4,88,7,5,14,7,81,88,5,67,55]
	#print(list1)
	unique_list=[x for x in list1 if(list1.count(x)==1)]
	print(unique_list)
	
	# List which contains 2 duplicate elements from list
	list2=[1,4,3,1,4,6,8]
	print(list2)
	unique_list2=[x for x in list2 if(list2.count(x)==1) or list2.remove(x)==None] 
	print(list2)
	print(unique_list2)
	
	

if __name__=='__main__':
	main()
	