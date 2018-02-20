# !/usr/bin/python
# Assignment : copy.py <source> <destination> [<number of lines>] using Config Parser

import sys
import argparse


def copy(source,destination,n):
	fd_source = open(source,"r")
	fd_dest = open(destination,"a")
	#print(fd_dest.tell())
	
	if(n==0):
		print("Inside if")
		line = fd_source.readline()
		while(line!=""):
			fd_dest.write(line)
			line = fd_source.readline()
	else:
		line = fd_source.readline()
		count=1
		while(line!="" and count <= n):
			print(count)
			fd_dest.write(line)
			line = fd_source.readline()
			count += 1
			
	fd_dest.close()
	fd_source.close()

	
def main():
	print(sys.argv)
	#print(sys.argv[1])
	print(type(sys.argv))

	parser=argparse.ArgumentParser()
	
	parser.add_argument("-s",type=str,help="Source file")
	parser.add_argument("-d",type=str,help="Destination file")
	parser.add_argument("-n",type=str,help="Number of lines, default is 0 i.e. copy entire file",default=0)
	
	args = parser.parse_args()
	
	if(len(sys.argv) >= 3):
		copy(args.s,args.d,int(args.n))
	else:
		print("Help --> copy.py <source> <destination> [<Number of lines>]")
	

if __name__ =='__main__':
	main()