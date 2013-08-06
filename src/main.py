'''
Created on Aug 1, 2013

@author: mlecce
'''
import wx
import ui

if __name__ == '__main__':
    app = wx.App(False)
    frame = ui.MyApp(None, "Tweet Generator")
    app.MainLoop()
