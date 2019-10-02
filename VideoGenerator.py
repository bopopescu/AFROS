import cv2
import wx
import pickle
from Student import Student
from datetime import datetime
import preferences
from Broadcast_Result import ResultEvent
from Broadcast_Result import ProgressEvent
import os

class video_stream(wx.Panel):


    def __init__(self, parent , cap):

        wx.Panel.__init__(self, parent, wx.ID_ANY, (0, 0), (640, 480))


        self.parent = parent
        self.capture = cap

        ret, frame = self.capture.read()

        height, width = frame.shape[:2]

        parent.SetSize((width, height))

        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        self.bmp = wx.Bitmap.FromBuffer(width, height, frame)

        self.timer = wx.Timer(self)
        self.timer.Start(1000. / 30)
        self.face_cascade = cv2.CascadeClassifier('cascade/haarcascade_frontalface_default.xml')

        self.flag = 0
        self.flag_r = 0
        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.run()


    def run(self):

        self.Show()
        self.Bind(wx.EVT_TIMER, self.NextFrame)


    def OnPaint(self, evt):
        dc = wx.BufferedPaintDC(self)
        dc.DrawBitmap(self.bmp, 0, 0)

    def close_video(self):

        self.timer.Stop()
        self.capture.release()
        self.Refresh()
        self.Hide()

    def start_face_recognitiona(self , attendance_id , list ):

        self.list = list
        self.id = attendance_id
        self.flag = 1

        self.recognizer = cv2.face.LBPHFaceRecognizer_create()
        self.recognizer.read("./recognizers/"+self.id+".yml")

        self.labels = {"person_name": 1}
        with open("pickles/"+self.id+".pickle", 'rb') as f:
            og_labels = pickle.load(f)
            self.labels = {v: k for k, v in og_labels.items()}
        self.list_student = []
        self.list_student_complete = []



    def submit_data (self):

        return self.list_student_complete

    def start_record(self , window , location):

        os.makedirs(location)

        self.location = location
        self.window = window
        self.num_frames = preferences.num_frames
        self.n = 0
        self.flag_r = 1

    def return_cmplt_record(self):

        self.x = 0
        return self.x


    def NextFrame(self , event):
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

            # recognize? deep learned model predict keras tensorflow pytorch scikit learn

            if self.flag == 1:
                id_, conf = self.recognizer.predict(roi_gray)
                if conf >= 80 and conf <= 100:
                    # print(5: #id_)

                    if self.labels[id_] in self.list_student:
                        pass
                    else:
                        now = datetime.now()
                        print(self.labels[id_])
                        t = (Student.retrive_studentName(self.labels[id_])[0], self.labels[id_],
                             now.strftime("%H:%M:%S"))
                        print(t)
                        self.list.AppendItem(t)
                        self.list.Refresh()
                        self.list_student.append(self.labels[id_])
                        self.list_student_complete.append(t)
                        # self.list.

                    font = cv2.FONT_HERSHEY_SIMPLEX
                    name = self.labels[id_]
                    color = (255, 255, 255)
                    stroke = 2
                    cv2.putText(frame, name, (x, y), font, 1, color, stroke, cv2.LINE_AA)

            if self.flag_r == 1:
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

                self.x = 0

                if self.num_frames == 0:
                    self.flag_r = 0
                    wx.PostEvent(self.window, ResultEvent(" data collection finish "))
                    self.x = 1
                    self.close_video()

            color = (255, 0, 0)  # BGR 0-255
            stroke = 2
            end_cord_x = x + w
            end_cord_y = y + h
            cv2.rectangle(frame, (x, y), (end_cord_x, end_cord_y), color, stroke)

        if self.ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            self.bmp.CopyFromBuffer(frame)
            self.Refresh()



















