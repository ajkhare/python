# !/usr/bin/python
# Assignment : File parsing for displaying alternate 20 charcters

def main():
	fd = open("D:\\temp\\audio.conf","rb")
	next20chars = fd.read(20)
	skipped20chars = ""
	while(next20chars != b''):
		print(str(next20chars))
		fd.seek(20,1)
		next20chars = fd.read(20)
	
	print("\n============================================\n")
	
	fd.seek(0)
	while(skipped20chars != b''):
		fd.seek(20,1)
		skipped20chars=fd.read(20)
		print(str(skipped20chars))
	
	
if __name__=='__main__':
	main()