# !/usr/bin/python
# Assignment : RTP Packet assignment

def createPacket(version,padding,extension,cc,marker,pt,seq_number,timestamp,SSRC_identifier,CSRC_identifier,header_extension):
	packet=version
	packet=packet<<1
	packet=packet|padding
	packet=packet<<1
	packet=packet|extension
	packet=packet<<4
	packet=packet|cc
	packet=packet<<1
	packet=packet|marker
	packet=packet<<6
	packet=packet|pt
	packet=packet<<16
	packet=packet|seq_number
	packet=packet<<32
	packet=packet|timestamp
	packet=packet<<32
	packet=packet|SSRC_identifier
	packet=packet<<32
	packet=packet|CSRC_identifier
	packet=packet<<64
	packet=packet|header_extension
	
	return packet

	
def depacket(packet):
	header_extension = packet & ((1<<64)-1)
	packet = packet >> 64
	CSRC_identifier = packet & ((1<<32)-1)
	packet = packet >> 32
	SSRC_identifier = packet & ((1<<32)-1)
	packet = packet >> 32
	timestamp = packet & ((1<<32)-1)
	packet = packet >> 32
	seq_number = packet & ((1<<16)-1)
	packet = packet >> 16
	pt = packet & ((1<<6)-1)
	packet = packet >> 6
	marker = packet & ((1<<1)-1)
	packet = packet >> 1
	cc= packet & ((1<<4)-1)
	packet = packet >> 4
	extension = packet & ((1<<1)-1)
	packet = packet >> 1
	padding = packet & ((1<<1)-1)
	packet = packet >> 1
	version = packet
	
	print(version,padding,extension,cc,marker,pt,seq_number,timestamp,SSRC_identifier,CSRC_identifier,header_extension)
	

def main():
	print("****** RTP packet Program ******")
	version = eval(input("Enter version (Values can be from 0-3) : "))				# version is 2 bits
	padding = eval(input("Enter padding (Values can be from 0-1) : "))				# padding is 1 bit
	extension = eval(input("Enter extension (Values can be from 0-1) : "))			# extension is 1 bit
	cc = eval(input("Enter CSRC count (Values can be from 0-15) : "))				# cc is 4 bits
	marker = eval(input("Enter marker (Values can be from 0-1) : "))				# marker is 1 bit
	pt = eval(input("Enter payload type (Values can be from 0-127) : "))			# pt is 6 bits
	seq_number = eval(input("Enter seq. number (Values can be from 0-65535) : "))	# seq number is 16 bits
	timestamp = eval(input("Enter timestamp (Values can be from 0-4294967295) : "))	# timestamp is 32 bits
	SSRC_identifier = eval(input("Enter SSRC_identifier (Values can be from 0-4294967295) : "))		# SSRC_identifier is 32 bits
	CSRC_identifier = eval(input("Enter CSRC_identifier (Values can be from 0-4294967295) : "))		# CSRC_identifier is 32 bits
	header_extension = eval(input("Enter Extension header (Values can be from 0-18446744073709551615) : "))	# Extension Header is 64 bits
	
	
	packet = createPacket(version,padding,extension,cc,marker,pt,seq_number,timestamp,SSRC_identifier,CSRC_identifier,header_extension)
	print("Packet is {}".format(packet))
	
	depacket(packet)
	
if (__name__ == '__main__'):
	main()