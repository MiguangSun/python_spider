'''
#作用域
i=10
def func():
    j=10
    print(j)
print(i)
func()
#print(j)
'''
'''
函数定义的格式：
def 函数名(参数):
    函数体
'''
def abc():
    print("abcde")
    print("456")
#调用函数：函数名(参数)
abc()
#参数：与外界沟通的接口
#参数：形参和实参
#一般在函数定义的时候使用的参数是形参
#一般再函数调用的时候使用的参数是实参
def func2(a,b):
    if(a>b):
        print(str(a)+"比"+str(b)+"大")
    else:
        print(str(b)+"比"+str(a)+"大或者"+str(b)+"与"+str(a)+"相等")
#4,5
func2(9,5)
func2(10,9)
#模块的导入
import cgi
cgi.closelog()
from cgi import closelog


#文件的操作
#打开
#open(文件地址,操作形式)
'''
w:写入
r：读取
b：二进制
a：追加
'''
fh=open("D:/我的教学/Python/腾讯-韬云教育-Python爬虫/文本1.txt","r",encoding="utf-8")
#文件读取
data=fh.read()
line=fh.readline()
x=0
'''
while True:
    line2=fh.readline()
    if(len(line)==0 and x>10):
        break
    print(line2)
    x+=1
fh.close()
'''
#关闭文件
fh.close()
#文件的写入(w/a+)
data="一起学Python！"
fh2=open("D:/我的教学/Python/腾讯-韬云教育-Python爬虫/文本3.txt","w")
fh2.write(data)
fh2.close()
fh2=open("D:/我的教学/Python/腾讯-韬云教育-Python爬虫/文本3.txt","w")
data2="学好Python！"
fh2.write(data2)
fh2.close()
fh3=open("D:/我的教学/Python/腾讯-韬云教育-Python爬虫/文本3.txt","a+")
fh3.write(data)
fh3.close()


































