'''
#出版社爬取
import urllib.request
import re
data=urllib.request.urlopen("https://read.douban.com/provider/all").read().decode("utf-8")
pat='<div class="name">(.*?)</div>'
rst=re.compile(pat).findall(data)
fh=open("D:\\我的教学\\Python\\韬云教育-腾讯-Python爬虫\\chubanshe.txt","w")
for i in range(0,len(rst)):
    print(rst[i])
    fh.write(rst[i]+"\n")
fh.close()
'''
'''
#urllib基础
import urllib.request
#urlretrieve(网址,本地文件存储地址) 直接下载网页到本地
urllib.request.urlretrieve("http://www.baidu.com","D:\\我的教学\\Python\\韬云教育-腾讯-Python爬虫\\dld.html")
urllib.request.urlcleanup()
#看网页相应的简介信息info()
file=urllib.request.urlopen("https://read.douban.com/provider/all")
print(file.info())
#返回网页爬取的状态码getcode()
print(file.getcode())
#获取当前访问的网页的url，geturl()
print(file.geturl())
'''
'''
#超时设置
import urllib.request
for i in range(0,100):
    try:
        file=urllib.request.urlopen("http://www.baidu.com",timeout=1)
        print(len(file.read().decode("utf-8")))
    except Exception as err:
        print("出现异常"+str(err))

'''
'''
#get请求实战--实现百度信息自动搜索
import urllib.request,re
keywd="韦玮"
keywd=urllib.request.quote(keywd)
#page=(num-1)*10
for i in range(1,11):
    url="http://www.baidu.com/s?wd="+keywd+"&pn="+str((i-1)*10)
    data=urllib.request.urlopen(url).read().decode("utf-8")
    pat="title:'(.*?)',"
    pat2='"title":"(.*?)",'
    rst1=re.compile(pat).findall(data)
    rst2=re.compile(pat2).findall(data)
    for j in range(0,len(rst1)):
        print(rst1[j])
    for z in range(0,len(rst2)):
        print(rst2[z])

'''
'''
#post请求实战
import urllib.request
import urllib.parse
posturl="http://www.iqianyue.com/mypost/"
postdata=urllib.parse.urlencode({
    "name":"ceo@txk7.com",
    "pass":"kjsahgjkashg",
    }).encode("utf-8")
#进行post，就需要使用urllib.request下面的Request(真实post地址,post数据)
req=urllib.request.Request(posturl,postdata)
rst=urllib.request.urlopen(req).read().decode("utf-8")
fh=open("D:\\我的教学\\Python\\韬云教育-腾讯-Python爬虫\\post.html","w")
fh.write(rst)
fh.close()
'''
#异常处理
'''
URLError出现的原因：
1）连不上服务器
2）远程url不存在
3）无网络
4）触发HTTPError
'''
'''
import urllib.request
import urllib.error
try:
    urllib.request.urlopen("http://blog.csdn.net")
except urllib.error.URLError as e:
    if hasattr(e,"code"):
        print(e.code)
    if hasattr(e,"reason"):
        print(e.reason)
'''
'''
#浏览器伪装
import urllib.request
url="http://blog.csdn.net"
#头文件格式header=("User-Agent",具体用户代理值)
headers=("User-Agent","Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.22 Safari/537.36 SE 2.X MetaSr 1.0")
opener=urllib.request.build_opener()
opener.addheaders=[headers]
data=opener.open(url).read()
fh=open("D:\\我的教学\\Python\\韬云教育-腾讯-Python爬虫\\ua.html","wb")
fh.write(data)
fh.close()
#需要研究的问题
#1、（以后会讲，大家先探索）如何将opener安装为全局，让urlopen()访问时也添加对应报头？
#2、研究一下使用Request的方式进行报头添加。（非重点，不讲，自行探索研究）
'''

#爬取腾讯新闻首页所有新闻内容
'''
1、爬取新闻首页
2、得到各新闻链接
3、爬取新闻链接
4、寻找有没有frame
5、若有，抓取frame下对应网页内容
6、若没有，直接抓取当前页面
'''
import urllib.request
import re
url="http://news.qq.com/"
data=urllib.request.urlopen(url).read().decode("UTF-8","ignore")
pat1='<a target="_blank" class="linkto" href="(.*?)"'
alllink=re.compile(pat1).findall(data)
for i in range(0,len(alllink)):
    thislink=alllink[i]
    thispage=urllib.request.urlopen(thislink).read().decode("gb2312","ignore")
    pat2="<frame src=(.*?)>"
    isframe=re.compile(pat2).findall(thispage)
    if(len(isframe)==0):
        #直接爬
        print(i)
        urllib.request.urlretrieve(thislink,"D:\\我的教学\\Python\\韬云教育-腾讯-Python爬虫\\data\\"+str(i)+".html")
    else:
        #得到frame的网址爬
        flink=isframe[0]
        urllib.request.urlretrieve(flink,"D:\\我的教学\\Python\\韬云教育-腾讯-Python爬虫\\data\\"+str(i)+".html")







































