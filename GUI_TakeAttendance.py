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
from Class import classes
from CONT import TakeAtt
import preferences
from VideoGenerator import video_stream
import cv2

###########################################################################
## Class MyPanel1
###########################################################################

class take_attendance_gui (wx.Panel):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 570,353 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )


		self.parent = parent.GetParent()

		bSizer6 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel6 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer7 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_panel7 = wx.Panel( self.m_panel6, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer5 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel4 = wx.Panel( self.m_panel7, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )


		#panel_separator = wx.BoxSizer( wx.VERTICAL )

		self.videoFrame = wx.Panel(self, -1, size=(640, 480))
		videoWarper = wx.StaticBox(self, size=(640, 480))
		videoBoxSizer = wx.StaticBoxSizer(videoWarper, wx.HORIZONTAL)
		videoBoxSizer.Add(self.videoFrame, 0)

		#self.videoFrame.SetBackgroundColour((0, 0, 0))

		capture = cv2.VideoCapture(0)

		#video_stream(self.videoFrame, capture)

		#panel_separator.Add(videoBoxSizer, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

		#self.m_panel4.SetSizer( panel_separator )
		#self.m_panel4.Layout()
		#panel_separator.Fit( self.m_panel4 )


		bSizer5.Add( videoBoxSizer, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_panel5 = wx.Panel( self.m_panel7, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		gSizer2 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_staticText11 = wx.StaticText( self.m_panel5, wx.ID_ANY, u"Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )

		gSizer2.Add( self.m_staticText11, 0, wx.ALL, 5 )

		self.m_textCtrl4 = wx.TextCtrl( self.m_panel5, wx.ID_ANY, u"Unknown", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer2.Add( self.m_textCtrl4, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText12 = wx.StaticText( self.m_panel5, wx.ID_ANY, u"ID", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )

		gSizer2.Add( self.m_staticText12, 0, wx.ALL, 5 )

		self.m_textCtrl5 = wx.TextCtrl( self.m_panel5, wx.ID_ANY, u"Unknown", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer2.Add( self.m_textCtrl5, 1, wx.ALL|wx.EXPAND, 5 )


		self.m_panel5.SetSizer( gSizer2 )
		self.m_panel5.Layout()
		gSizer2.Fit( self.m_panel5 )
		bSizer5.Add( self.m_panel5, 0, wx.ALL|wx.EXPAND, 5 )


		self.m_panel7.SetSizer( bSizer5 )
		self.m_panel7.Layout()
		bSizer5.Fit( self.m_panel7 )
		bSizer7.Add( self.m_panel7, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL|wx.EXPAND, 5 )

		self.m_panel8 = wx.Panel( self.m_panel6, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer8 = wx.BoxSizer( wx.VERTICAL )


		m_choice1Choices = []


		for x in classes.select_classes(preferences.mydb) :
			m_choice1Choices.append(x[0])


		print(m_choice1Choices)





		self.list_of_class = wx.Choice(self.m_panel8, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice1Choices, 0)
		self.list_of_class.SetSelection(0)
		bSizer8.Add(self.list_of_class, 0, wx.ALL | wx.EXPAND, 5)



		self.list_of_student = wx.dataview.DataViewListCtrl(self.m_panel8, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)
		self.m_dataViewListColumn6 = self.list_of_student.AppendTextColumn(u"Name", wx.dataview.DATAVIEW_CELL_INERT, -1, wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_RESIZABLE)
		self.m_dataViewListColumn7 = self.list_of_student.AppendTextColumn(u"ID", wx.dataview.DATAVIEW_CELL_INERT, -1, wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_RESIZABLE)
		bSizer8.Add(self.list_of_student, 1, wx.ALL | wx.EXPAND, 5)

		if len(m_choice1Choices) > 0 :
			for n in classes.retrive_list_of_student(preferences.mydb, str(self.list_of_class.GetString(self.list_of_class.GetSelection()))):
			   self.list_of_student.AppendItem(n)



		self.m_staticText3 = wx.StaticText( self.m_panel8, wx.ID_ANY, u"Already ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )

		bSizer8.Add( self.m_staticText3, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.student_already_absent = wx.dataview.DataViewListCtrl(self.m_panel8, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)
		self.m_dataViewListColumn4 = self.student_already_absent.AppendTextColumn(u"Name", wx.dataview.DATAVIEW_CELL_INERT, -1, wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_RESIZABLE)
		self.m_dataViewListColumn5 = self.student_already_absent.AppendTextColumn(u"ID", wx.dataview.DATAVIEW_CELL_INERT, -1, wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_RESIZABLE)
		self.m_dataViewListColumn61 = self.student_already_absent.AppendTextColumn(u"Time", wx.dataview.DATAVIEW_CELL_INERT, -1, wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_RESIZABLE)
		bSizer8.Add(self.student_already_absent, 1, wx.ALL | wx.EXPAND, 5)



		bSizer9 = wx.GridSizer( 0, 2, 0, 0 )

		self.Start_takeattnd = wx.Button(self.m_panel8, wx.ID_ANY, u"Start", wx.DefaultPosition, wx.DefaultSize, 0)
		bSizer9.Add(self.Start_takeattnd, 1, wx.ALL | wx.EXPAND, 5)

		#self.stop_takeattn = wx.ToggleButton(self.m_panel8, wx.ID_ANY, u"Pause", wx.DefaultPosition, wx.DefaultSize, 0)
		#bSizer9.Add(self.stop_takeattn, 1, wx.ALL | wx.EXPAND, 5)

		#self.cancel = wx.Button(self.m_panel8, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0)
		#bSizer9.Add(self.cancel, 1, wx.ALL | wx.EXPAND, 5)

		self.submit_attendance = wx.Button(self.m_panel8, wx.ID_ANY, u"Submit", wx.DefaultPosition, wx.DefaultSize, 0)
		bSizer9.Add(self.submit_attendance, 1, wx.ALL | wx.EXPAND, 5)

		self.submit_attendance.Disable()


		bSizer8.Add( bSizer9, 0, wx.EXPAND, 5 )







		self.m_panel8.SetSizer( bSizer8 )
		self.m_panel8.Layout()
		bSizer8.Fit( self.m_panel8 )
		bSizer7.Add( self.m_panel8, 1, wx.EXPAND |wx.ALL, 5 )


		self.m_panel6.SetSizer( bSizer7 )
		self.m_panel6.Layout()
		bSizer7.Fit( self.m_panel6 )
		bSizer6.Add( self.m_panel6, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( bSizer6 )
		self.Layout()

		self.Start_takeattnd.Bind( wx.EVT_BUTTON, self.start )
		#self.stop_takeattn.Bind( wx.EVT_TOGGLEBUTTON, self.stop )
		self.submit_attendance.Bind( wx.EVT_BUTTON, self.submit )

		self.submit_attendance.Disable()

		#self.cancel.Bind( wx.EVT_BUTTON, self.cancelfunc )
		self.list_of_class.Bind(wx.EVT_CHOICE, self.load_list)





	def __del__( self ):
		pass

	def start(self , event):

		myobject = event.GetEventObject()
		myobject.Disable()
		self.submit_attendance.Enable()
		self.cam = TakeAtt( self.videoFrame , self.parent)
		self.cam.begin_take_att(self.list_of_class.GetString(self.list_of_class.GetSelection()) , self.student_already_absent)


	def submit(self , event):

		self.Start_takeattnd.Enable()
		self.cam.sub()
		self.student_already_absent.DeleteAllItems()

		pass



	def load_list(self, event):

		self.list_of_student.DeleteAllItems()

		for n in classes.retrive_list_of_student(preferences.mydb , str(self.list_of_class.GetString(self.list_of_class.GetSelection()))) :
			self.list_of_student.AppendItem(n)


	def cancelfunc (self , event):

		self.cam.pause_or_stop()



