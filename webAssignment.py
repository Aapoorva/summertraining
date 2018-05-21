#!/usr/bin/env python3
import time
import webbrowser as wb
#to load web page content from url
import requests
#to parse html of web page
from bs4 import BeautifulSoup

#functions
#to read input and split in list
def readData(msg):
	data=input(msg)
	#removing extra space from start and end
	data=data.strip()
	#spliting input
	data=data.split()
	return data

#to fetch and display urls from google search result
def fetch_display_urls(data):
	#url where to fetch data
	url="https://google.com/search?q="+data
	#create instance of page
	page=requests.get(url)

	#to parse html page is stored in BeautifulSoup format
	soup=BeautifulSoup(page.content,'html5lib')

	#to fetch all url in page
	#to find <a> tag which contain href
	all_links=soup.find_all("a")
	print("Search Results : S")
	for link in all_links :
		#print link which is present in href attribute
		link_href=link.get("href")
		if "url?q=" in link_href and not "webcache" in link_href :
			#to replace url codes like ? as %3F and = as %3D as =
			if "%3F" in link_href :
				link_href=link_href.replace("%3F","?")
			if "%3D" in link_href:
				link_href=link_href.replace("%3D","=")
			#removing /url?q= from the link
			link_url=link_href.split('url?q=')[1]
			#filtering usefull part of url
			link_final=link_url.split('&sa=U')[0]
			print(link_final)
	

option='''
Press 1 : To Search on Browser
Press 2 : To Get Images Search Result
Press 3 : To Search URLs for search
Press 4 : To Get Current Time
Press 5 : To Open Default browser
Press 6 : To Scan Network
Press 7 : To Get Domain Owner Details
'''
print(option)

ch=input("Choice = ")

#To Search on Browser
if ch == '1':
	data=readData("Enter words to search : ")
	print("------------Opening browser---------------")
	for i in data:
		wb.open_new_tab('https://www.google.com/search?q='+i)

#To Get Images Search Result
elif ch == '2':
	data=readData("Enter words to search images : ")
	print("------------Displaying images-------------")
	for x in data:
		wb.open_new_tab('https://www.google.com/search?tbm=isch&q='+x)

#To Search URLs for search
elif ch == '3':
	data=input("Search : ")
	print("Please be patient.Searching....")
	fetch_display_urls(data)
	
#To Get Current Time
elif ch == '4':
	print(time.ctime())

#To Open Default browser
elif ch == '5':
	print(ch)

elif ch == '6':

	print(ch)
elif ch == '7':

	print(ch)
else:
	print("Invalid Choice")
