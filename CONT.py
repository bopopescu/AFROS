import cv2
from CONT_RegisterStudent import Add_Student
import preferences
from CONT_CreateClass import create_class
from CONT_TakeAttend import take_attendance
from VideoGenerator import video_stream
from Student import Student
from Class import classes

class Regis_stud :


    def __init__(self , windows , name, email, username, password, id_num , video_frame):

        self.windows = windows
        self.name = name
        self.email = email
        self.username = username
        self.password = password
        self.id_num = id_num
        self.video_frame = video_frame

        self.capture = cv2.VideoCapture(0)


    def check_duplicate(self):
        return Student.check_duplicate(preferences.mydb, self.id_num, self.username, self.name, self.email)

    def collect_data(self):
        self.location = self.id_num
        p = video_stream(self.video_frame, self.capture)
        p.start_record(self.windows, self.location)

    def Register(self):

        Add_Student(self.name, self.email, self.username, self.password, self.id_num, self.windows , self.capture , self.video_frame )

class create_classs:

    def __init__(self , day , subject , timestart , timeend , location , data , parent):

        self.day = day
        self.subject = subject
        self.timestart = timestart
        self.timeend = timeend
        self.location = location
        self.data = data
        self.parent = parent

        create_class(self.day , self.subject , self.timestart , self.timeend , self.location , self.data , self.parent)

class TakeAtt:

    def __init__(self, videoframe , window):

        self.cam = take_attendance(videoframe , window)

    def begin_take_att(self , subject , list_studnt ):

        self.cam.begin_take_attendance(subject , list_studnt)

    def sub(self):

        self.cam.submit()


class AlterClass:

    def __init__(self , subject_name , time_start , time_end , location , day):

        classes.modify_class_details(preferences.mydb , subject_name, time_start , time_end , location , day)

        pass

class Delete_Class:

    def __init__(self , subject_name):

        classes.delete_class(preferences.mydb , subject_name)








