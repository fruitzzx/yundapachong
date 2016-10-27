from SqlHelpter import *
#conding-utf8
import re
import urllib.request
import urllib
import time;  # 引入time模块

ticks = time.time()
url='http://office.zzuli.edu.cn'

def getHtml(url): 
    page=urllib.request.urlopen(url)
    html=page.read()
    return html.decode('utf-8')
def getDSJ(html):
    reg=r"<a href=['\"](.*?)['\"](.*?)>(.*?)</a>"
    lsre=re.compile(reg)
    ls=re.finditer(lsre,html)
    return ls
	

		
html=getHtml(url)
ls=getDSJ(html)
fd=open(r'theBigDate2.txt','a+')
print("ID"+"    "+"名字")
x=0
sql=SqlHelpter()
reghtml=r"^http://"
murl=re.compile(reghtml)
for item in ls:
	try:
		urls=item.group(1).replace("'","")
		title=item.group(3).replace("'","")
		if murl.match(urls):
			print("")
		else:
			urls=url+urls
		fd.write(title+"  --  "+urls+"\n")
		x=x+1
		sql.insert(title,urls)
		print(title+"    "+urls)
	except Exception :
		print("发生异常")
fd.close()
print("总共有"+str(x)+"个")
