from urllib.request import urlopen as open
from tkinter import Tk
import win32com.client as win32

u = open("http://n.sinaimg.cn/news/1_img/dfic/34fa2aa3/62/w1024h638/20190510/4350-hwsffzc2527481.jpg")
x1= win32.gencache.EnsureDispatch('Excel.Application')
ss = x1.Workbooks.Add()
sh = ss.ActiveSheet
x1.Visible = True
sh.Cells(5,10).Valueu = u