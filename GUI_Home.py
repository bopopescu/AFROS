# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version May 30 2019)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.dataview
import wx.adv
from GUI_CreateClass import create_class_panel
from GUI_TakeAttendance import take_attendance_gui
from GUI_AlterAttendance import Alt_Attend
from GUI_AlterClassDetails import AlterCLS
import Broadcast_Result

###########################################################################
## Class Menus
###########################################################################

class lecturer (wx.Frame):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 631,438 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer4 = wx.BoxSizer( wx.VERTICAL )

		self.TAB = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.AddClass = create_class_panel(self.TAB , wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.TakeAttnd = take_attendance_gui(self.TAB, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
		self.AltAtt = Alt_Attend(self.TAB, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
		self.Altcl = AlterCLS(self.TAB, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)




		self.TAB.AddPage( self.AddClass, u"Add Class", False )
		self.TAB.AddPage( self.TakeAttnd, u"Take Attendance", False )
		self.TAB.AddPage( self.AltAtt , u"Change And View Attendance" ,  False)
		self.TAB.AddPage( self.Altcl , u"Edit Class" ,  False)




		bSizer4.Add( self.TAB, 1, wx.EXPAND, 5 )


		self.m_gauge2 = wx.Gauge( self, wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL )
		bSizer4.Add( self.m_gauge2, 0, wx.EXPAND, 5 )


		self.SetSizer( bSizer4 )
		self.Layout()
		self.m_statusBar2 = self.CreateStatusBar( 1, wx.STB_SIZEGRIP, wx.ID_ANY )
		self.m_menubar1 = wx.MenuBar( 0 )
		self.m_menu1 = wx.Menu()
		self.m_menubar1.Append( self.m_menu1, u"Settings" )

		self.m_menu5 = wx.Menu()
		self.m_menubar1.Append( self.m_menu5, u"Help" )

		self.SetMenuBar( self.m_menubar1 )


		self.Centre( wx.BOTH )

		Broadcast_Result.EVT_RESULT(self, self.OnResult)
		Broadcast_Result.EVT_PROGRESS(self, self.OnProgress)


	def OnResult(self, event):

		if event.data is None:
			# Thread aborted (using our convention of None return)
			self.m_statusBar2.SetLabel('Stand By')
		else:
			# Process results here
			print(event.data)
			self.m_statusBar2.SetLabel(event.data)

	def OnProgress(self , event):
		print(event.data)
		print(event.Range)
		self.m_gauge2.SetValue(int(event.data))
		self.m_gauge2.SetRange(int(event.Range))

		pass
