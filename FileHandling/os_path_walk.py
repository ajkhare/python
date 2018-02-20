# !/usr/bin/python
# Assignment : Implement os.walk methods

import os
import sys
import os.path

py_count = 0
txt_count = 0
other_count = 0

def callback(arg, directory, files):
	print (arg)
	global py_count
	global txt_count
	global other_count
	for file in files:
		if(file.endswith(".py")):
			py_count+=1
		elif(file.endswith(".txt")):
			txt_count+=1
		else:
			other_count+=1

def main():
	global py_count
	global txt_count
	global other_count
	
	for root,dirs,files in os.walk("D:\\temp\\pytemp"):
		print("Files are : {}".format(files))
		print("Dirs are : {}".format(dirs))
		print("Root is : {}".format(root))
		
		for file in files:
			if(file.endswith(".py")):
				py_count+=1
			elif(file.endswith(".txt")):
				txt_count+=1
			else:
				other_count+=1
			
	#os.walk("C:\\Python\\Python37\\Lib", callback, "directory traverse")
	print("Python Files are : {}, Text Files are : {}, Other Files are : {}".format(py_count,txt_count,other_count))
	
	


if __name__=='__main__':
	main()