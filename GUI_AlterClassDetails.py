# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version May 30 2019)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.adv
import wx.xrc
import wx.propgrid as pg
import datetime
import wx.dataview
from Class import classes
from CONT import AlterClass
from CONT import Delete_Class
import preferences


###########################################################################
## Class MyPanel1
###########################################################################

class AlterCLS(wx.Panel):

    def __init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.Size(677, 414), style=wx.TAB_TRAVERSAL,
                 name=wx.EmptyString):
        wx.Panel.__init__(self, parent, id=id, pos=pos, size=size, style=style, name=name)

        bSizer1 = wx.BoxSizer(wx.VERTICAL)

        self.m_panel1 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer2 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_panel2 = wx.Panel(self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer3 = wx.BoxSizer(wx.VERTICAL)


        # self.coloumn
        #
        #
        # bSizer3.Add(self.m_propertyGrid2, 1, wx.ALL | wx.EXPAND, 5)

        sub = classes.retrive_classes_based_lecturer(preferences.mydb)

        print(sub)





        self.m_dataViewListCtrl1 = wx.dataview.DataViewListCtrl(self.m_panel2, wx.ID_ANY, wx.DefaultPosition,
                                                                wx.DefaultSize, 0)
        self.m_dataViewListColumn1 = self.m_dataViewListCtrl1.AppendTextColumn(u"Subject", wx.dataview.DATAVIEW_CELL_INERT, -1,
                                                                               wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_RESIZABLE)

        for x in sub :
            self.m_dataViewListCtrl1.AppendItem(x)

        bSizer3.Add(self.m_dataViewListCtrl1, 1, wx.ALL | wx.EXPAND, 5)

        Result = wx.GridSizer(0, 2, 0, 0)

        self.m_staticText1 = wx.StaticText(self.m_panel2, wx.ID_ANY, u"Day", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1.Wrap(-1)

        Result.Add(self.m_staticText1, 0, wx.ALL, 5)

        self.day = wx.TextCtrl(self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        Result.Add(self.day, 0, wx.ALL | wx.EXPAND, 5)

        self.m_staticText2 = wx.StaticText(self.m_panel2, wx.ID_ANY, u"Time Start", wx.DefaultPosition, wx.DefaultSize,
                                           0)
        self.m_staticText2.Wrap(-1)

        Result.Add(self.m_staticText2, 0, wx.ALL, 5)

        self.time_start = wx.adv.TimePickerCtrl(self.m_panel2, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition,
                                                wx.DefaultSize, wx.adv.TP_DEFAULT)
        Result.Add(self.time_start, 0, wx.ALL | wx.EXPAND, 5)

        self.m_staticText3 = wx.StaticText(self.m_panel2, wx.ID_ANY, u"Time End", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText3.Wrap(-1)

        Result.Add(self.m_staticText3, 0, wx.ALL, 5)

        self.time_end = wx.adv.TimePickerCtrl(self.m_panel2, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition,
                                              wx.DefaultSize, wx.adv.TP_DEFAULT)
        Result.Add(self.time_end, 0, wx.ALL | wx.EXPAND, 5)

        self.m_staticText4 = wx.StaticText(self.m_panel2, wx.ID_ANY, u"Location", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText4.Wrap(-1)

        Result.Add(self.m_staticText4, 0, wx.ALL, 5)

        self.location = wx.TextCtrl(self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        Result.Add(self.location, 0, wx.ALL | wx.EXPAND, 5)

        bSizer3.Add(Result, 0, wx.EXPAND, 5)

        self.m_button2 = wx.Button(self.m_panel2, wx.ID_ANY, u"Save Changes", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer3.Add(self.m_button2, 0, wx.ALL | wx.EXPAND, 5)

        self.m_panel2.SetSizer(bSizer3)
        self.m_panel2.Layout()
        bSizer3.Fit(self.m_panel2)
        bSizer2.Add(self.m_panel2, 1, wx.EXPAND | wx.ALL, 5)

        self.m_panel3 = wx.Panel(self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer4 = wx.BoxSizer(wx.VERTICAL)

        self.m_dataViewListCtrl3 = wx.dataview.DataViewListCtrl(self.m_panel3, wx.ID_ANY, wx.DefaultPosition,
                                                                wx.DefaultSize, 0)
        self.m_dataViewListColumn3 = self.m_dataViewListCtrl3.AppendTextColumn(u"Name", wx.dataview.DATAVIEW_CELL_INERT, -1,
                                                                               wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_RESIZABLE)
        self.m_dataViewListColumn4 = self.m_dataViewListCtrl3.AppendTextColumn(u"ID", wx.dataview.DATAVIEW_CELL_INERT, -1,
                                                                               wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_RESIZABLE)
        bSizer4.Add(self.m_dataViewListCtrl3, 1, wx.ALL | wx.EXPAND, 5)

        self.m_button1 = wx.Button(self.m_panel3, wx.ID_ANY, u"Delete Class", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer4.Add(self.m_button1, 0, wx.ALL | wx.EXPAND, 5)

        self.m_panel3.SetSizer(bSizer4)
        self.m_panel3.Layout()
        bSizer4.Fit(self.m_panel3)
        bSizer2.Add(self.m_panel3, 1, wx.EXPAND | wx.ALL, 5)

        self.m_panel1.SetSizer(bSizer2)
        self.m_panel1.Layout()
        bSizer2.Fit(self.m_panel1)
        bSizer1.Add(self.m_panel1, 1, wx.EXPAND | wx.ALL, 5)

        self.SetSizer(bSizer1)
        self.Layout()

        # Connect Events
        self.m_dataViewListCtrl1.Bind(wx.dataview.EVT_DATAVIEW_ITEM_ACTIVATED,
                                      self.m_dataViewListCtrl1OnDataViewListCtrlItemActivated, id=wx.ID_ANY)
        self.m_button2.Bind(wx.EVT_BUTTON, self.m_button2OnButtonClick)
        self.m_button1.Bind(wx.EVT_BUTTON, self.m_button1OnButtonClick)

    def m_dataViewListCtrl1OnDataViewListCtrlItemActivated(self, event):

        self.m_dataViewListCtrl3.DeleteAllItems()

        name_of_subj = str(self.m_dataViewListCtrl1.GetValue(self.m_dataViewListCtrl1.GetSelectedRow() , 0 ))

        querry = classes.retrive_classDetails_based_subject(preferences.mydb , name_of_subj)[0]

        print(querry[1])

        tim_s = datetime.datetime.strptime( str(querry[1]) , '%H:%M:%S' )
        time_e = datetime.datetime.strptime( str(querry[2]) , '%H:%M:%S' )


        self.day.SetValue(querry[0])

        self.time_start.SetTime(tim_s.hour , tim_s.minute , tim_s.second)

        self.time_end.SetTime(time_e.hour , time_e.minute , time_e.second)

        self.location.SetValue(querry[3])


        list_of_stud = classes.retrive_list_of_student(preferences.mydb , name_of_subj)

        for x in list_of_stud :
            self.m_dataViewListCtrl3.AppendItem(x)

        print(list_of_stud)



    def m_button2OnButtonClick(self, event):

        name_of_subj = str(self.m_dataViewListCtrl1.GetValue(self.m_dataViewListCtrl1.GetSelectedRow() , 0 ))

        AlterClass(name_of_subj ,self.time_start.GetTime() ,  self.time_end.GetTime() ,self.location.GetValue() , self.day.GetValue())


    def m_button1OnButtonClick(self, event):

        name_of_subj = str(self.m_dataViewListCtrl1.GetValue(self.m_dataViewListCtrl1.GetSelectedRow() , 0 ))

        Delete_Class(name_of_subj)

