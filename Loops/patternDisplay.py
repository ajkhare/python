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

import sys

def main():
	option = 0
	while(option != 4):
		print("Enter Option\n1 : Triangle pattern\n2 : Reverse Triangle\n3 : Letters Triangle\n4 : Exit")
		option = eval(input("Enter option : "))
		if(option == 4):
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

if __name__=='__main__':
	main()