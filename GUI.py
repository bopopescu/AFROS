import wx
from GUI_EntranceMenu import Login
from GUI_Home import lecturer
from GUI_ViewAttend_Stud import Stud_viewAtt


def EntranceMenus():
	app = wx.App(False)
	frame = Login(None)
	frame.Show(True)
	app.MainLoop()

def HomeLecturer():
	app = wx.App(False)
	frame = lecturer(None)
	frame.Show(True)
	app.MainLoop()

def HomeStudent():
	app = wx.App(False)
	frame = Stud_viewAtt(None)
	frame.Show(True)
	app.MainLoop()









