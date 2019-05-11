#!/usr/bin/env python

from tkinter import Tk
from time import sleep
from tkinter.messagebox import showwarning
import win32com.client as win32

warn = lambda app: showwarning(app, 'Exit?')
RANGE = range(3, 8)


def word():
    app = 'Word'
    word = win32.gencache.EnsureDispatch('%s.Application'% app)
    doc = word.Documents.Add()
    word.Visible = True
    sleep(1)

    rng = doc.Range(0, 0)
    rng.InsertAfter('Python-to-%s Test\n\n' % app)
    sleep(1)
    for i in RANGE:
        rng.InsertAfter('Line %d\n' % i)
        sleep(1)
    rng.InsertAfter("\nTh-th-th-that's all folks!\n")

    warn(app)
    doc.Close(False)
    word.Application.Quit()


Tk().withdraw()
word()
