import cv2
import threading
import os
import mysql.connector
import time
import ftplib
from zipfile import ZipFile
from Student import Student
from threading import *
import preferences
import Broadcast_Result
from Broadcast_Result import ResultEvent
from Broadcast_Result import ProgressEvent
from VideoGenerator import video_stream
import wx
from UploadProgress import FtpUploadTracker



class Add_Student(wx.Panel):

    def __init__(self, name, email, username, password, id_num, window , capture , video_frame ):

        wx.Panel.__init__(self, video_frame , wx.ID_ANY, (0, 0), (640, 480))

        #Thread.__init__(self)
        self.name = name
        self.email = email
        self.username = username
        self.password = password
        self.id_num = id_num
        self.window = window
        self.capture = capture
        self.mydb = preferences.mydb
        self.video_frame = video_frame
        self.num_frames = preferences.num_frames
        self.n = 0



        self.location = self.id_num

        self.face_cascade = cv2.CascadeClassifier('cascade/haarcascade_frontalface_default.xml')




        ret, frame = self.capture.read()

        height, width = frame.shape[:2]

        video_frame.SetSize((width, height))

        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        self.bmp = wx.Bitmap.FromBuffer(width, height, frame)


        self.Bind(wx.EVT_PAINT, self.OnPaint)


        self.run()

    def OnPaint(self, evt):
        dc = wx.BufferedPaintDC(self)
        dc.DrawBitmap(self.bmp, 0, 0)


    def run(self):

        dirName = self.location
        zipFileName = self.location+".zip"
        os.makedirs(self.location)


        while (True):

            wx.Yield()
            self.ret, frame = self.capture.read()

            face_found = 0

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            faces = self.face_cascade.detectMultiScale(
                gray,
                scaleFactor=1.1,
                minNeighbors=5,
                minSize=(30, 30),
            )

            # Draw a rectangle around the faces
            for (x, y, w, h) in faces:
                roi_gray = gray[y:y + h, x:x + w]  # (ycord_start, ycord_end)
                roi_color = frame[y:y + h, x:x + w]
                face_found += 1

                # recognize? deep learned model predict keras tensorflow pytorch scikit learn

                if (self.num_frames != 0):

                    if face_found > 1:
                        pass
                        wx.PostEvent(self.window,
                                     ResultEvent("multiple faces detected , must only one face registered ! "))
                    elif face_found == 0:
                        pass
                        wx.PostEvent(self.window,
                                     ResultEvent(
                                         "no face detected , data collection paused until face detected ! "))
                    else:
                        wx.PostEvent(self.window, ResultEvent(
                            "dont move until data collection finish " + " | frames left : " + str(self.num_frames)))
                        print(self.num_frames)
                        wx.PostEvent(self.window, ProgressEvent(self.num_frames, self.n))
                        self.n += 1
                        self.num_frames -= 1
                        cv2.imwrite(self.location + "/frame%d.jpg" % self.num_frames, frame)

                color = (255, 0, 0)  # BGR 0-255
                stroke = 2
                end_cord_x = x + w
                end_cord_y = y + h
                cv2.rectangle(frame, (x, y), (end_cord_x, end_cord_y), color, stroke)

            if self.ret:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                self.bmp.CopyFromBuffer(frame)
                self.Refresh()

            if self.num_frames == 0:
                wx.PostEvent(self.window, ResultEvent(" data collection finish "))
                self.capture.release()
                self.Refresh()
                self.Hide()
                break





        n = 1
        wx.PostEvent(self.window, ResultEvent(" Packaging files ..."))

        with ZipFile(zipFileName, 'w') as zipObj:
            # Iterate over all the files in directory
            for folderName, subfolders, filenames in os.walk(dirName):
                for filename in filenames:
                    wx.PostEvent(self.window, ProgressEvent(len(filenames), n))
                    wx.Yield()
                    if filter(lambda name: '.jpg' in name,filename ):
                        # create complete filepath of file in directory
                        n += 1
                        filePath = os.path.join(folderName, filename)
                        # Add file to zip
                        zipObj.write(filePath)

        #self.status_bar.SetStatusText(" zipping file complete  ", 1)
        time.sleep(2)

        print('upload')

        ftp = ftplib.FTP()

        ftp.connect(preferences.host, preferences.port)

        file = open(zipFileName , 'rb')

        wx.PostEvent(self.window, ResultEvent(" Upload File ..."))

        uploadTracker = FtpUploadTracker(int(os.path.getsize(zipFileName)) , self.window)

        try:
            ftp.login(preferences.username, preferences.password)
            ftp.cwd('/Student/')
            ftp.storbinary('STOR ' + zipFileName, file , 1024 , uploadTracker.handle)
            file.close
            ftp.quit()

        except:
            pass
            #self.status_bar.SetStatusText(" failed to  connect ", 1)

        wx.PostEvent(self.window, ResultEvent(" "))
        wx.PostEvent(self.window, ProgressEvent(0,0))





