from uaip import *
import urllib.request
import re
key="Python"
for i in range(0,10):
    key=urllib.request.quote(key)
    thispageurl="http://weixin.sogou.com/weixin?oq=&query="+key+"&type=2&page="+str(i+1)+"&ie=utf8"
    thispagedata=ua_ip(thispageurl)
    print(len(thispagedata))
    pat1='<div class="txt-box">.*?href="(.*?)"'
    rst1=re.compile(pat1,re.S).findall(thispagedata)
    if(len(rst1)==0):
        print("这一页没有爬成功")
        continue
    for j in range(0,len(rst1)):
        thisurl=rst1[j]
        pat2='amp;'
        thisurl=thisurl.replace(pat2,"")
        print(thisurl)
        thisdata=ua_ip(thisurl)
        print("这篇文章爬取成功，长度为：" +str(len(thisdata)))
        fh=open("D:\\我的教学\\Python\\韬云教育-腾讯-Python爬虫\\rst\\weixin\\"+str(i)+str(j)+".html","w",encoding="utf-8")
        fh.write(thisdata)
        fh.close()
