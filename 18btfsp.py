from bs4 import BeautifulSoup as bs
import urllib.request
data=urllib.request.urlopen("http://edu.iqianyue.com/").read().decode("utf-8","ignore")
bs1=bs(data)
#格式化输出
#print(bs1.prettify())
#获取标签：bs对象.标签名
bs1.title
#获取标签里面的文字:bs对象.标签名.string
bs1.title.string
#获取标签名：bs对象.标签名.name
bs1.title.name
#获取属性列表：bs对象.标签名.attrs
bs1.a.attrs
#获取某个属性对应的值:bs对象.标签名[属性名] 或者 bs对象.标签名.get(属性名)
bs1.a["class"]
bs1.a.get("class")
#提取所有某个节点的内容：bs对象.find_all('标签名') bs对象.find_all(['标签名1','标签名2，…,标签n'])
bs1.find_all('a')
bs1.find_all(['a','ul'])
#提取所有子节点:bs对象.标签.contents bs对象.标签.children
k1=bs1.ul.contents
k2=bs1.ul.children
allulc=[i for i in k2]
#更多信息可以阅读官方文档：http://beautifulsoup.readthedocs.io/zh_CN/latest/
