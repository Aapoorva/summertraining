#!/usr/bin/python3
import socket

recv_ip="127.0.0.1"
recv_port=9999
#creating socket
#		            for ipV4	for UDP
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#now connecting ip and port
print("****TO EXIT CHAT SEND MSG - BYE****")

msg=""
#to be able to send continously
while True:
	if msg.lower().strip() == "bye" :
		break

	msg=input("Enter Message : ")
	#msg in python3 sendto accepts unicode msg(i.e. in bytes)
	s.sendto(msg.encode(),(recv_ip,recv_port))

	#recieving reply message
	reply_pckt=s.recvfrom(1000)
	#Decode reply from unicode to string
	reply_decoded=reply_pckt[0].decode()
	print("Reply Message : ",reply_decoded)