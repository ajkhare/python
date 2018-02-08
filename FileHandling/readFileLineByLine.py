# !/usr/bin/python
# Assignment : Read file line by line and convert it in dictionary

import copy

def readFile(fd,MasterConfigDict):
	line=fd.readline()
	while(line != ''):
		appendDict(line,MasterConfigDict)
		line=fd.readline()

		
def appendDictofDict(fd):
	MasterConfigDict={}
	line=fd.readline()
	while (line != ''):
		if (line.startswith('[')):
			sectionType = line.split('[')[1].split(']')[0]
			MasterConfigDict[sectionType]=''
			#print(line)
			#print(sectionType)
			miniDict,line = appendDict(fd)
			MasterConfigDict[sectionType]=copy.deepcopy(miniDict)
			
		else:
			line=fd.readline()

	print(MasterConfigDict)
	return MasterConfigDict
	
	
def appendDict(fd):
	configDict = {}
	line=fd.readline()
	while (line != '' and not line.startswith('[')):
		if (not line.startswith('#') and '=' in line):
			l1=line.split('=')
			value=l1[1]
			if ('#' in l1[1]):
				value= l1[1].split('#')[0]
			configDict[l1[0]]=value.strip()
		line=fd.readline()
		#print("Inside appendDict while")
		
	return configDict,line
	

	
'''	
def appendDict(fd):
	configDict = {}
	MasterConfigDict = {}
	line=fd.readline()
	while (line != ''):
		if (not line.startswith('#') and '=' in line):
			l1=line.split('=')
			value=l1[1]
			if ('#' in l1[1]):
				value= l1[1].split('#')[0]
			configDict[l1[0]]=value.strip()
			
		line=fd.readline()

	print(configDict)
'''
	
def openFile(fileName):
	fd=open(fileName)
	return fd

def main():
	fileName = input("Enter File Name : ")
	fd=openFile(fileName)
	
	#appendDictofDict(fd)
	MasterConfigDict = appendDictofDict(fd)
	print(MasterConfigDict)

if __name__=='__main__':
	main()