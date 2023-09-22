import wx
import wx.xrc
import wx.aui

import threading
import time

from widgets.Plt_Shop import *
from widgets.MainFrame import *

app = wx.App(False)
frame = MainFrame(parent=None)
frame.Show()

def secondPass():
    while True:
        for lot in frame.lots:
            if lot.plt != None: 
                lot.plant(None)
        time.sleep(1)

x = threading.Thread(target=secondPass)
x.start()


app.MainLoop()

