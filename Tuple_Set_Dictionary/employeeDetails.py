# !/usr/bin/python
# Assignment : Employee List example using data structure of dictonary
# e.g. {1:{"name":"Ajinkya","DOB":"12/08/1987","address":"Nigdi","salary":20000}
#		...}
import copy

def menu():
	print("1) Insert \
			\n2) Update \
			\n3) Display \
			\n4) Search \
			\n5) Remove \
			\n6) Exit")
	choice = eval(input("Enter Choice : "))
	return choice
	
def getNextUnique_EmpID(emp_list):
	# Check is dictionary is empty
	# bool(dict) evaluates to false if dictionary is empty
	# If dictionary is empty then return next_EmpID = 1
	if(not bool(emp_list)):
		return 1
	
	#print(emp_list)
	# Otherwise generate next number and return
	keyList = list(emp_list.keys())
	keyList.sort()
	next_EmpID = keyList[len(keyList)-1]+1
	#print(emp_list)
	return next_EmpID
	
def main():
	emp_list={}
	each_emp_details={}
	choice=menu()
	while(choice!=6):
		if(choice==1):		# Accept Employee from user input
			name = input("Enter name of the employee : ")
			dob = input("Enter dob of the employee : ")
			address = input("Enter address of the employee : ")
			salary = eval(input("Enter salary of the employee : "))
			each_emp_details["name"]=copy.deepcopy(name)
			each_emp_details["dob"]=copy.deepcopy(dob)
			each_emp_details["address"]=copy.deepcopy(address)
			each_emp_details["salary"]=copy.deepcopy(salary)
			
			# Fetch next auto generated empID
			empID = getNextUnique_EmpID(emp_list)
			#print(empID)
			emp_list[empID]=copy.deepcopy(each_emp_details)
						
			#emp_list[empID]=each_emp_details
			
		elif(choice==2):		# Update Employee from user input
			print(emp_list)
			empID = eval(input("Enter empID of the employee you want to update : "))
			name = input("Enter name of the employee : ")
			dob = input("Enter dob of the employee : ")
			address = input("Enter address of the employee : ")
			salary = eval(input("Enter salary of the employee : "))
			
			each_emp_details["name"]=copy.deepcopy(name)
			each_emp_details["dob"]=copy.deepcopy(dob)
			each_emp_details["address"]=copy.deepcopy(address)
			each_emp_details["salary"]=copy.deepcopy(salary)
			emp_list[empID]=copy.deepcopy(each_emp_details)
			
		elif(choice==3):
			print(emp_list)
			
		elif(choice==4):		# Search employee
			searchStr = input("Enter empID/Name of the employee you want to search : ")
			
			if(searchStr.isdigit()):		# If found empID then display
				if(emp_list.get(int(searchStr))!=None):
					print("Details are\
					\n{}".format(emp_list.get(int(searchStr))))
			
			# Search for name in dictionary
			for emp_list_key in emp_list:
				if(emp_list[emp_list_key]["name"] ==searchStr):		# Found record
					print("Details are\
					\n{}".format(emp_list[emp_list_key]))
					break
			else:
				print("Details are not found")
				
				
		elif(choice==5):		# Remove Employee
			print(emp_list)
			empID = eval(input("Enter empID of the employee you want to remove : "))
			print("Following entry is removed \
				\n{}".format(emp_list.pop(empID)))
			
		choice=menu()
		

if __name__=='__main__':
	main()
