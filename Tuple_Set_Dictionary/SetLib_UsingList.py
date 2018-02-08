# !/usr/bin/python
# Assignment : Set Library Functions implementation using List 

def menu():
	print("1) Accept Sets \
			\n2) Display Union \
			\n3) Display Intersection\
			\n4) Display isDisjoint \
			\n5) Display isSuperSet \
			\n6) Display isSubSet\
			\n7) Display Difference\
			\n8) Display SymatricDifference\
			\n10 Exit)")
	choice = eval(input("Enter Choice : "))
	return choice

def main():
	choice=menu()
	while(choice!=10):
		if(choice==1):
			Set1 = list(eval(input("Enter Set1 : ")))
			Set2 = list(eval(input("Enter Set2 : ")))
			#print(Set1)
			#print(Set2)
		elif(choice==2):			# Union of 2 sets, using List data structure
			if(len(Set1)>len(Set2)):
				unionSet=Set1
				for x in Set2:
					if(not unionSet.__contains__(x)):
						unionSet.append(x)
			else:
				unionSet=Set2
				for x in Set1:
					if(not unionSet.__contains__(x)):
						unionSet.append(x)
			
			print("Union of Set1 and Set2 is : {}".format(unionSet))

			
		elif(choice==3):			# Intersection of 2 sets, using List data structure
			intersectionSet=[]
			if(len(Set1)<len(Set2)):
				for x in Set1:
					if(Set2.__contains__(x)):
						intersectionSet.append(x)
			else:
				for x in Set2:
					if(Set1.__contains__(x)):
						intersectionSet.append(x)
			print("Intersection of Set1 and Set2 is : {}".format(intersectionSet))
			
		
		elif(choice==4):		# Display if sets are disJoint or not
			for x in Set1:
				if(Set2.__contains__(x)):
					print("Set1 and Set2 are not DisJoint Sets")
					break
			else:
				print("Set1 and Set2 are DisJoint Sets")
			
			
		elif(choice==5):		# Display if sets are superSet
			if(len(Set1)>len(Set2)):
				for x in Set2:
					if(not Set1.__contains__(x)):
						print("Set1 is not SuperSet of Set2")
						break
				else:
					print("Set1 is SuperSet of Set2")
			elif(len(Set2)>len(Set1)):
				for x in Set1:
					if(not Set2.__contains__(x)):
						print("Set2 is not SuperSet of Set1")
						break
				else:
					print("Set2 is SuperSet of Set1")

					
		elif(choice==6):			# Display if sets are subSet	
			if(len(Set1)<len(Set2)):
				for x in Set1:
					if(not Set2.__contains__(x)):
						print("Set1 is not SubSet of Set2")
						break
				else:
					print("Set1 is SubSet of Set2")
			elif(len(Set1)>len(Set2)):
				for x in Set2:
					if(not Set1.__contains__(x)):
						print("Set2 is not SubSet of Set1")
						break
				else:
					print("Set2 is SubSet of Set1")
		
		
		elif(choice==7):			# Display Difference from 2 sets
			differenceSet=[]
			print("If you want output as Set1.difference(Set2) then Type \"1\"\
					\nIf you want output as Set2.difference(Set1) then Type \"2\"")
			innerChoice=eval(input("Enter choise : "))
			
			if(innerChoice==1):
				for x in Set1:
					if(not Set2.__contains__(x)):
						differenceSet.append(x)
				print("Output as Set1.difference(Set2) = {}".format(differenceSet))
			elif(innerChoice==2):
				for x in Set2:
					if(not Set1.__contains__(x)):
						differenceSet.append(x)		
				print("Output as Set2.difference(Set1) = {}".format(differenceSet))
		
		
		elif(choice==8):			# Display symmetric difference from both sets
			symmDiffSet=[]
			for x in Set1:
				if(not Set2.__contains__(x)):
					symmDiffSet.append(x)
			for x in Set2:
				if(not Set1.__contains__(x) and not symmDiffSet.__contains__(x)):
					symmDiffSet.append(x)
			print("Symatric Difference of 2 sets = {}".format(symmDiffSet))
			
		choice=menu()








if __name__=='__main__':
	main()