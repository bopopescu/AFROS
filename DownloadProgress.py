import wx
from Broadcast_Result import ProgressEvent



class FtpDownloadTracker:
    sizeWritten = 0
    totalSize = 0
    lastShownPercent = 0

    def __init__(self, totalSize  , localfile , window):
        self.localfile = localfile
        self.totalSize = totalSize
        self.window = window

    def handle(self , data):

        self.sizeWritten += len(data)
        self.localfile.write(data)
        percentComplete = round((self.sizeWritten / self.totalSize) * 100)

        wx.Yield()
        if (self.lastShownPercent != percentComplete):
            self.lastShownPercent = percentComplete
            print(percentComplete)
            wx.PostEvent(self.window, ProgressEvent(100, percentComplete))



