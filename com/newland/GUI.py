import wx
top = wx.Panel()
sizer = wx.BoxSizer(wx.VERTICAL)
font = wx.Font(9, wx.SWISS, wx.NORMAL, wx.BOLD)
lb = wx.StaticText(top, -1, 'Animals(in pairs;min:pair, max: dozen)')
sizer.Add(lb)

cl = wx.StaticText(top, -1, 'Number:')
cl.SetFont(font)
ct = wx.SpinCtrl(top, -1, '2', min=2, max=12)
sizer.Add(ct)

c2 = wx.StaticText(top, -1, 'Type:')
c2.SetFont(font)
cb = wx.ComboBox(top, -1, '', choices=('dog', 'cat', 'hamster', 'python'))
sizer.Add(c2)
sizer.Add(cb)

qb = wx.Button(top, -1, 'QUIT')
qb.SetBackgroundColour('red')
qb.SetForegroundColour('white')
sizer.Add(qb)
top.SetSize(sizer)
