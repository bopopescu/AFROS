###########################################################################
## Python code generated with wxFormBuilder (version May 30 2019)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.dataview
from Attendance import attendance
import preferences

###########################################################################
## Class MyFrame1
###########################################################################

class Stud_viewAtt(wx.Panel):

    def __init__(self, parent ,  id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
        wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )


        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        bSizer1 = wx.BoxSizer(wx.VERTICAL)

        self.m_panel1 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer2 = wx.BoxSizer(wx.VERTICAL)

        gSizer1 = wx.GridSizer(0, 3, 0, 0)

        self.m_staticText2 = wx.StaticText(self.m_panel1, wx.ID_ANY, preferences.id , wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText2.Wrap(-1)

        gSizer1.Add(self.m_staticText2, 0, wx.ALL, 5)

        self.m_staticText3 = wx.StaticText(self.m_panel1, wx.ID_ANY, u"Student Record", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText3.Wrap(-1)

        gSizer1.Add(self.m_staticText3, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.m_staticText4 = wx.StaticText(self.m_panel1, wx.ID_ANY, preferences.name, wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText4.Wrap(-1)

        gSizer1.Add(self.m_staticText4, 0, wx.ALL | wx.ALIGN_RIGHT, 5)

        bSizer2.Add(gSizer1, 0, wx.EXPAND | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.m_dataViewListCtrl1 = wx.dataview.DataViewListCtrl(self.m_panel1, wx.ID_ANY, wx.DefaultPosition,
                                                                wx.DefaultSize, 0)

        self.m_dataViewListColumn0 = self.m_dataViewListCtrl1.AppendTextColumn(u"Lecturer",
                                                                               wx.dataview.DATAVIEW_CELL_INERT, -1,
                                                                               wx.ALIGN_LEFT,
                                                                               wx.dataview.DATAVIEW_COL_RESIZABLE)

        self.m_dataViewListColumn1 = self.m_dataViewListCtrl1.AppendTextColumn(u"Subject", wx.dataview.DATAVIEW_CELL_INERT, -1,
                                                                               wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_RESIZABLE)
        self.m_dataViewListColumn3 = self.m_dataViewListCtrl1.AppendTextColumn(u"Number Of Absent",
                                                                               wx.dataview.DATAVIEW_CELL_INERT, -1,
                                                                               wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_RESIZABLE)
        self.m_dataViewListColumn2 = self.m_dataViewListCtrl1.AppendTextColumn(u"Medical", wx.dataview.DATAVIEW_CELL_INERT, -1,
                                                                               wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_RESIZABLE)
        bSizer2.Add(self.m_dataViewListCtrl1, 1, wx.ALL | wx.EXPAND, 5)


        querry = attendance.viewAttnd_as_Stud(preferences.mydb , preferences.id)

        for x in  querry :
            self.m_dataViewListCtrl1.AppendItem(x)

        self.m_panel1.SetSizer(bSizer2)
        self.m_panel1.Layout()
        bSizer2.Fit(self.m_panel1)
        bSizer1.Add(self.m_panel1, 1, wx.EXPAND | wx.ALL, 5)

        self.SetSizer(bSizer1)
        self.Layout()

        self.Centre(wx.BOTH)


    def __del__(self):
        pass
