#!/usr/bin/python
# Assignment : Check if string is right rotaion of given string
# Exmaple : String = India,  RightRotationString = aIndi / iaInd / diaIn / ndiaI / India ... etc ...

def main():
	mainStr = input("Enter String : ")
	rrCheckStr = input("Enter String to be checked : ")
	
	if(len(mainStr) == len(rrCheckStr)):
		masterStr = mainStr+mainStr
		if (rrCheckStr in masterStr):		#Equvalent to String's function __contains__()
			print("String is right rotation")
		else:
			print("String is not right rotation")
	else:
		print("String is not right rotation")


if __name__=='__main__':
	main()