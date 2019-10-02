import wx
import wx.xrc
import wx.dataview
import wx.adv
from Student import Student
from CONT import create_classs
import mysql.connector


class create_class_panel(wx.Panel):

    def __init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.Size(500, 400), style=wx.TAB_TRAVERSAL,
                 name=wx.EmptyString ):
        wx.Panel.__init__(self, parent, id=id, pos=pos, size=size, style=style, name=name)

        self.parent = parent.GetParent()


        bSizer13 = wx.BoxSizer(wx.VERTICAL)

        self.AddClass = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer3 = wx.BoxSizer(wx.VERTICAL)

        self.m_panel9 = wx.Panel(self.AddClass, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer6 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText6 = wx.StaticText(self.m_panel9, wx.ID_ANY, u"Database", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText6.Wrap(-1)

        bSizer6.Add(self.m_staticText6, 1, wx.ALIGN_CENTER | wx.ALL, 5)

        self.m_staticText7 = wx.StaticText(self.m_panel9, wx.ID_ANY, u"Your Class", wx.DefaultPosition, wx.DefaultSize,
                                           0)
        self.m_staticText7.Wrap(-1)

        bSizer6.Add(self.m_staticText7, 1, wx.ALL, 5)

        self.m_panel9.SetSizer(bSizer6)
        self.m_panel9.Layout()
        bSizer6.Fit(self.m_panel9)
        bSizer3.Add(self.m_panel9, 0, wx.ALL | wx.EXPAND, 5)

        self.m_panel6 = wx.Panel(self.AddClass, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer41 = wx.BoxSizer(wx.HORIZONTAL)

        self.database_of_student = wx.dataview.DataViewListCtrl(self.m_panel6, wx.ID_ANY, wx.DefaultPosition,
                                                                wx.DefaultSize, 0)
        self.name_of_student = self.database_of_student.AppendTextColumn(u"Name", wx.dataview.DATAVIEW_CELL_INERT,
                                                                         -1, wx.ALIGN_LEFT,
                                                                         wx.dataview.DATAVIEW_COL_RESIZABLE)
        self.Id_of_student = self.database_of_student.AppendTextColumn(u"ID", wx.dataview.DATAVIEW_CELL_INERT,
                                                                       -1, wx.ALIGN_LEFT,
                                                                       wx.dataview.DATAVIEW_COL_RESIZABLE)
        bSizer41.Add(self.database_of_student, 1, wx.ALL | wx.EXPAND, 5)

        mydb = mysql.connector.connect(host='127.0.0.1 ', user='raihan', passwd='wuJWY3wHZmWwXAIs', database='project')

        res = Student.get_student(mydb)

        for i in res:
            self.database_of_student.AppendItem(i)

        self.student_added = wx.dataview.DataViewListCtrl(self.m_panel6, wx.ID_ANY, wx.DefaultPosition,
                                                          wx.DefaultSize, 0)
        self.name_of_student_added = self.student_added.AppendTextColumn(u"Name", wx.dataview.DATAVIEW_CELL_INERT,
                                                                         -1, wx.ALIGN_LEFT,
                                                                         wx.dataview.DATAVIEW_COL_RESIZABLE)
        self.id_student_added = self.student_added.AppendTextColumn(u"ID", wx.dataview.DATAVIEW_CELL_INERT,
                                                                    -1, wx.ALIGN_LEFT,
                                                                    wx.dataview.DATAVIEW_COL_RESIZABLE)
        bSizer41.Add(self.student_added, 1, wx.ALL | wx.EXPAND, 5)

        self.m_panel6.SetSizer(bSizer41)
        self.m_panel6.Layout()
        bSizer41.Fit(self.m_panel6)
        bSizer3.Add(self.m_panel6, 1, wx.EXPAND | wx.ALL, 5)

        self.m_panel7 = wx.Panel(self.AddClass, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer5 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_searchCtrl2 = wx.SearchCtrl(self.m_panel7, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                           0)
        self.m_searchCtrl2.ShowSearchButton(False)
        self.m_searchCtrl2.ShowCancelButton(False)
        bSizer5.Add(self.m_searchCtrl2, 1, wx.ALL, 5)

        #self.m_searchCtrl3 = wx.SearchCtrl(self.m_panel7, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                           #0)
        #self.m_searchCtrl3.ShowSearchButton(False)
        #self.m_searchCtrl3.ShowCancelButton(False)
        #bSizer5.Add(self.m_searchCtrl3, 1, wx.ALL, 5)

        self.m_panel7.SetSizer(bSizer5)
        self.m_panel7.Layout()
        bSizer5.Fit(self.m_panel7)
        bSizer3.Add(self.m_panel7, 0, wx.ALL | wx.EXPAND, 5)

        self.m_panel8 = wx.Panel(self.AddClass, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        fgSizer2 = wx.FlexGridSizer(0, 4, 0, 0)
        fgSizer2.SetFlexibleDirection(wx.BOTH)
        fgSizer2.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_staticText1 = wx.StaticText(self.m_panel8, wx.ID_ANY, u"Day", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1.Wrap(-1)

        fgSizer2.Add(self.m_staticText1, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.data_day_of_class = wx.TextCtrl(self.m_panel8, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(150, -1),
                                             0)
        fgSizer2.Add(self.data_day_of_class, 0, wx.ALL, 5)

        self.m_staticText2 = wx.StaticText(self.m_panel8, wx.ID_ANY, u"Subject", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText2.Wrap(-1)

        fgSizer2.Add(self.m_staticText2, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.data_subject_of_class = wx.TextCtrl(self.m_panel8, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(150, -1),
                                                 0)
        fgSizer2.Add(self.data_subject_of_class, 0, wx.ALL, 5)

        self.m_staticText3 = wx.StaticText(self.m_panel8, wx.ID_ANY, u"Time Start", wx.DefaultPosition, wx.DefaultSize,
                                           0)
        self.m_staticText3.Wrap(-1)

        fgSizer2.Add(self.m_staticText3, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.data_time_start = wx.adv.TimePickerCtrl(self.m_panel8, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition,
                                                     wx.Size(150, -1), wx.adv.TP_DEFAULT)
        fgSizer2.Add(self.data_time_start, 0, wx.ALL, 5)

        self.m_staticText4 = wx.StaticText(self.m_panel8, wx.ID_ANY, u"Time End", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText4.Wrap(-1)

        fgSizer2.Add(self.m_staticText4, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.data_time_end = wx.adv.TimePickerCtrl(self.m_panel8, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition,
                                                   wx.Size(150, -1), wx.adv.TP_DEFAULT)
        fgSizer2.Add(self.data_time_end, 0, wx.ALL, 5)

        self.Location_statictext = wx.StaticText(self.m_panel8, wx.ID_ANY, u"Location", wx.DefaultPosition, wx.DefaultSize, 0)
        self.Location_statictext.Wrap(-1)

        fgSizer2.Add(self.Location_statictext, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.data_location = wx.TextCtrl(self.m_panel8, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(150, -1), 0)
        fgSizer2.Add(self.data_location, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_panel8.SetSizer(fgSizer2)
        self.m_panel8.Layout()
        fgSizer2.Fit(self.m_panel8)
        bSizer3.Add(self.m_panel8, 0, wx.ALL | wx.EXPAND | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.button_create_class = wx.Button(self.AddClass, wx.ID_ANY, u"Create Class", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer3.Add(self.button_create_class, 0, wx.ALL | wx.EXPAND, 5)

        self.AddClass.SetSizer(bSizer3)
        self.AddClass.Layout()
        bSizer3.Fit(self.AddClass)
        bSizer13.Add(self.AddClass, 1, wx.EXPAND | wx.ALL, 5)

        self.SetSizer(bSizer13)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.database_of_student.Bind(wx.dataview.EVT_DATAVIEW_ITEM_ACTIVATED,
                                      self.m_dataViewListCtrl3OnDataViewListCtrlItemActivated, id=wx.ID_ANY)
        self.student_added.Bind(wx.dataview.EVT_DATAVIEW_ITEM_ACTIVATED,
                                self.m_dataViewListCtrl4OnDataViewListCtrlItemActivated, id=wx.ID_ANY)

        self.temporary_data = []

        self.button_create_class.Bind( wx.EVT_BUTTON , self.create_class)
        self.m_searchCtrl2.Bind(wx.EVT_TEXT, self.m_searchCtrl1OnTextEnter)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def m_dataViewListCtrl3OnDataViewListCtrlItemActivated(self, event):

        if str(self.database_of_student.GetValue(self.database_of_student.GetSelectedRow(), 1)) in self.temporary_data:
            pass
        else:
            test = [str(self.database_of_student.GetValue(self.database_of_student.GetSelectedRow(), 0)),
                    str(self.database_of_student.GetValue(self.database_of_student.GetSelectedRow(), 1))]
            self.student_added.AppendItem(test)
            self.temporary_data.append(
                str(self.database_of_student.GetValue(self.database_of_student.GetSelectedRow(), 1)))

    def m_dataViewListCtrl4OnDataViewListCtrlItemActivated(self, event):

        self.temporary_data.remove(str(self.student_added.GetValue(self.student_added.GetSelectedRow(), 1)))
        self.student_added.DeleteItem(self.student_added.GetSelectedRow())
        self.student_added.UnselectAll()

    def create_class(self , event):

        day = self.data_day_of_class.GetValue()
        subject = self.data_subject_of_class.GetValue()
        timestart = self.data_time_start.GetTime()
        timeend = self.data_time_end.GetTime()
        location = self.data_location.GetValue()

        create_classs(day , subject , timestart , timeend , location , self.temporary_data , self.parent)

    def m_searchCtrl1OnTextEnter(self, event):

        self.database_of_student.DeleteAllItems()

        res = Student.search_student_likely(self.m_searchCtrl2.GetValue())

        print (res)

        for i in res:
            self.database_of_student.AppendItem(i)






