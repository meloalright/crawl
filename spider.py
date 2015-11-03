#melo-python-spider
import requests
import urllib
import os
from bs4 import BeautifulSoup

url = raw_input("THE URL YOU WANNNA TO CRAW: ")

shortname = raw_input("THE SHORTNAME OF IT: ")
#url = 'http://NBA.hupu.com'
header = {'User-Agent':'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_2_1 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5'}
source_code = requests.get(url,headers = header)#get html
plain_text = source_code.text
#print(plain_text)
#beautiful for maching the code as beautiful HTML code
Soup = BeautifulSoup(plain_text)

download_links =[]
#folder_path = '/Desktop/PYTHON/spider-code/SPIDER-in-PYTHON/jiandan'
#print(download_links)
#for item in download_links:
	#filename =urllib.urlretrieve(item)
	#print(filename)
	#,folder_path + item[-10:]
os.mkdir(shortname)
fo = open(shortname+"/spider.html","wb")

#fo.write("<DOCTYPE html>")
#fo.write("<html>")
#fo.write("<head></head>")
#fo.write("<body>")
for pic_tag in Soup.find_all('img'):
	pic_link = pic_tag.get('src')
	fo.write("<img src='")
	fo.write(pic_link)
	fo.write("'/>")
	download_links.append(pic_link)
#fo.write ("</body>")
#fo.write ("</html>")
fo.close()
urllib.urlcleanup()
print(shortname+" IS DONE")
