from selenium import webdriver
import time
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import re
import urllib.request

dcap = dict(DesiredCapabilities.PHANTOMJS)  
dcap["phantomjs.page.settings.userAgent"] = ("Mozilla/4.0 (compatible; MSIE 5.5; windows NT)"  )  
browser = webdriver.PhantomJS(desired_capabilities=dcap)
#browser = webdriver.PhantomJS()
#browser.get("http://ac.qq.com/ComicView/index/id/538048/cid/3?fromPrev=1")
browser.get("http://ac.qq.com/ComicView/index/id/539443/cid/1")
a=browser.get_screenshot_as_file("D:/Python35/test.jpg")
for i in range(10):
    #browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    js='window.scrollTo('+str(i*1280)+','+str((i+1)*1280)+')'
    browser.execute_script(js)
    time.sleep(1)
#js="document.body.scrollTop=10000"#滚动条下拉1000px
#browser.execute_script(js)
#browser.implicitly_wait(300) 
print(browser.current_url)
data=browser.page_source
fh=open("D:/Python35/dongman.html","w",encoding="utf-8")
fh.write(data)
fh.close()
browser.quit()

pat='<img src="(http:..ac.tc.qq.com.store_file_download.buid=.*?name=.*?).jpg"'
allid=re.compile(pat).findall(data)
for i in range(0,len(allid)):
    thisurl=allid[i]
    thisurl2=thisurl.replace("amp;","")+".jpg"
    print(thisurl2)
    localpath="D:/Python35/dongman/"+str(i)+".jpg"
    urllib.request.urlretrieve(thisurl2,filename=localpath)
'''
#coding:utf-8
from selenium import webdriver
import time

driver = webdriver.PhantomJS()
driver.get('http://www.jianshu.com/collections')
time.sleep(1)
driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
for i in range(10):
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    time.sleep(1)
a=driver.get_screenshot_as_file("D:/Python35/test.jpg")
'''
