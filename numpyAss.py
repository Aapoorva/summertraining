#!/usr/bin/python3
import numpy as np
import math

#functions
def isPrime(num):
	"to check no is prime or not"
	i=2
	while i < int(math.sqrt(num)) :
		if num%i==0:
			return False
		i+=1
	return True

print("Enter elements (TO END INPUT ENTER - STOP) : ")
elmnt=[]
#fetching data to be processed
elmnt.append(input())
for i in elmnt:
	if i.lower()!='stop':
		elmnt.append(input())

#removing last element ie stop from elmnt
elmnt.remove(elmnt[-1])

#checking no. of elements entered are valid or not
elmnt_len=len(elmnt)
print("You have entered ",elmnt_len," elements")
if elmnt_len < 4 :
	print("You need "+str(4-elmnt_len)+" more element to create matrix : ")
	for x in range(elmnt_len,4):
		elmnt.append(input())
if elmnt_len > 4 and isPrime(elmnt_len) :
	elmnt.append(input("You need 1 more element to create matrix : "))

#displaying possible matrix order choice
print("Select matrix order")
ordr_list=[]
elmnt_len=len(elmnt)
for x in range(2,int(math.sqrt(elmnt_len))+1):
	if elmnt_len%x==0 :
		ordr_list.append((x,elmnt_len//x))
		print(ordr_list[-1]," : ",len(ordr_list))
		if(x!=elmnt_len//x):
			ordr_list.append((elmnt_len//x,x))
			print(ordr_list[-1]," : ",len(ordr_list))

ordr_ch=int(input())
if ordr_ch>0 and ordr_ch<=len(ordr_list):
	row = int(ordr_list[ordr_ch-1][0])
	col = int(ordr_list[ordr_ch-1][1])
	print(np.array(elmnt).reshape(row,col))
else :
	print("INVALID CHOICE")