#!/usr/bin/env python3
#to download web page from url
import requests
#to parse html of web page
from bs4 import BeautifulSoup

#url where to fetch data
url="https://google.com/search?q=hello"
#create instance of page
page=requests.get(url)

#to parse html page is stored in BeautifulSoup format
soup=BeautifulSoup(page.content,'html5lib')

#to print html in nested structure
# print(soup.prettify())

#to fetch a tag
# print(soup.title.string) #to fetch and print title

#to fetch all url in page
#to find <a> tag which contain href
all_links=soup.find_all("a")
for link in all_links :
	#print link which is present in href attribute
	link_href=link.get("href")
	if "url?q=" in link_href and not "webcache" in link_href :
		#to replace url codes like ? as %3F and = as %3D as =
        if "%3F" in link_href:
            link_href=link_href.replace("%3F","?")
        if "%3D" in link_href:
            link_href=link_href.replace("%3D","=")
		#removing /url?q= from the link
		link_url=link_href.split('url?q=')[1]
		#filtering usefull part of url
		link_final=link_url.split('&sa=U')[0]
		print(link_final)