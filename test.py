from GUI_ViewAttend_Stud import Stud_viewAtt
import wx







app = wx.App(False)

mainparent = wx.Frame(None)
frame = Stud_viewAtt(None)
frame.Show(True)

app.MainLoop()

