import wx
from Broadcast_Result import ProgressEvent



class FtpUploadTracker:
    sizeWritten = 0
    totalSize = 0
    lastShownPercent = 0

    def __init__(self, totalSize , window):
        self.totalSize = totalSize
        self.window = window

        print(self.window)


    def handle(self, block):
        self.sizeWritten += 1024
        percentComplete = round((self.sizeWritten / self.totalSize) * 100)

        wx.Yield()
        if (self.lastShownPercent != percentComplete):
            self.lastShownPercent = percentComplete
            wx.PostEvent(self.window, ProgressEvent(100, percentComplete))
            print(percentComplete)


