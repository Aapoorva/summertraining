#!/usr/bin/env python3
import  socket 
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

while True:
	msg=input("Enter message : ").encode()
	s.sendto(msg,('127.0.0.1',9999))