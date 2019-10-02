# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version May 30 2019)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import cv2
from GUI_RegisterStudent import student_registration_panel
from GUI_RegisterLecturer import lecturer_registration
from GUI_Home import lecturer
from GUI_ViewAttend_Stud import Stud_viewAtt
from Controller import login
import Broadcast_Result
from utils import CFEVideoConf, image_resize


###########################################################################
## Class Login
###########################################################################

class Login ( wx.Frame ) :


	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.CAPTION|wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.main_sizer = wx.BoxSizer( wx.VERTICAL )

		##########################
		# login and button module ###############################################################################
		##########################

		self.m_panel8 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		wSizer3 = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		self.username = wx.StaticText(self.m_panel8, wx.ID_ANY, u"Username", wx.DefaultPosition, wx.DefaultSize, 0)
		self.username.Wrap(-1)

		wSizer3.Add(self.username, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

		self.username_cntrl = wx.TextCtrl(self.m_panel8, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(200, -1), 0)
		wSizer3.Add(self.username_cntrl, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

		self.passwrd = wx.StaticText(self.m_panel8, wx.ID_ANY, u"Password", wx.DefaultPosition, wx.DefaultSize, 0)
		self.passwrd.Wrap(-1)

		wSizer3.Add(self.passwrd, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 5)

		self.password_cntrl = wx.TextCtrl(self.m_panel8, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(200, -1), 0)
		wSizer3.Add(self.password_cntrl, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)



		wSizer3.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		type_userChoices = [ u"Student", u"Lecturer" ]
		self.type_user = wx.RadioBox( self.m_panel8, wx.ID_ANY, u"Sign Up or Log In as", wx.DefaultPosition, wx.DefaultSize, type_userChoices, 1, wx.RA_SPECIFY_ROWS )
		wSizer3.Add( self.type_user, 1, wx.ALL|wx.EXPAND, 5 )

		self.Log_in = wx.Button( self.m_panel8, wx.ID_ANY, u"Log in", wx.DefaultPosition, wx.DefaultSize, 0 )
		wSizer3.Add( self.Log_in, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		self.m_panel8.SetSizer( wSizer3 )
		self.m_panel8.Layout()
		wSizer3.Fit( self.m_panel8 )
		self.main_sizer.Add( self.m_panel8, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_gauge1 = wx.Gauge( self, wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL )
		self.m_gauge1.SetValue( 0 )
		self.main_sizer.Add( self.m_gauge1, 0, wx.EXPAND, 5 )



		self.status_bar = self.CreateStatusBar(2, wx.STB_SIZEGRIP, wx.ID_ANY)


		self.registrationPanel = student_registration_panel(self,  self.status_bar)

		self.lecturer_registrationpanel = lecturer_registration(self)
		self.lecturer_registrationpanel.Hide()
		self.registrationPanel.Show()


		self.main_sizer.Add( self.registrationPanel , 0, wx.ALL|wx.EXPAND, 5 )
		self.main_sizer.Add(self.lecturer_registrationpanel ,0, wx.ALL|wx.EXPAND, 5)



		self.SetSizer( self.main_sizer )
		self.Layout()
		self.main_sizer.Fit( self )

		self.Centre( wx.BOTH )

		# Connect Events
		self.Log_in.Bind( wx.EVT_BUTTON, self.login )
		self.type_user.Bind( wx.EVT_RADIOBOX, self.radiobox)

		Broadcast_Result.EVT_RESULT(self, self.OnResult)
		Broadcast_Result.EVT_PROGRESS(self , self.OnProgress)

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def login( self, event ):

		username = self.username_cntrl.GetValue()
		passwrd = self.password_cntrl.GetValue()

		if not passwrd and not username :
			pass
		else :

			acre = login(username , passwrd, self.type_user.GetSelection())

			if acre.result() :

				if self.type_user.GetSelection() == 0:

					self.registrationPanel.Hide()

					self.loggedinStud = Stud_viewAtt(self)
					self.main_sizer.Add(self.loggedinStud ,0, wx.ALL|wx.EXPAND, 5)


       				# acre.save_to_sqlLite(0)
					# app = wx.App(False)
					# frame = Stud_viewAtt(None)
					# frame.Show(True)
					# app.MainLoop()
				else :

					self.Close()

					acre.save_to_sqlLite(1)
					app = wx.App(False)
					frame = lecturer(None)
					frame.Show(True)
					app.MainLoop()


					pass

			else:
				print('fail')


	def radiobox(self, event):
		if self.type_user.GetSelection() == 0 :
			self.lecturer_registrationpanel.Hide()
			self.registrationPanel.Show()

			self.SetSize(wx.Size(1020, 600))
			print(3)
		else :
			self.registrationPanel.Hide()
			self.lecturer_registrationpanel.Show()

			self.SetSize(wx.Size(1020, 400))
			print(1)


	def OnResult(self, event):

		if event.data is None:
			# Thread aborted (using our convention of None return)
			self.status_bar.SetLabel('Stand By')
		else:
			# Process results here
			print(event.data)
			self.status_bar.SetLabel(event.data)

	def OnProgress(self , event):
		print(event.data)
		print(event.Range)
		self.m_gauge1.SetValue(int(event.data))
		self.m_gauge1.SetRange(int(event.Range))

		pass







