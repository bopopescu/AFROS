import preferences
import cv2
import ftplib
from VideoGenerator import video_stream
from Attendance import attendance
from datetime import datetime
from Broadcast_Result import ProgressEvent
from Broadcast_Result import ResultEvent
from DownloadProgress import FtpDownloadTracker
import wx

class take_attendance :

    def __init__(self , videoframe , window):

        self.window = window
        self.videopanel = videoframe

        self.ftp = ftplib.FTP()
        self.ftp.connect(preferences.host , preferences.port)

        self.ftp.login(preferences.username, preferences.password)

        self.ftp.cwd('/Class/')

        #pass


    def begin_take_attendance(self , subject , gui_list ):

        self.subject =  str(subject)
        self.list = gui_list

        self.recognizer = preferences.name + "_" + self.subject + ".yml"
        wx.PostEvent(self.window, ResultEvent(" Downloading yml file ... "))
        localfile = open('recognizers/' + self.recognizer, 'wb')
        totalsz = self.ftp.size(self.recognizer)
        p = FtpDownloadTracker(totalsz, localfile, self.window)
        self.ftp.retrbinary('RETR ' + self.recognizer, p.handle, 1024)
        localfile.close()


        self.pickle = preferences.name + "_" + self.subject + ".pickle"
        wx.PostEvent(self.window, ResultEvent(" Downloading pickle file ... "))
        localfile = open('pickles/' + self.pickle, 'wb')
        totalsz = self.ftp.size(self.recognizer)
        pr = FtpDownloadTracker(totalsz, localfile, self.window)
        self.ftp.retrbinary('RETR ' + self.pickle, pr.handle, 1024)
        localfile.close()

        self.ftp.quit()

        self.capture = cv2.VideoCapture(0)

        self.cam = video_stream(self.videopanel ,self.capture)
        self.cam.start_face_recognitiona(preferences.name + "_" + self.subject ,self.list )


        self.table_id = preferences.name + "_" + self.subject



    def submit(self):
        now = datetime.now()

        self.cam.close_video()
        data =  self.cam.submit_data()
        attendance.submit_attendance(preferences.mydb , self.table_id , data , now.strftime("%m%d%Y")+now.strftime("%H%M%S") )
        self.list.DeleteAllItems()