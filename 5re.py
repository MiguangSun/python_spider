import re
string="taoyunjiaoyu"
#普通字符作为原子
pat="yun"
#正则表达式函数
rst=re.search(pat,string)
print(rst)
#非打印字符作为原子
#\n 换行符  \t   制表符
string='''taoyunjiaoyubaidu'''
pat="\n"
rst=re.search(pat,string)
print(rst)

#通用字符作为原子
'''
\w 字母、数字、下划线
\W 除字母、数字、下划线
\d 十进制数字
\D 除十进制数字
\s 空白字符
\S 除空白字符
'''
string='''taoyunji8 7362387aoyubaidu'''
pat="\w\d\s\d\d"
rst=re.search(pat,string)
print(rst)
#原子表
string='''taoyunji87362387aoyubaidu'''
pat="tao[y]un"
pat="tao[^abc]"
rst=re.search(pat,string)
print(rst)

#元字符
'''
. 除换行外任意一个字符
^ 开始位置
$ 结束位置
* 0\1\多次 
? 0\1次
+ 1\多次
{n} 恰好n次
{n,} 至少n次
{n,m} 至少n，至多m次 
| 模式选择符或
() 模式单元
'''
string='''taoyunnnnji87362387aoyubaidu'''
pat="tao..."
pat="^ao..."
pat="bai..$"
pat="tao.*"
pat="taoyun+"
pat="yun{1,2}"

rst=re.search(pat,string)
print(rst)

#模式修正符
'''
I 匹配时忽略大小写*
M 多行匹配*
L 本地化识别匹配
U unicode
S 让.匹配包括换行符*
'''
string="Python"
pat="pyt"
rst=re.search(pat,string,re.I)
print(rst)

#贪婪模式与懒惰模式
string="poythonyhjskjsa"
pat1="p.*y"#贪婪模式
pat2="p.*?y"#懒惰模式，精准
rst=re.search(pat1,string,re.I)
rst2=re.search(pat2,string,re.I)
print(rst)
print(rst2)

#正则表达式函数
#1、match
string="poythonyhjskjsa"
pat="p.*?y"#懒惰模式，精准
rst=re.match(pat,string,re.I)
print(rst)
#2、search 已讲
#3、全局匹配函数
string="hgpoythpnyhjsptjhgjykjsa"
pat="p.*?y"#懒惰模式，精准
#全局匹配格式re.compile(正则表达式).findall(数据)
rst=re.compile(pat).findall(string)
print(rst)

#实例：匹配.com和.cn网址
string="<a href='ftp://www.iqianyue.com'>百度首页</a>'"
pat="[a-zA-Z]+://[^\s]*[.com|.cn]"
rst=re.compile(pat).findall(string)
print(rst)
#实例：匹配电话号码
string="jsghajsdhk021-8928874997678328jhdjskgjkh0773-776257672360kjcxdhkj"
pat="\d{4}-\d{7}|\d{3}-\d{8}"
rst=re.compile(pat).findall(string)
print(rst)



#简单爬虫的编写
import urllib.request
data=urllib.request.urlopen("http://edu.csdn.net").read()

#自动提取课程页面的QQ群
import urllib.request
import re
data=urllib.request.urlopen("http://edu.csdn.net/huiyiCourse/detail/253").read().decode("utf-8")
pat="<em>QQ:(\d*?)</em>"
rst=re.compile(pat).findall(data)
print(rst[0])



























