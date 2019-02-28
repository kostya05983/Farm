import mysql.connector


class LoginModel(object):

    def __init__(self):
        self.mysql_db = mysql.connector.connect(user='kostya05983', password='root',
                                                host='172.17.0.2',
                                                database='farm')

    Select_Password_Query = """
    select AES_DECRYPT(password,'%s') from Users where login = '%s'
    """

    def check(self, login, password):
        cursor = self.mysql_db.cursor()
        cursor.execute(self.Select_Password_Query % (login, login))

        result = cursor.fetchall()

        if result[0][0] == password:
            return 1
        return -1
