'''
#CSDN博文爬虫
import urllib.request
import re
url="http://blog.csdn.net/"
headers=("User-Agent","Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.22 Safari/537.36 SE 2.X MetaSr 1.0")
opener=urllib.request.build_opener()
opener.addheaders=[headers]
#安装为全局
urllib.request.install_opener(opener)
data=urllib.request.urlopen(url).read().decode("utf-8","ignore")
pat='<h3  class="tracking-ad" data-mod="popu_254"><a href="(.*?)"'
alllink=re.compile(pat).findall(data)
#print(alllink)
for i in range(0,len(alllink)):
    localpath="D:\\我的教学\\Python\\韬云教育-腾讯-Python爬虫\\rst\\"+str(i)+".html"
    thislink=alllink[i]
    urllib.request.urlretrieve(thislink,filename=localpath)
    print("当前文章(第"+str(i)+"篇）爬取成功！")
    
'''
'''
#糗事百科段子爬虫
import urllib.request
import re
headers=("User-Agent","Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.22 Safari/537.36 SE 2.X MetaSr 1.0")
opener=urllib.request.build_opener()
opener.addheaders=[headers]
#安装为全局
urllib.request.install_opener(opener)
for i in range(0,35):
    thisurl="http://www.qiushibaike.com/8hr/page/"+str(i+1)+"/?s=4948859"
    data=urllib.request.urlopen(thisurl).read().decode("utf-8","ignore")
    pat='<div class="content">.*?<span>(.*?)</span>.*?</div>'
    rst=re.compile(pat,re.S).findall(data)
    for j in range(0,len(rst)):
        print(rst[j])
        print("-------")

'''
'''
#用户代理池的构建
import urllib.request
import re
import random
uapools=[
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.22 Safari/537.36 SE 2.X MetaSr 1.0",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)",
    ]

def ua(uapools):
    thisua=random.choice(uapools)
    print(thisua)
    headers=("User-Agent",thisua)
    opener=urllib.request.build_opener()
    opener.addheaders=[headers]
    #安装为全局
    urllib.request.install_opener(opener)

for i in range(0,35):
    ua(uapools)
    thisurl="http://www.qiushibaike.com/8hr/page/"+str(i+1)+"/?s=4948859"
    data=urllib.request.urlopen(thisurl).read().decode("utf-8","ignore")
    pat='<div class="content">.*?<span>(.*?)</span>.*?</div>'
    rst=re.compile(pat,re.S).findall(data)
    for j in range(0,len(rst)):
        print(rst[j])
        print("-------")
'''
'''
#IP代理的构建实战
import urllib.request
ip="68.13.196.233:8080"
proxy=urllib.request.ProxyHandler({"http":ip})
opener=urllib.request.build_opener(proxy,urllib.request.HTTPHandler)
urllib.request.install_opener(opener)
url="http://www.baidu.com"
data1=urllib.request.urlopen(url).read()
data=data1.decode("utf-8","ignore")
print(len(data))
fh=open("D:\\我的教学\\Python\\韬云教育-腾讯-Python爬虫\\rst\\ip_baidu.html","wb")
fh.write(data1)
fh.close()
'''

'''
#IP代理池构建的第一种方案(适合于代理IP稳定的情况)
import random
import urllib.request
ippools=[
    "68.13.196.233:8080",
    "112.247.100.200:9999",
    "112.247.5.22:9999",
    ]
def ip(ippools):
    thisip=random.choice(ippools)
    print(thisip)
    proxy=urllib.request.ProxyHandler({"http":thisip})
    opener=urllib.request.build_opener(proxy,urllib.request.HTTPHandler)
    urllib.request.install_opener(opener)

for i in range(0,5):
    try:
        ip(ippools)
        url="http://www.baidu.com"
        data1=urllib.request.urlopen(url).read()
        data=data1.decode("utf-8","ignore")
        print(len(data))
        fh=open("D:\\我的教学\\Python\\韬云教育-腾讯-Python爬虫\\rst\\ip_baidu_"+str(i)+".html","wb")
        fh.write(data1)
        fh.close()
    except Exception as err:
        print(err)
'''
'''
#IP代理池实现的第二种方式（接口调用法，这种方法更适合于代理IP不稳定的情况）
import urllib.request
def api():
    print("这一次调用了接口")
    thisall=urllib.request.urlopen("http://tvp.daxiangdaili.com/ip/?tid=559126871522487&num=10&foreign=only")
    ippools=[]
    for item in thisall:
        ippools.append(item.decode("utf-8","ignore"))
    return ippools
def ip(ippools,time):
    thisip=ippools[time]
    print("当前用的IP是："+ippools[time])
    proxy=urllib.request.ProxyHandler({"http":thisip})
    opener=urllib.request.build_opener(proxy,urllib.request.HTTPHandler)
    urllib.request.install_opener(opener)
    
x=0
for i in range(0,35):
    try:
        if(x%10==0):
            time=x%10
            ippools=api()
            ip(ippools,time)
        else:
            time=x%10
            ip(ippools,time)
        url="http://www.baidu.com"
        data1=urllib.request.urlopen(url).read()
        data=data1.decode("utf-8","ignore")
        print(len(data))
        fh=open("D:\\我的教学\\Python\\韬云教育-腾讯-Python爬虫\\rst\\ip_baidu_"+str(i)+".html","wb")
        fh.write(data1)
        fh.close()
        x+=1
    except Exception as err:
        print(err)
        x+=1
'''
#淘宝商品图片爬虫
import urllib.request
import re
import random
keyname="维维豆奶"
key=urllib.request.quote(keyname)
uapools=[
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.22 Safari/537.36 SE 2.X MetaSr 1.0",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)",
    ]

def ua(uapools):
    thisua=random.choice(uapools)
    print(thisua)
    headers=("User-Agent",thisua)
    opener=urllib.request.build_opener()
    opener.addheaders=[headers]
    #安装为全局
    urllib.request.install_opener(opener)
for i in range(1,101):
    url="https://s.taobao.com/search?q="+key+"&s="+str((i-1)*44)
    ua(uapools)
    data=urllib.request.urlopen(url).read().decode("utf-8","ignore")
    pat='"pic_url":"//(.*?)"'
    imglist=re.compile(pat).findall(data)
    for j in range(0,len(imglist)):
        thisimg=imglist[j]
        thisimgurl="http://"+thisimg
        localfile="D:\\我的教学\\Python\\韬云教育-腾讯-Python爬虫\\rst\\taobao\\dounai\\"+str(i)+str(j)+".jpg"
        urllib.request.urlretrieve(thisimgurl,filename=localfile)
        



























