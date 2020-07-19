#print("Hello Python!")
"""
print("Hello Python!")
print("Hello Python!")
print("Hello Python!")
print("Hello Python!")
"""
#print("Hello Python!")
abc=9
'''
数、字符串、列表、元组、集合、字典
'''
a1='abc'
a2="abc"
a3='''abc'''
#列表：存储多个元素的东西,列表里面的元素是可以重新赋值的
b=[7,"cd",9]
#元组：存储多个元素的东西,元组里面的元素是不可以重新赋值的
c=(7,"cd",9)
#字典
#{键：值，键：值，…}
#取值格式：字典名["对应键名"]
d={"name":"weiwei","sex":"boy","job":"teacher"}
#集合
#集合：去重
'''
e=set("abcgjkhsgkjha")
f=set("jikhsdghsdueigdsfzau")
g=e-f

#运算符+-*/%
h=5+9*2-1
i=19%2
j="hello Python"
#+字符串连接符
k="abc"+j
'''
#缩进
'''
b="9"
if(b=="9"):
    print("abc")
'''
'''
#if
a=100
b=1
if(a>19 and a<30):
    print(a)
    if(b<9):
        print(b)
elif(a>9 and a<=19):
    print("a>9 and a<=19")
elif(a<9):
    print("a<9")
else:
    print("gsdajk")

#while
a=0
while(a<10):
    print("hello")
    a+=1
#for
#for:遍历列表
a=["aa","b","c","d"]
for i in a:
    print(i)
#for:进行常规循环
#for i in range(0,10)
for i in range(0,10):
    print("hello A")

#continue、break
#break：全部直接退出,整个循环都中断
#continue:中断一次循环，继续下一次循环
for i in a:
    if(i=="c"):
        #break
        continue 
    print(i)
'''


#乘法口诀
#end=""代表不换行输出
for i in range(1,10):
    for j in range(1,i+1):
        print(str(i)+"*"+str(j)+"="+str(i*j),end="  ")
    print()
#作业：逆向输出乘法口诀表

















