import preferences
from datetime import datetime



class attendance :

    def create_class_table (mydb , attendance_id , list_of_student ):

        cursor = mydb.cursor()

        cursor.execute(" create table "+attendance_id+"_att  ( timestamp  TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP );")

        mydb.commit()

        for x in list_of_student :
            cursor.execute(" alter table "+attendance_id+"_att add `"+x+"` varchar(10) not null default 'ABSENT';")
            mydb.commit()

    def submit_attendance (mydb , table ,  list , attendance_id):


        table_id = attendance_id+table
        id = []
        value = ''

        for x in list:
            id.append(x[1].strip())
            value += ', \'PRESENT\''

        row = "`"+"`,`".join(id)+"`"

        print(row)

        cursor = mydb.cursor()

        t = " insert into  `"+table+"_att`   ( `timestamp` ,  "+row+" ) values ( CURRENT_TIMESTAMP  "+value+")"

        print (t)

        cursor.execute(t)


        mydb.commit()

        #cursor.execute(" create table "+table_id+"  (  name varchar(50) , id  varchar(30) ,time varchar(30) , foreign key (id) references student(ID));")

        #mydb.commit()

        #for x in list :

            #cursor.execute(" insert into "+table_id+" ( name , id , time ) values ( '"+x[0]+"','"+x[1]+"','"+x[2]+"')")
           # mydb.commit()

    def retrive_attendance_timestamp (mydb, attendanceid):

        cursor = mydb.cursor()

        cursor.execute(" select timestamp  from  "+attendanceid+"_"+"att"  )

        res = cursor.fetchall()

        print(res)

        return res

    def retrive_attendace_list_based_timestamp(mydb, attendance_id , timestamp):

        cursor = mydb.cursor()

        print(attendance_id.lower())

        cursor.execute(" select * from "+attendance_id.lower()+"_"+"att where timestamp='"+timestamp+"'")

        res = cursor.fetchall()

        return res

    def alter_record (mydb , attendance_id , timestamp , list):



        print (" changed :"+str(list))

        cursor = mydb.cursor()

        col = " , ".join(list)

        temp = " update "+attendance_id.lower()+" set  "+col+"   where timestamp ='"+timestamp+"';"

        print(temp)

        cursor.execute(temp)

        mydb.commit()


    def viewAttnd_as_Stud(mydb , id ):


        temp = []

        cursor = mydb.cursor()

        cursor.execute(" select attendance_id from list_of_enrolled_student where student_id='"+str(id)+"' ")

        res = cursor.fetchall()[0]

        for x in res :

            print(x)

            cursor.execute("select count("+str(id)+") from "+x.lower()+"_att"+" where  `"+str(id)+"`='ABSENT' ")
            y = cursor.fetchone()[0]

            cursor.execute("select count("+str(id)+") from "+x.lower()+"_att"+" where  `"+str(id)+"`='MEDICAL' ")
            n = cursor.fetchone()[0]

            p = x.split("_")

            tupl = (p[0] , p[1] , y , n)

            temp.append(tupl)


        return temp














