# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version May 30 2019)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
from CONT import  Regis_stud
from VideoGenerator import video_stream
###########################################################################
## Class MyPanel2
###########################################################################
import cv2



class student_registration_panel(wx.Panel):


    def __init__(self, parent, status_bar, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.Size(640, 480),
                 style=wx.TAB_TRAVERSAL, name=wx.EmptyString):
        wx.Panel.__init__(self, parent, id=id, pos=pos, size=size, style=style, name=name)

        self.status_bar = status_bar

        self.parent = parent

        panel_separator = wx.BoxSizer(wx.HORIZONTAL)

        self.videoFrame = wx.Panel(self, -1, size=(640, 480))
        videoWarper = wx.StaticBox(self, size=(640, 480))
        videoBoxSizer = wx.StaticBoxSizer(videoWarper, wx.HORIZONTAL)
        videoBoxSizer.Add(self.videoFrame, 0)

        self.videoFrame.SetBackgroundColour((0,0,0))

        # capture = cv2.VideoCapture(0)
        #
        #
        # video_stream(self.videoFrame, capture)
        #



        panel_separator.Add(videoBoxSizer, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.form_panel = wx.Panel(self,wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)

        registration_sizer = wx.BoxSizer(wx.VERTICAL)

        self.fillin_panel = wx.Panel(self.form_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        fillin_sizer = wx.FlexGridSizer(0, 2, 0, 0)
        fillin_sizer.SetFlexibleDirection(wx.BOTH)
        fillin_sizer.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_staticText20 = wx.StaticText(self.fillin_panel, wx.ID_ANY, u"Name", wx.DefaultPosition, wx.DefaultSize,
                                            0)
        self.m_staticText20.Wrap(-1)

        fillin_sizer.Add(self.m_staticText20, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL , 5)

        self.name_student = wx.TextCtrl(self.fillin_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                        wx.DefaultSize, 0)
        self.name_student.SetMinSize(wx.Size(200, -1))
        self.name_student.SetMaxSize(wx.Size (-1, -1))

        fillin_sizer.Add(self.name_student, 0, wx.ALL, 5)

        self.m_staticText21 = wx.StaticText(self.fillin_panel, wx.ID_ANY, u"Email", wx.DefaultPosition, wx.DefaultSize,
                                            0)
        self.m_staticText21.Wrap(-1)

        fillin_sizer.Add(self.m_staticText21, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL , 5)

        self.email_student = wx.TextCtrl(self.fillin_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                         wx.DefaultSize, 0)
        self.email_student.SetMinSize(wx.Size(200, -1))
        self.email_student.SetMaxSize(wx.Size(-1, -1))

        fillin_sizer.Add(self.email_student, 0, wx.ALL, 5)

        self.m_staticText22 = wx.StaticText(self.fillin_panel, wx.ID_ANY, u"ID Number", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText22.Wrap(-1)

        fillin_sizer.Add(self.m_staticText22, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL , 5)

        self.idNumber_student = wx.TextCtrl(self.fillin_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.idNumber_student.SetMinSize(wx.Size(200, -1))
        self.idNumber_student.SetMaxSize(wx.Size(-1, -1))

        fillin_sizer.Add(self.idNumber_student, 0, wx.ALL, 5)

        self.m_staticText24 = wx.StaticText(self.fillin_panel, wx.ID_ANY, u"Username", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText24.Wrap(-1)

        fillin_sizer.Add(self.m_staticText24, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.username_student = wx.TextCtrl(self.fillin_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.username_student.SetMinSize(wx.Size(200, -1))
        self.username_student.SetMaxSize(wx.Size(-1, -1))

        fillin_sizer.Add(self.username_student, 0, wx.ALL, 5)

        self.m_staticText23 = wx.StaticText(self.fillin_panel, wx.ID_ANY, u"Account Password", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText23.Wrap(-1)

        fillin_sizer.Add(self.m_staticText23, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.password_student = wx.TextCtrl(self.fillin_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.password_student.SetMinSize(wx.Size(200, -1))
        self.password_student.SetMaxSize(wx.Size(-1, -1))

        fillin_sizer.Add(self.password_student, 0, wx.ALL, 5)


        self.fillin_panel.SetSizer(fillin_sizer)
        self.fillin_panel.Layout()
        fillin_sizer.Fit(self.fillin_panel)
        registration_sizer.Add(self.fillin_panel, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.button_panel = wx.Panel(self.form_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        button_and_cameraselection_sizer = wx.GridSizer(0, 2, 0, 0)

        self.register = wx.Button(self.button_panel, wx.ID_ANY, u"Register", wx.DefaultPosition, wx.DefaultSize, 0)
        button_and_cameraselection_sizer.Add(self.register, 1, wx.ALL | wx.EXPAND, 5)

        # m_choice3Choices = []
        # self.collect_data = wx.Button(self.button_panel, wx.ID_ANY, u"Collect Data", wx.DefaultPosition, wx.DefaultSize, 0)
        # button_and_cameraselection_sizer.Add(self.collect_data, 1, wx.ALL | wx.EXPAND, 5)

        self.button_panel.SetSizer(button_and_cameraselection_sizer)
        self.button_panel.Layout()
        button_and_cameraselection_sizer.Fit(self.button_panel)
        registration_sizer.Add(self.button_panel, 0, wx.ALL | wx.EXPAND, 5)


        self.form_panel.SetSizer(registration_sizer)
        self.form_panel.Layout()
        registration_sizer.Fit(self.form_panel)
        panel_separator.Add(self.form_panel, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.SetSizer(panel_separator)
        self.Layout()

        self.register.Bind(wx.EVT_BUTTON, self.registerMeth)
        # self.collect_data.Bind(wx.EVT_BUTTON, self.collect_dt)



    def registerMeth(self, event ):

        name = self.name_student.GetValue()
        email = self.email_student.GetValue()
        username = self.username_student.GetValue()
        password = self.password_student.GetValue()
        id_num = self.idNumber_student.GetValue()

        if not name or  not email or not username or not password or not id_num:
            pass
        else :
            self.newstud = Regis_stud(self.parent, name, email, username, password, id_num, self.videoFrame)

            if self.newstud.check_duplicate()==True :
                self.newstud.Register()
            else :
                self.status_bar.SetLabel('Already Exist')
                self.status_bar.SetLabel('')

    # def collect_dt(self , event):
    #
    #     name = self.name_student.GetValue()
    #     email = self.email_student.GetValue()
    #     username = self.username_student.GetValue()
    #     password = self.password_student.GetValue()
    #     id_num = self.idNumber_student.GetValue()
    #











































