#!/usr/bin/python3
import socket
import _thread
recv_ip="127.0.0.1"
recv_port=9999
#creating socket
#		            for ipV4	for UDP
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#now connecting ip and port
s.bind((recv_ip,recv_port))

#receiving blank msg to get sender ip and port no.
print("Setting Up...")
msg_pckt=s.recvfrom(1000)
print("Now system is ready....")
print("Welcome")

def recv_msg():
	#to be able to receive continously using while
	while True :
	#buffer size ie. max limit data receiver want to receive at 1 time
		msg_pckt=s.recvfrom(1000)
		#Decode msg recieved in Unicode to String
		msg_decoded=msg_pckt[0].decode()
		#printing received msg
		print("\t\t\t",msg_decoded)

def send_msg():
	#to be able to send continously using while
	while True :
		#Reply to received Message
		reply=input()
		#sending reply
		s.sendto(reply.encode(),msg_pckt[1])

#starting threads
_thread.start_new_thread(recv_msg,())
_thread.start_new_thread(send_msg,())

#to keep code alive
while True:
	pass