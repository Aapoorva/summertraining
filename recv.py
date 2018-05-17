#!/usr/bin/env python3
import  socket 
rec_ip="127.0.0.1"
rec_port=9999                      
#  creating a socket - s 
#                     ipv4         for UDP 
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#  binding ip  and port 
s.bind((rec_ip,rec_port)) 
#  receiving data
while True :
	data=s.recvfrom(1000)
	print(data)