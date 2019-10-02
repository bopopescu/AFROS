class Lecturer:

    def check_legitimation(mydb, id_num):
        cursor = mydb.cursor()

        cursor.execute("select ID from lecturer where ID='" + id_num + "'")

        res2 = cursor.fetchone()

        if not res2:
            return False
        else:
            return True

    def check_duplicate(mydb, id_num, username, name):
        cursor = mydb.cursor()

        cursor.execute(
            "select ID , username from user where ID='" + id_num + "' or username='" + username + "'")

        res = cursor.fetchone()

        cursor.execute("select Name,ID from lecturer where Name='" + name + "'")

        res2 = cursor.fetchone()

        if not res and not res2:
            return True
        else:
            return False

    def insert_lecturer(mydb, username, password, id_num, name):

        cursor = mydb.cursor()

        cursor.execute(
            "insert into user (username , password , ID) values ('" + username + "','" + password + "','" + id_num + "')")

        mydb.commit()

        cursor.execute(
            "insert into lecturer (Name , ID ) values ('" + name + "' , '" + id_num + "' )")

        mydb.commit()
