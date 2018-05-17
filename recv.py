#!/usr/bin/env python3
import  socket 
rec_ip="127.0.0.1"
rec_port=9999                      
#  creating a socket - s 
#                     ipv4           UDP 
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#  binding ip  and port 
s.bind((rec_ip,rec_port)) 
#  receiving data
input_list=[]
while True :
	data=s.recvfrom(1000)
	data_input=data[0].decode()			#convert byte to string
	#space removed and split
	if data_input.find(" ")!=-1 :
		data_input=data_input.strip().split()
		input_list=input_list+data_input
	else :
		input_list.append(data_input)
	print(input_list)