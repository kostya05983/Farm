import mysql.connector

from admin.Settings import Settings


class LoginModel(object):

    def __init__(self):
        self.mysql_db = mysql.connector.connect(user='kostya05983', password='root',
                                                host=Settings.IP.value,
                                                database='farm')
        self.mysql_db.autocommit = True

    Select_Password_Query = """
    select AES_DECRYPT(password,'%s') from Users where login = '%s'
    """

    Select_Roles_Query = """
    Select role_id from Roles where user_id = (select id from Users where login='%s')
    """

    def check(self, login, password):
        cursor = self.mysql_db.cursor()
        cursor.execute(self.Select_Password_Query % (login, login))

        result = cursor.fetchall()

        if result[0][0] == password:
            return 1
        return -1

    def selectRoles(self, login):
        cursor = self.mysql_db.cursor()
        cursor.execute(self.Select_Roles_Query % (login))

        result = []
        for (role_id) in cursor:
            result.append(role_id[0])
        return result
