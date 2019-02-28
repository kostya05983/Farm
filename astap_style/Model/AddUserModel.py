from admin.Settings import Settings
import mysql.connector

from admin.View.Roles import Roles


class AddUserModel(object):
    Insert_User_Query = "insert into Users(login,password) values('%s',AES_ENCRYPT('%s','%s'));"
    Select_User_id = "select id from Users where login = '%s'"
    Insert_Role = "insert into Roles(user_id,role_id) values(%d,%d)"

    def __init__(self):
        self.mysql_db = mysql.connector.connect(user='kostya05983', password='root',
                                                host=Settings.IP.value,
                                                database='farm')
        self.mysql_db.autocommit = True

    def insert_to_users(self, login, password, role):
        cursor = self.mysql_db.cursor()
        cursor.execute(self.Insert_User_Query % (login, password, login))
        cursor.execute(self.Select_User_id % login)

        user_id = cursor.fetchall()
        for i in range(len(role)):
            cursor.execute(self.Insert_Role % (user_id[0][0], role[i]))

    def roles(self):
        return [([1], Roles.Lawyer.value),
                ([2], Roles.Technical_engineer.value),
                ([0, 3], Roles.Technological_engineer.value),
                ([0, 1, 2, 3], Roles.Owner.value),
                ([0], Roles.Tractor_Driver.value)]
