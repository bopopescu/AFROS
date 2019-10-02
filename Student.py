
import cv2
import time
import os
import ftplib
from zipfile import ZipFile
import preferences



class Student :


    def check_legitimation(mydb , id_num ):
        cursor = mydb.cursor()


        cursor.execute("select ID from student where ID='" + id_num + "'")

        res2 = cursor.fetchone()

        if not res2:
            return False
        else:
            return True


    def check_duplicate(mydb, id_num, username, name, email):
        cursor = mydb.cursor()

        cursor.execute(
            "select ID , username from user where ID='" + id_num + "' or username='" + username + "'")

        res = cursor.fetchone()

        cursor.execute("select Name,Email from student where Name='" + name + "' or Email='" + email + "'")

        res2 = cursor.fetchone()

        if not res and not res2:
            return True
        else:
            return False


    def insert_student( mydb , username ,password ,id_num , name , email , facial_location):

        cursor = mydb.cursor()

        cursor.execute(
            "insert into user (username , password , ID) values ('" + username + "','" + password + "','" +id_num + "')")

        mydb.commit()

        cursor.execute(
            "insert into student (Name , Email , ID , facial_path ) values ('" + name + "' , '" + email + "' , '" + id_num + "' , '" + facial_location + "' )")

        mydb.commit()

    def get_student(mydb):

        cursor = mydb.cursor()

        cursor.execute(
            "select Name , ID from student ")

        res = cursor.fetchall()

        return res

    def retrive_studentName(student_id):

        cursor =  preferences.mydb.cursor()

        cursor.execute("select Name from student where ID ='"+str(student_id)+"'")

        res = cursor.fetchone()

        return res

    def search_student_likely (string_like):

        cursor = preferences.mydb.cursor()

        cursor.execute("select Name , ID  from student where Name like '"+string_like+"%' or ID like '"+string_like+"%' ;")

        res = cursor.fetchall()

        return res

