"""
    以面向对象思想,描述下列情景.
    需求：老张开车去东北
    理念：分而治之 变则疏之
         数据的变化  行为的变化
            对象       类
    变化：
            老张  老李  老王 -->  人类
            车   飞机   骑车 -->  车类 飞机类 自行车类
            东北  西北  回家 --> 不做类(没行为,没多种数据)
    类与类交互(跨类调用)：
        直接创建对象
        在构造函数创建对象
        通过参数传递对象
"""

# 写法1：直接创建对象
# 语义：老张每次创建一辆新车去....
"""
class Person:
    def __init__(self, name=""):
        self.name = name

    def go_to(self,position):
        print("去",position)
        car = Car()
        car.run()

class Car:
    def run(self):
        print("跑喽～")

# 用对象区分数据不同
lz = Person("老张")
ll = Person("老李")
lw = Person("老王")

lz.go_to("东北")
"""

# 写法2：在构造函数中创建对象
# 语义：老张开自己的车去....
"""
class Person:
    def __init__(self, name=""):
        self.name = name
        self.car = Car()

    def go_to(self,position):
        print("去",position)
        # 自身对象.自身变量(车对象)
        # 车对象.车方法
        # 对象.实例成员
        self.car.run()

class Car:
    def run(self):
        print("跑喽～")

# 用对象区分数据不同
lz = Person("老张") 

lz.go_to("东北")
"""

# 方式3：通过参数传递
# 语义：老张用交通工具去....
class Person:
    def __init__(self, name=""):
        self.name = name

    def go_to(self,vehicle,position):
        print("去",position)
        vehicle.run()

class Car:
    def run(self):
        print("跑喽～")

# 用对象区分数据不同
lz = Person("老张")
car = Car()
lz.go_to(car,"东北")
