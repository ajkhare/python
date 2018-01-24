# !/usr/bin/python
# Assignment : Create Packet & depacket

def createPacket(crc,length,data,flag,protoType):
	packet=crc
	packet=packet<<3
	packet=packet|length
	packet=packet<<7
	packet=packet|data
	packet=packet<<16
	packet=packet|data
	packet=packet<<2
	packet=packet|flag
	packet=packet<<4
	packet=packet|protoType
	
	print(bin(packet))
	return packet

def createDepacket(packet):
	protoType=packet & ((1<<4)-1)
	packet=packet>>4
	flag=packet & ((1<<2)-1)
	packet=packet>>2
	data=packet & ((1<<16)-1)
	packet=packet>>16
	length=packet & ((1<<7)-1)
	packet=packet>>7
	crc = packet & ((1<<3)-1)
	
	print(crc,length,data,flag,protoType)

	
def main():
	crc = eval(input("Enter CRC : "))
	length = eval(input("Enter Lenght : "))
	data = eval(input("Enter Data : "))
	flag = eval(input("Enter Flag : "))
	protoType = eval(input("Enter Protocol Type : "))

	packet = createPacket(crc,length,data,flag,protoType)
	print("Packet is {}".format(packet))
	
	createDepacket(packet)
	
if __name__=='__main__':
	main()