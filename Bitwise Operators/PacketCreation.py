# !/usr/bin/python
# Assignment : Create Packet & depacket

def createPacket(crc,length,data,flag):
	packet = 0
	# Assign crc value to packet
	packet = crc
	
	packet = packet << 8
	
	# Create 8 least signigicant bits to 0
	packet = packet & ((1<<8)-1)
	# insert length into packet
	packet = packet & length
	
	# Create 18 least significant bits to 1
	packet = packet << 18
	
	

def createPacketCorrect(crc,length,data,flag):
	packet = crc
	
	packet = packet << 8
	packet = packet | length & ((1<<8)-1)
	packet = packet << 18
	packet = packet | data & ((1<<18)-1)
	packet = packet << 1
	packet = packet | flag & ((1<<1)-1)
	
	return packet

	
# Why create & operation above ?
# Why & operation is required here --> packet = packet | length & ((1<<8)-1)

def mycreatePacketCorrect(crc,length,data,flag):
	packet = crc
	
	packet = packet << 8
	packet = packet | length
	packet = packet << 18
	packet = packet | data 
	packet = packet << 1
	packet = packet | flag
	return packet

def depaketizeCorrect(packet):
	flag = packet & ((1<<1)-1)
	packet = packet >> 1
	data = packet & ((1<<18)-1)
	packet = packet >> 18
	length = packet & ((1<<8)-1)
	packet = packet >> 8 
	crc = packet & ((1<<5)-1)
	print(crc,length,data,flag)

# Why to do & to get CRC
def mydepaketizeCorrect(packet):
	flag=packet&((1<<1)-1)
	packet = packet >> 1
	data = packet & ((1<<18)-1)
	packet = packet >> 18
	length = packet & ((1<<8)-1)
	packet = packet >> 8
	crc = packet
	print(crc,length,data,flag)
	

	
def main():
	crc = eval(input("Enter CRC Value : "))				#5 bits
	length = eval(input("Enter length Value : "))		#8 bits
	data = eval(input("Enter data Value : "))			#18 bits
	flag = eval(input("Enter flag Value : "))			#1 bit

	#createPacket(crc,length,data,flag)
	packet = createPacketCorrect(crc,length,data,flag)
	print(packet)
	depaketizeCorrect(packet)
	
	packet1 = mycreatePacketCorrect(crc,length,data,flag)
	print(packet1)
	mydepaketizeCorrect(packet1)
	
if __name__=='__main__':
	main()