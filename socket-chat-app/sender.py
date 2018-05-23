#!/usr/bin/python3
import socket
import _thread
recv_ip="127.0.0.1"
recv_port=9999
#creating socket
#		            for ipV4	for UDP
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#sending blank msg to tell reciver sender ip
s.sendto("".encode(),(recv_ip,recv_port))
print("Welcome")

def send_msg() :
	#to be able to send continously
	while True:
		msg=input()
		#msg in python3 sendto accepts unicode msg(i.e. in bytes)
		s.sendto(msg.encode(),(recv_ip,recv_port))

def recv_msg() :
	"to receive msg continously"
	while True:
		#recieving reply message
		reply_pckt=s.recvfrom(1000)
		#Decode reply from unicode to string
		reply_decoded=reply_pckt[0].decode()
		#sending reply message
		print("\t\t\t",reply_decoded)

#starting threads
_thread.start_new_thread(send_msg,())
_thread.start_new_thread(recv_msg,())

#to keep program alive
while True:
	pass