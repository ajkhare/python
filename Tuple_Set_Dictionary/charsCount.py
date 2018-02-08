# !/usr/bin/python
# Assignment : counts Characters in the given string

def generateCharsCount(inputStr):
	inputStrList = list(inputStr)
	internalCnt=0
	cnt=0
	
	while(cnt<len(inputStr)):
		resultStr=inputStr[cnt]
		internalCnt = 1
		while(inputStr[cnt]==inputStr[cnt+1]):
			internalCnt +=1
			cnt+=1
		print(resultStr)
		print(internalCnt)
		resultStr = resultStr+str(internalCnt)
		cnt=cnt+internalCnt
	
	print(resultStr)
	
def generateDictStringCount(inputStr):
	i=0
	resultStr=""
	resultDict={}
	
	while (i<len(inputStr)):
		charToCheck=inputStr[i]
		count=1
		while(i+1 < len(inputStr) and inputStr[i+1]==charToCheck):
			count+=1
			i+=1
			
		if (charToCheck in resultDict.keys()):
			resultDict[charToCheck] = int(resultDict[charToCheck]) + count
		else:
			resultDict[charToCheck] = count
		
		i+=1
	
	return resultDict
	
	
def generateDictStringCountOptimazedWay(inputStr):
	i=0
	resultDict={}
	while (i<len(inputStr)):
		if (inputStr[i] in resultDict):
			resultDict[inputStr[i]] = resultDict[inputStr[i]] + 1
		else:
			resultDict[inputStr[i]] = 1
		i+=1
		
	return resultDict

	
# Home Work
'''	
def generateDictOfDictStringCount(inputStr):
	i=0
	resultStr=""
	resultDict={}
	innerDict={}
	
	while (i<len(inputStr)):
		charToCheck=inputStr[i]
		count=1
		while(i+1 < len(inputStr) and inputStr[i+1]==charToCheck):
			count+=1
			i+=1
		
		if (charToCheck in resultDict.keys()):
			
			resultDict[charToCheck] = int(resultDict[charToCheck]) + count
		else:
			resultDict[charToCheck] = count
		
		i+=1
	
	return resultDict
'''	

def generateStringCount(inputStr):
	i=0
	resultStr=""
	
	while (i<len(inputStr)):
		charToCheck=inputStr[i]
		count=1
		while(i+1 < len(inputStr) and inputStr[i+1]==charToCheck):
			count+=1
			i+=1
		
		resultStr += charToCheck+str(count)
		i+=1
	
	return resultStr
	


def main():
	inputStr="aabbcccddabbb"
	#print(generateCharsCount(inputStr))
	print(generateStringCount(inputStr))
	print(generateDictStringCount(inputStr))
	print(generateDictStringCountOptimazedWay(inputStr))
	
if __name__=='__main__':
	main()