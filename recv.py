#!/usr/bin/env python3
import socket

#functions
# to count word
def count_words(input_list):
	"To count words and create unique list of elements"
	unique_list=[]
	for i in input_list :
		elmnt=[i,[input_list.count(i)]]
		if elmnt[1][0]>1:
			elmnt_index=input_list.index(i)
			for x in range(elmnt_index, elmnt_index+elmnt[1][0]):
				del input_list[elmnt_index]
		unique_list.append(elmnt)
	print(unique_list)

#socket connection
rec_ip="127.0.0.1"
rec_port=9999                      
#  creating a socket - s 
#                     ipv4           UDP 
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#  binding ip  and port 
s.bind((rec_ip,rec_port)) 
#  receiving data
input_list=[]
count=0
while True :
	
	#counting words after interval of 6 message
	if count!=0 and count%6 == 0:
		input_list.sort()
		print(input_list,"\n")
		count_words(input_list)
		input_list.clear()
		print("\n\n")

	count+=1

	data=s.recvfrom(1000)

	#convert byte to string
	data_input=data[0].decode()
	#storing data to list
	#space removed and split
	if data_input.find(" ")!=-1 :
		data_input=data_input.strip().split()
		input_list=input_list+data_input
	#no space added as element
	else :
		input_list.append(data_input)