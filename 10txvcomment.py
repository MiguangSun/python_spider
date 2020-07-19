#1、腾讯视频评论爬虫（单页评论爬虫）:获取深度解读评论内容
'''
import urllib.request
import re
#https://video.coral.qq.com/filmreviewr/c/upcomment/[视频id]?commentid=[评论id]&reqnum=[每次提取的评论的个数]
vid="j6cgzhtkuonf6te"
cid="6233603654052033588"
num="20"
#构造当前评论网址
url="https://video.coral.qq.com/filmreviewr/c/upcomment/"+vid+"?commentid="+cid+"&reqnum="+num
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.22 Safari/537.36 SE 2.X MetaSr 1.0",
        "Content-Type":"application/javascript",
         }
opener=urllib.request.build_opener()
headall=[]
for key,value in headers.items():
    item=(key,value)
    headall.append(item)
opener.addheaders=headall
urllib.request.install_opener(opener)
#爬取当前评论页面
data=urllib.request.urlopen(url).read().decode("utf-8")
titlepat='"title":"(.*?)"'
commentpat='"content":"(.*?)"'
titleall=re.compile(titlepat,re.S).findall(data)
commentall=re.compile(commentpat,re.S).findall(data)
for i in range(0,len(titleall)):
    try:
        print("评论标题是:"+eval('u"'+titleall[i]+'"'))
        print("评论内容是:"+eval('u"'+commentall[i]+'"'))
        print("------")
    except Exception as err:
        print(err)
'''
#2、腾讯视频评论爬虫（自动切换下一页评论的爬虫）:获取深度解读评论内容
'''
import urllib.request
import re
#https://video.coral.qq.com/filmreviewr/c/upcomment/[视频id]?commentid=[评论id]&reqnum=[每次提取的评论的个数]
vid="j6cgzhtkuonf6te"
cid="6233603654052033588"
num="3"
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.22 Safari/537.36 SE 2.X MetaSr 1.0",
        "Content-Type":"application/javascript",
         }
opener=urllib.request.build_opener()
headall=[]
for key,value in headers.items():
    item=(key,value)
    headall.append(item)
opener.addheaders=headall
urllib.request.install_opener(opener)
for j in range(0,100):
    #爬取当前评论页面
    print("第"+str(j)+"页")
    thisurl="https://video.coral.qq.com/filmreviewr/c/upcomment/"+vid+"?commentid="+cid+"&reqnum="+num
    data=urllib.request.urlopen(thisurl).read().decode("utf-8")
    titlepat='"title":"(.*?)","abstract":"'
    commentpat='"content":"(.*?)"'
    titleall=re.compile(titlepat,re.S).findall(data)
    commentall=re.compile(commentpat,re.S).findall(data)
    lastpat='"last":"(.*?)"'
    cid=re.compile(lastpat,re.S).findall(data)[0]
    for i in range(0,len(titleall)):
        try:
            print("评论标题是:"+eval('u"'+titleall[i]+'"'))
            print("评论内容是:"+eval('u"'+commentall[i]+'"'))
            print("------")
        except Exception as err:
            print(err)

'''

#获取短评内容
import urllib.request
import re
#https://coral.qq.com/article/1743283224/comment?commentid=6237632351690994016&reqnum=20
vid="1743283224"
cid="6237632351690994016"
num="20"
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.22 Safari/537.36 SE 2.X MetaSr 1.0",
        "Content-Type":"application/javascript",
         }
opener=urllib.request.build_opener()
headall=[]
for key,value in headers.items():
    item=(key,value)
    headall.append(item)
opener.addheaders=headall
urllib.request.install_opener(opener)
for j in range(0,100):
    #爬取当前评论页面
    print("第"+str(j)+"页")
    thisurl="https://coral.qq.com/article/"+vid+"/comment?commentid="+cid+"&reqnum="+num
    data=urllib.request.urlopen(thisurl).read().decode("utf-8")
    #titlepat='"title":"(.*?)","abstract":"'
    commentpat='"content":"(.*?)"'
    #titleall=re.compile(titlepat,re.S).findall(data)
    commentall=re.compile(commentpat,re.S).findall(data)
    lastpat='"last":"(.*?)"'
    cid=re.compile(lastpat,re.S).findall(data)[0]
    for i in range(0,len(commentall)):
        try:
            print("评论内容是:"+eval('u"'+commentall[i]+'"'))
            print("------")
        except Exception as err:
            print(err)







        
