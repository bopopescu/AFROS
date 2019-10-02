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
from Controller import alter_att
from Attendance import attendance
import preferences


###########################################################################
## Class MyPanel1
###########################################################################

class Alt_Attend(wx.Panel):


    def __init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.Size(500, 300), style=wx.TAB_TRAVERSAL,
                 name=wx.EmptyString):
        wx.Panel.__init__(self, parent, id=id, pos=pos, size=size, style=style, name=name)

        bSizer1 = wx.BoxSizer(wx.VERTICAL)

        self.m_panel1 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer4 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_treeCtrl3 = wx.TreeCtrl(self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                       wx.TR_DEFAULT_STYLE)

        self.root = self.m_treeCtrl3.AddRoot(preferences.name)

        res = classes.select_classes(preferences.mydb)

        for x in res:
            os = self.m_treeCtrl3.AppendItem(self.root, x[0])

            att = attendance.retrive_attendance_timestamp(preferences.mydb, x[1])
            #print (att)

            for y in att :
                self.m_treeCtrl3.AppendItem(os, str(y[0]), image=-1, selImage=-1, data=x[0])

        bSizer4.Add(self.m_treeCtrl3, 1, wx.ALL | wx.EXPAND, 5)


        self.m_panel3 = wx.Panel(self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer5 = wx.BoxSizer(wx.VERTICAL)

        self.m_dataViewListCtrl1 = wx.dataview.DataViewListCtrl(self.m_panel3, wx.ID_ANY, wx.DefaultPosition,
                                                                wx.DefaultSize, 0)
        self.m_dataViewListColumn1 = self.m_dataViewListCtrl1.AppendTextColumn(u"Name", wx.dataview.DATAVIEW_CELL_INERT,
                                                                               -1, wx.ALIGN_LEFT,
                                                                               wx.dataview.DATAVIEW_COL_RESIZABLE)
        self.m_dataViewListColumn2 = self.m_dataViewListCtrl1.AppendTextColumn(u"ID", wx.dataview.DATAVIEW_CELL_INERT,
                                                                               -1, wx.ALIGN_LEFT,
                                                                               wx.dataview.DATAVIEW_COL_RESIZABLE)
        self.m_dataViewListColumn3 = self.m_dataViewListCtrl1.AppendToggleColumn(u"Attendance", wx.dataview.DATAVIEW_CELL_ACTIVATABLE,
                                                                              -1, wx.ALIGN_CENTER,
                                                                              wx.dataview.DATAVIEW_COL_RESIZABLE)
        self.m_dataViewListColumn3 = self.m_dataViewListCtrl1.AppendToggleColumn(u"Medical",
                                                                                 wx.dataview.DATAVIEW_CELL_ACTIVATABLE,
                                                                                 -1, wx.ALIGN_CENTER,
                                                                                 wx.dataview.DATAVIEW_COL_RESIZABLE)


        bSizer5.Add(self.m_dataViewListCtrl1, 1, wx.ALL | wx.EXPAND, 5)

        self.m_button1 = wx.Button(self.m_panel3, wx.ID_ANY, u"Save", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer5.Add(self.m_button1, 0, wx.ALL | wx.EXPAND, 5)

        self.m_panel3.SetSizer(bSizer5)
        self.m_panel3.Layout()
        bSizer5.Fit(self.m_panel3)
        bSizer4.Add(self.m_panel3, 1, wx.EXPAND | wx.ALL, 5)

        self.m_panel1.SetSizer(bSizer4)
        self.m_panel1.Layout()
        bSizer4.Fit(self.m_panel1)
        bSizer1.Add(self.m_panel1, 1, wx.EXPAND | wx.ALL, 5)

        self.SetSizer(bSizer1)
        self.Layout()

        self.m_treeCtrl3.Bind(wx. EVT_LEFT_DCLICK ,  self.tree)
        self.m_dataViewListCtrl1.Bind(wx.dataview.EVT_DATAVIEW_ITEM_VALUE_CHANGED, self.checkbox_clicked, id=wx.ID_ANY)
        self.m_button1.Bind(wx.EVT_BUTTON , self.save)


    def tree(self, event):

        self.m_dataViewListCtrl1.DeleteAllItems()

        self.subj = self.m_treeCtrl3.GetItemData(self.m_treeCtrl3.GetSelection())
        self.time = self.m_treeCtrl3.GetItemText(self.m_treeCtrl3.GetSelection())


        res = attendance.retrive_attendace_list_based_timestamp(preferences.mydb , preferences.name+"_"+self.subj , self.time)
        res2 = classes.retrive_list_of_student(preferences.mydb ,self.subj )

        print(res)

        row_att = (res[0][1 : len(res[0])])
        print (row_att)

        temp = []

        for x , y  in zip(res2 , row_att) :

            if y == 'PRESENT' :
               temp.append((x[0],x[1],True , False))
            elif y == 'MEDICAL':
               temp.append((x[0], x[1],False , True))
            else :
               temp.append((x[0], x[1], False, False))


        for n in temp :
            id_num = int(n[1])
            self.m_dataViewListCtrl1.AppendItem(n , data=id_num)

        print(temp)

    def checkbox_clicked(self, event):

        att = self.m_dataViewListCtrl1.GetToggleValue(self.m_dataViewListCtrl1.GetSelectedRow() , 2)
        med = self.m_dataViewListCtrl1.GetToggleValue(self.m_dataViewListCtrl1.GetSelectedRow() , 3)

        if att == True and med == True :
            self.m_dataViewListCtrl1.SetToggleValue(False , self.m_dataViewListCtrl1.GetSelectedRow(), 2)
            self.m_dataViewListCtrl1.SetToggleValue(False , self.m_dataViewListCtrl1.GetSelectedRow(), 3)

    def save (self , event):

        temp = []

        for x in range (self.m_dataViewListCtrl1.GetItemCount()):

            att = self.m_dataViewListCtrl1.GetToggleValue(x, 2)
            med = self.m_dataViewListCtrl1.GetToggleValue(x, 3)
            data = self.m_dataViewListCtrl1.GetItemData(self.m_dataViewListCtrl1.RowToItem(x))

            if med == False :
                if att == True :
                    temp.append((data , 'PRESENT'))
                else :
                    temp.append((data , 'ABSENT'))
            else :
                temp.append((data , 'MEDICAL'))

        alter_att(self.subj , self.time , temp)


    def __del__(self):
        pass





