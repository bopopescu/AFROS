import sqlite3
from Attendance import attendance
import preferences




class classes :

    def insert_class(mydb, day , subject , timestart , timeend , location , data , recognizerFile ):

        cursor = mydb.cursor()



        timstrt = str(timestart[0])+":"+str(timestart[1])+":"+str(timestart[2])
        timend = str(timeend[0])+":"+str(timeend[1])+":"+str(timeend[2])

        print (timstrt , timend)


        table_id = preferences.name+"_"+subject

        print (table_id)


        cursor.execute(" insert into classes (ID,lecturer_name,subject_name,days,time_start,time_end,attendance_id_table , location , recognizerfile) values ('"+preferences.id+"','"+preferences.name+"','"+subject+"','"+day+"','"+timstrt +"','"+ timend+"','"+preferences.name+"_"+subject+"','"+location+"','"+recognizerFile+"')")

        mydb.commit()

        cursor.execute(" create table "+table_id+"( name varchar(50) , id varchar(10)  , foreign key (id) references student(ID) );")

        mydb.commit()

        attendance.create_class_table(mydb , table_id , data )

        for x in data :
            cursor.execute(" insert into " + table_id + " (name , id ) select Name , ID from student where ID ='"+x+"'")
            mydb.commit()
            cursor.execute(" insert into list_of_enrolled_student (student_id , attendance_id ) values ('"+x+"' , '"+ table_id +"')")
            mydb.commit()


    def select_classes(mydb):

        cursor = mydb.cursor()

        cursor.execute(" select subject_name , attendance_id_table from classes where ID='"+str(preferences.id)+"'")

        res = cursor.fetchall()

        return res

    def retrive_list_of_student (mydb , subjectname):

        cursor = mydb.cursor()

        cursor.execute(" select name , id  from "+preferences.name+"_"+subjectname)

        res = cursor.fetchall()

        return res

    def retrive_classes_based_lecturer (mybd):

        cursor = mybd.cursor()

        cursor.execute(" select subject_name from classes where ID ='"+str(preferences.id)+"'" )

        res = cursor.fetchall()

        return res

    def retrive_classDetails_based_subject(mybd , subject_name):

        cursor = mybd.cursor()

        cursor.execute(" select days , time_start , time_end , location from classes where ID='" + str(preferences.id) + "' and subject_name='"+subject_name+"'")

        res = cursor.fetchall()

        return res

    def modify_class_details (mydb , subject_name , time_start , time_end , location , day):


        timstrt = str(time_start[0]) + ":" + str(time_start[1]) + ":" + str(time_start[2])
        timend = str(time_end[0]) + ":" + str(time_end[1]) + ":" + str(time_end[2])

        cursor = mydb.cursor()
        cursor.execute(" update classes set time_start = '"+timstrt+"' ,time_end = '"+timend+"' , location = '"+location+"' , days = '"+day+"'  where subject_name='"+subject_name+"' and ID='" + preferences.id + "'" )
        mydb.commit()

    def delete_class (mydb , subject_name):
        cursor = mydb.cursor()

        cursor.execute(
            " delete from classes where subject_name='" + subject_name + "' and ID='" + preferences.id + "'")
        mydb.commit()

















