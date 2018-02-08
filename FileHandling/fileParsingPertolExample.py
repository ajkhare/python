# !/usr/bin/python
# Assignment : File parsing for petrol example

def menu():
	print("1) Enter state (MH/Goa/KA) for which average price you want\
			\n2) Enter 2 to Exit")
	choice = input("Enter choice : ")
	return choice

def getAverage(fd,choice):
	fd.seek(0)
	line = fd.readline()
	total = 0
	lineCnt = 1

	while(line != ''):
		if(choice=='MH'):		# Get average for MH
			#print(line.split(" ")[2])
			total = total + int(line.split(" ")[2])
		elif(choice=='Goa'):	# Get average for Goa
			#print(line.split(" ")[3])
			total = total + int(line.split(" ")[3])
		elif(choice=='KA'):	# Get average for KA
			#print(line.split(" ")[4])
			total = total + int(line.split(" ")[4])
		line=fd.readline()
		lineCnt+=1
		
	return (total/(lineCnt-1))	
	
	
def main():
	fd = open("D:\\python\\JB\\FileHandling\\petrol_avg_out.txt")
	choice = menu()
	
	while(choice!="2"):
		print("Average price of petrol for state {} is {}".format(choice,getAverage(fd,choice)))
		choice=menu()

if __name__=='__main__':
	main()