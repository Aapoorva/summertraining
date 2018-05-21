#!/usr/bin/python3

import socket
recv_ip="127.0.0.1"
recv_port=9999
#creating socket
#		            for ipV4	for UDP
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#now connecting ip and port
s.bind((recv_ip,recv_port))

msg_decoded=""
#to be able to send continously
while True :
	if msg_decoded.lower().strip() == "bye" :
		break
#buffer size ie. max limit data receiver want to receive at 1 time
	msg_pckt=s.recvfrom(1000)
	#Decode msg recieved in Unicode to String
	msg_decoded=msg_pckt[0].decode()
	print("Message Recieved : ",msg_decoded)