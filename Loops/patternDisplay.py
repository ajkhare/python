# !/usr/bin/python
# Assignment : Pattern display
# 1) 	*
#		**
#		***
#		****
# 2)	****
#		***
#		**
#		*
# 3)	A
#		AB
#		ABC
#		ABCD
# 4)	  *
#		 ***
#       *****
#      *******
# 5)	A
#	   BAB
#	  CBABC
#	 DCBABCD
# 6)	*******
#		*** ***
#		**   **
#		*     *

import sys

def main():
	option = 0
	while(option != 5):
		print("Enter Option\n1 : Triangle pattern\n2 : Reverse Triangle\n3 : Letters Triangle\n	\
		4 : Perfect Triangle\n5 : Perfect Triagle of Letters\n6 : Toran Pattern\n7 : Exit")
		
		option = eval(input("Enter option : "))
		if(option == 7):
			sys.exit()
		
		rows = eval(input("Enter number of rows : "))

		if(option == 1):
			for x in range(rows):
				for y in range(x+1):
					print("*",end='')
				print("\n",end='')
		
		elif(option == 2):
			for x in range(rows,0,-1):
				for y in range(x):
					print("*",end='')
				print("\n",end='')
		
		elif(option == 3):
			for x in range(rows):
				ch='A'
				for y in range(x+1):
					print("{}".format(ch),end='')
					ch = chr(ord(ch)+1)
				print("\n",end='')
		
		elif(option == 4):
			for x in range(rows):
				#print(x)
				for m in range(rows-x-1,0,-1):
					print(" ",end='')
				for n in range(x+1):
					print("*",end='')
				for p in range(x):
					print("*",end='')
				print("\n",end='')
		
		elif(option == 5):
			ch='A'
			for x in range(rows):
				#print(x)
				for m in range(rows-x-1,0,-1):
					print(" ",end='')
				for n in range(65+x,64,-1):
					ch = chr(n)
					print(ch,end='')
				for p in range(x):
					print(chr(ord('A')+p+1),end='')
				print("\n",end='')
				
		elif(option == 6):
			for x in range(rows,0,-1):
				for y in range(x):
					print("*",end='')
				for m in range(rows-x):
					print(" ",end='')
				
				print("\n",end='')
			
			print("Incomplete Program")
		
		
if __name__=='__main__':
	main()
