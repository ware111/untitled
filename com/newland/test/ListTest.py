#-*- coding: UTF-8 -*-
class Test:
    """测试代码"""

    def __init__(self, value1, value2):
        self.value1 = value1
        self.value2 = value2

    def count(self):
            value = int(self.value1) + int(self.value2)
            return value

"""
while True:
    value3 = input("请输入第一个值：\n")
    value4 = input("请输入第二个值：\n")
    if int(value4) > int(value3):
        break

test = Test(value3, value4)
test.count()
print(test.count())

"""