from Student import Student

from VideoGenerator import video_stream
import cv2
import threading
import os
import mysql.connector
import time
import ftplib
from zipfile import ZipFile
from Student import Student
from lecturer import Lecturer
from Class import classes
from Attendance import attendance
import pickle
import numpy as np
import preferences
from PIL import Image
from datetime import datetime



class add_lecturer:

    def __init__(self, name, username, password, id_num):
        self.name = name
        self.username = username
        self.password = password
        self.id_num = id_num

        self.mydb = mysql.connector.connect(host='127.0.0.1 ', user='raihan', passwd='wuJWY3wHZmWwXAIs',
                                            database='project')

    def check_duplicate(self):
        return Lecturer.check_duplicate(self.mydb, self.id_num, self.username, self.name, )

    def add(self):
        Lecturer.insert_lecturer(self.mydb, self.username, self.password, self.id_num, self.name)


class login:

    def __init__(self, username, password, type_user):

        self.username = username
        self.type_user = type_user
        self.mydb = mysql.connector.connect(host='127.0.0.1 ', user='raihan', passwd='wuJWY3wHZmWwXAIs',
                                            database='project')

        cursor = self.mydb.cursor()

        cursor.execute(
            "select username , password , id  from user where username='" + username + "' and  password='" + password + "'")
        self.res = cursor.fetchone()

        if self.type_user == 1 :
            cursor.execute("select Name from lecturer where id ='" + self.res[2] + "'")
            self.nameres = cursor.fetchone()
        else :
            cursor.execute("select Name from student where id ='" + self.res[2] + "'")
            self.nameres = cursor.fetchone()



    def result(self):

        if not self.res:
            return False
        else:

            if self.type_user == 0:

                if Student.check_legitimation(self.mydb, self.res[2]) == True:
                    return True
                else:
                    return False

            else:

                if Lecturer.check_legitimation(self.mydb, self.res[2]) == True:
                    return True
                else:
                    return False

    def save_to_sqlLite(self, bool):

        preferences.name = str(self.nameres[0])
        preferences.id = str(self.res[2])

        print (preferences.name)

class alter_att :

    def __init__(self ,  subject , time , list ):

        temp = []

        for x in list :
            temp.append(( "`"+str(x[0])+"`='"+x[1]+"'" ))


        attendance.alter_record(preferences.mydb , preferences.name+"_"+subject+"_att" , time , temp)























