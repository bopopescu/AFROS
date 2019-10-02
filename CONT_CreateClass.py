from VideoGenerator import video_stream
import cv2
import threading
import os
import mysql.connector
import time
import ftplib
from zipfile import ZipFile
from Class import classes
import pickle
import numpy as np
import preferences
from PIL import Image
import wx
from Broadcast_Result import ProgressEvent
from Broadcast_Result import ResultEvent
from DownloadProgress import FtpDownloadTracker
from UploadProgress import FtpUploadTracker


class create_class:

    def __init__(self, day, subject, timestart, timeend, location, data , window):
        self.day = day
        self.subject = subject
        self.timestart = timestart
        self.timeend = timeend
        self.location = location
        self.data = data
        self.window = window

        # self.mydb = mysql.connector.connect(host='127.0.0.1 ', user='raihan', passwd='wuJWY3wHZmWwXAIs',
        #                                     database='project')

        self.recognizer = preferences.name+"_"+subject+".yml"
        self.pickle = preferences.name+"_"+subject+".pickle"
        self.foldername = preferences.name+"_"+subject


        self.ftp = ftplib.FTP()
        self.ftp.connect(preferences.host , preferences.port)

        self.ftp.login(preferences.username, preferences.password)

        self.create()

    def create(self):

        for x in self.data :

            wx.PostEvent(self.window, ResultEvent(" Downloading "+x+"'s dataset ... "))
            self.ftp.cwd('/Student/')
            filename = x+'.zip'
            localfile = open('images/' + filename, 'wb')
            totalsz = self.ftp.size(filename)
            p = FtpDownloadTracker(totalsz, localfile , self.window)
            self.ftp.retrbinary('RETR ' + filename, p.handle, 1024)

        self.ftp.quit()
        localfile.close()

        for foldername, subfolder, filesname in os.walk('images/'):
            for filename in filesname:
                if filename.endswith('.zip'):
                    with  ZipFile(os.path.join(foldername, filename), 'r') as zip:
                        zip.extractall(path='images/')


        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        image_dir = os.path.join(BASE_DIR, "images")

        face_cascade = cv2.CascadeClassifier('cascade/haarcascade_frontalface_default.xml')
        recognizer = cv2.face.LBPHFaceRecognizer_create()

        current_id = 0
        label_ids = {}
        y_labels = []
        x_train = []
        wx.PostEvent(self.window, ResultEvent(" Dataset Training ... "))

        for root, dirs, files in os.walk(image_dir):
            x = 0

            for file in files:
                x += 1
                wx.PostEvent(self.window, ProgressEvent(  len(files) , x))
                print(x)

                wx.Yield()
                if file.endswith("png") or file.endswith("jpg"):
                    path = os.path.join(root, file)
                    label = os.path.basename(root).replace(" ", "-").lower()
                    # print(label, path)
                    if not label in label_ids:
                        label_ids[label] = current_id
                        current_id += 1
                    id_ = label_ids[label]
                    # print(label_ids)
                    # y_labels.append(label) # some number
                    # x_train.append(path) # verify this image, turn into a NUMPY arrray, GRAY
                    pil_image = Image.open(path).convert("L")  # grayscale
                    size = (550, 550)
                    final_image = pil_image.resize(size, Image.ANTIALIAS)
                    image_array = np.array(final_image, "uint8")
                    # print(image_array)
                    faces = face_cascade.detectMultiScale(image_array, scaleFactor=1.5, minNeighbors=5)

                    for (x, y, w, h) in faces:
                        roi = image_array[y:y + h, x:x + w]
                        x_train.append(roi)
                        y_labels.append(id_)

        # print(y_labels)
        # print(x_train)

        with open("pickles/"+self.pickle, 'wb') as f:
            pickle.dump(label_ids, f)

        recognizer.train(x_train, np.array(y_labels))
        recognizer.save("recognizers/"+self.recognizer)
        time.sleep(5)

        ftp = ftplib.FTP()

        ftp.connect(preferences.host, preferences.port)
        wx.PostEvent(self.window, ResultEvent(" Upload YML File ... "))

        print("test")

        try:
            ftp.login(preferences.username, preferences.password)
            ftp.cwd('/Class/')

            print(self.recognizer)

            wx.PostEvent(self.window, ResultEvent(" Upload YML File ... "))
            file_yml = open("recognizers/" + self.recognizer, 'rb')
            stot = FtpUploadTracker(int(os.path.getsize("recognizers/" + self.recognizer)) , self.window)
            ftp.storbinary('STOR ' + self.recognizer , file_yml ,1024 , stot.handle )

            wx.PostEvent(self.window, ResultEvent(" Upload Pickle File ... "))
            file_pickle = open("pickles/" + self.pickle, 'rb')
            stoy = FtpUploadTracker(int(os.path.getsize("pickles/" + self.pickle)) , self.window)
            ftp.storbinary('STOR ' + self.pickle, file_pickle , 1024 , stoy.handle  )

            file_pickle.close()
            file_yml.close()

            ftp.quit()
        except:
            pass

        wx.PostEvent(self.window, ResultEvent(" "))
        wx.PostEvent(self.window, ProgressEvent(0,0))


