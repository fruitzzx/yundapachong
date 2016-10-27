import re
import urllib.request
import urllib
from SqlHelpter import *
from collections import deque

def gettitle(data):
  titlere=r"<title>(.*?)</title>"
  retitle=re.compile(titlere)
  return retitle.findall(data)[0]
#使用队列存放url
queue = deque()
#使用visited防止重复爬同一页面
visited = set()

url = 'http://www.ynu.edu.cn/'  # 入口页面, 可以换成别的
 #入队最初的页面
queue.append(url)
cnt = 0

while queue:
  url = queue.popleft()  # 队首元素出队
  visited |= {url}  # 标记为已访问

  print('已经抓取: ' + str(cnt) + '   正在抓取 <---  ' + url)
  cnt += 1

  try:
      #抓取页面
      urlop = urllib.request.urlopen(url,timeout=10)
      
      
  except Exception:
      print("超时")
      continue
  #判断是否为html页面
  if 'html' not in urlop.getheader('Content-Type'):
    continue

  # 避免程序异常中止, 用try..catch处理异常
  try:
   #转换为utf-8码
    data = urlop.read().decode('utf-8')
    urllib.request.urlretrieve(url,'F://exerciese//dug//'+gettitle(data)+'.html')
  except:
    continue
  reg=r"<a href=['\"](.*?)['\"](.*?)>(.*?)</a>"
  lsre=re.compile(reg)
  ls=re.finditer(lsre,data)
  sql=SqlHelpter()
  reghtml=r"^http://"
  murl=re.compile(reghtml)
  x=0
  # 正则表达式提取页面中所有队列, 并判断是否已经访问过, 然后加入待爬队列
  for item in ls:
    urls=item.group(1).replace("'","")
    title=item.group(3).replace("'","")
    if murl.match(urls):
      print("")
    else:
      urls=url+urls
    x=x+1
    sql.insert(title,urls,data)
    queue.append(urls)
    print(title+"    "+urls)


