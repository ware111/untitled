import re


class Test:
    def regex1(self):
        value = ("bat", "bit", "but", "hat")
        for val in value:
            v = re.match('b.t', val)
            if v is not None:
                print(v.group())

    def regex2(self):
        value = "pan hai ming"
        val = re.split(' ',value)
        print(val)

    def regex3(self):
        value = "www.baidu.com"
        val = re.match('(^www\.).+(\.com$)', value)
        print(val.group(1))


t = Test()
t.regex1()
t.regex2()
t.regex3()

