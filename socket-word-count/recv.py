#!/usr/bin/env python3
import socket
import numpy as np
import matplotlib.pyplot as plt

#functions
# to count word
def count_words(input_list):
	"To count words and create unique list of elements"
	unique_list=[]
	for i in input_list :
		elmnt=[i,[input_list.count(i)]]
		if elmnt[1][0]>1:
			elmnt_index=input_list.index(i)
			for x in range(elmnt_index, elmnt_index+elmnt[1][0]-1):
				del input_list[elmnt_index]
		unique_list.append(elmnt)
	return unique_list

'''
# to merge lists
def concat_list(pre_uniq_list,uniq_list):
	"To merge previous and new list of inputs"
	#when input for first time or after refresh
	if len(pre_uniq_list)==0:
		return uniq_list
	#assuming and assigning each word occurence next time is 0
	for y in pre_uniq_list:
		y[1].append(0)
	#merging
	for x in uniq_list:
		w_found=0
		for y in pre_uniq_list:
			if x[0]==y[0]:
				w_found=1
				y[1][-1]=x[1][0]
				break
		if w_found==0:
			x[1].insert(0,0)
			pre_uniq_list.append(x)
	return pre_uniq_list
'''
#initialising graph
#making graph interactive
plt.ion()
#creating instance of fig
fig=plt.figure()

ax=fig.add_subplot(111)
#bar instance
bar=ax.bar(['a'],[10])

# plot graph
def plot_graph(uniq_list) :
	x_list=[]
	y_list=[]
	
	#plot graph
	for x in uniq_list :
		bar.set_xdata(x[0])
		bar.set_ydata(x[1][0])
		fig.canvas.draw()
	print(x_list)
	print(y_list)
	# plt.show()

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
# pre_uniq_list=[]
count=0
while True :
	#counting words after interval of 6 message
	if  count!=0 and count%5 == 0:
		input_list.sort()
		#words counted here
		uniq_list = count_words(input_list)
		#previous list combined with new data
		# pre_uniq_list = concat_list(pre_uniq_list,uniq_list)
		# print(pre_uniq_list)
		# plot_graph(pre_uniq_list)
		# pre_uniq_list.clear()

		print("Showing Graph")
		print(uniq_list)
		plot_graph(uniq_list)
		input_list.clear()	#to store next set of input

	count+=1
	#receive data
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