#!/usr/bin/env python3
import time
import webbrowser as wb

option='''
Press 1 : To Search on Browser
Press 2 : To Get Images
Press 3 : To Get URL
Press 4 : To Get Current Time
Press 5 : To Open default browser
Press 6 : To Scan Network
Press 7 : To Get Domain Owner Details
'''

print(option)

ch=input("Choice = ")

if ch == '1':
	x=input("Enter anything : ")
	#removing extra space from start and end
	x=x.strip()
	#spliting input
	x=x.split()
	for i in x:
		print("------------Opening browser---------------")
		wb.open_new_tab('https://www.google.com/search?q='+i)

elif ch == '2':
	print("Displaying images")
elif ch == '3':
	print(ch)
elif ch == '4':
	
	print(ch)
elif ch == '5':
	
	print(ch)
elif ch == '6':

	print(ch)
elif ch == '7':

	print(ch)
else:
	print("Invalid Choice")
