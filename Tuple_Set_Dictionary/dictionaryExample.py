# !/usr/bin/python
# Assignment : Dictionary example
'''
input dict = {1:1,2:2,3:3}
outputDictValues / List = [100,101,102]
default function fromKeys will generate output like this, {1:[100,101,102],2:[100,101,102],3:[100,101,102]}

Implement overrided function which will do 1:1 mapping like,
{1:100,2:102,3:103}

'''

def fromKeys(inputDict,outputDictValues):
	resultDict = {}
	print(type(inputDict))
	if (type(outputDictValues)==list or type(outputDictValues)==tuple):
		keys_list=list(inputDict.keys())
		print(type(keys_list))
		valuesLength = len(outputDictValues)
		print(len(keys_list))
		for i in range(len(keys_list)):
			print(i)
			print(keys_list)
			
			if(i<valuesLength):
				resultDict[keys_list[i]] = outputDictValues[i]
			else:
				resultDict[keys_list[i]] = None
	else:
		resultDict=dict.fromkeys(inputDict,outputDictValues)
	#print (resultDict)
	return resultDict
	

def main():
	inputDict = {1:1,2:2,3:3}
	outputDictValues=[100,101,102]
	#print("HIII")
	#fromKeys(inputDict,outputDictValues)
	print(fromKeys(inputDict,outputDictValues))
	
if __name__=='__main__':
	main()
