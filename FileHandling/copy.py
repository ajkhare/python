# !/usr/bin/python
# Assignment : copy.py <source> <destination>

import sys

def copy(source,destination):
	fd_source = open(source,"r")
	fd_dest = open(destination,"w+")
	
	line = fd_source.readline()
	while(line!=""):
		fd_dest.write(line)
		line = fd_source.readline()
		
	fd_dest.close()
	fd_source.close()

def main():
	print(sys.argv)
	print(sys.argv[1])
	print(type(sys.argv))
	if((sys.argv[1]!="") and (sys.argv[2]!="")):
		copy(sys.argv[1],sys.argv[2])
	else:
		print("Help --> copy.py <source> <destination>")
	

if __name__ =='__main__':
	main()