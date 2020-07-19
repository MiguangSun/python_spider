#在Urllib模块下使用XPath表达式
import urllib.request
from lxml import etree
data=urllib.request.urlopen("http://www.baidu.com").read().decode("utf-8","ignore")
treedata=etree.HTML(data)
title=treedata.xpath("//title/text()")
if(str(type(title))=="<class 'list'>"):
    pass
else:
    title=[i for i in title]
print(title[0])
