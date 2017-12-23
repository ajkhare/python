#!/usr/bin/python
# Assignment : Check if string is right rotaion of given string
# Exmaple : String = India,  RightRotationString = aIndi / iaInd / diaIn / ndiaI / India ... etc ...

# Last char = b[len(b)-1]
# All string sxcept last char = b[:len(b)-1]
# b = "Pune"
# lchar = "e"
# otherStr = "Pun"
# rotatedString = lchar + otherStr (ePun)


def main():
	mainStr = input("Enter String : ")
	rrCheckStr = input("Enter String to be checked : ")
	
	flag = 0
	
	rotatedString = mainStr
	lastChar = rotatedString[len(rotatedString)-1]
	otherStr = rotatedString[:len(rotatedString)-1]
	rotatedString = lastChar+otherStr
	
	if (rotatedString == rrCheckStr):
			flag = 1
		
	while (rotatedString != mainStr and flag == 0):
		lastChar = rotatedString[len(rotatedString)-1]
		otherStr = rotatedString[:len(rotatedString)-1]
		rotatedString = lastChar+otherStr
		if (rotatedString == rrCheckStr):
			flag = 1
			break
	
	if(flag == 1):
		print("String is right rotating")
	else:
		print("String is not right rotaing")

		
if __name__=='__main__':
	main()
