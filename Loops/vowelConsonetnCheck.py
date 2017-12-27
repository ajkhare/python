# !/usr/bin/python
# Assignment : Print vowels and consonents from given string


def isVowel(x):
	if (x in list("aeiouAEIOU")):
		return True
	else:
		return False

def isConsonent(x):
	if (x in list("bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ")):
		return True
	else:
		return False
		
def main():
	user_str = input("Enter a string : ")
	vowelCnt = 0
	consonentCnt = 0
	
	for x in user_str:
		if(isVowel(x)):
			vowelCnt += 1
			print ("{} character is vowel".format(x))
		elif(isConsonent(x)):
			consonentCnt += 1
			print ("{} character is consonent".format(x))
		else:
			print ("{} character is special character".format(x))

	print("Total Vowels are {}. \nTotal Consonents are {}".format(vowelCnt,consonentCnt))
	
if __name__=='__main__':
	main()