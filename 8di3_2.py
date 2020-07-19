#如何同时使用用户代理池和IP代理池
def ua_ip(myurl):
    import random
    uapools=[
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393",
        "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.22 Safari/537.36 SE 2.X MetaSr 1.0",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)",
        ]
    import urllib.request
    def api():
        print("这一次调用了接口")
        thisall=urllib.request.urlopen("http://tvp.daxiangdaili.com/ip/?tid=559126871522487&num=10&foreign=only&filter=on")
        ippools=[]
        for item in thisall:
            ippools.append(item.decode("utf-8","ignore"))
        return ippools
    def ip(ippools,time,uapools):
        thisua=random.choice(uapools)
        print(thisua)
        headers=("User-Agent",thisua)
        thisip=ippools[time]
        print("当前用的IP是："+ippools[time])
        proxy=urllib.request.ProxyHandler({"http":thisip})
        opener=urllib.request.build_opener(proxy,urllib.request.HTTPHandler)
        opener.addheaders=[headers]
        urllib.request.install_opener(opener)
        
    x=0
    for i in range(0,35):
        try:
            if(x%10==0):
                time=x%10
                ippools=api()
                ip(ippools,time,uapools)
            else:
                time=x%10
                ip(ippools,time,uapools)
            url=myurl
            data1=urllib.request.urlopen(url).read()
            data=data1.decode("utf-8","ignore")
            print(len(data))
            #fh=open("D:\\我的教学\\Python\\韬云教育-腾讯-Python爬虫\\rst\\ip_baidu_"+str(i)+".html","wb")
            #fh.write(data1)
            #fh.close()
            x+=1
            break
        except Exception as err:
            print(err)
            x+=1
    return data
#data=ua_ip("http://www.baidu.com")








    
