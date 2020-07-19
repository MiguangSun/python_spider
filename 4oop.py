#类和对象
'''
创建一个类
class 类名:
    类里面的内容
'''
class cl1:
    pass
'''
实例化一个类：
a=cl1()
'''

#构造函数（构造方法）
#self:在类中的方法必须加上self参数
#__init__(self,参数)
#构造函数实际意义：初始化
class cl2:
    def __init__(self):
        print("I am cl2 self!")

#给类加上参数:给构造方法加上参数
class cl3:
    def __init__(self,name,job):
        print("My name is "+name+" My job is "+job)

#属性:类里面的变量:self.属性名
class cl4:
    def __init__(self,name,job):
        self.myname=name
        self.myjob=job

#方法：类里面的函数：def 方法名(self,参数)
class cl5:
    def myfunc1(self,name):
        print("hello "+name)

class cl6:
    def __init__(self,name):
        self.myname=name
    def myfunc1(self):
        print("hello "+self.myname)

#继承（单继承，多继承）
#某一个家庭有父亲、母亲、儿子、女儿，父亲可以说话，母亲可以写字，大儿子继承了父亲
#女儿同时继承了父母，并且有新能力听东西，小儿子继承了父亲，但是优化（减弱）了父亲的说话能力
#
#父亲类(基类)
class father():
    def speak(self):
        print("I can speak!")
#单继承：class 子类(父类)
class son(father):
    pass
#母亲类
class mother():
    def write(self):
        print("I can write")
#多继承
class daughter(father,mother):
    def listen(self):
        print("I can listen!")
#重写（重载）
class son2(father):
    def speak(self):
        print("I can speak 2!")
















