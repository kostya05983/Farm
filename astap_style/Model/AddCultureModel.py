from admin.Settings import Settings
import mysql.connector


class AddCultureModel(object):
    def __init__(self):
        self.mysql_db = mysql.connector.connect(user='kostya05983', password='root',
                                                host=Settings.IP.value,
                                                database='farm')
        self.mysql_db.autocommit = True

    Insert_Culture = "insert into Culture(name,amount,price) values ('%s',%d,%d)"

    def insert_culture(self, name, amount, price):
        cursor = self.mysql_db.cursor()
        cursor.execute(self.Insert_Culture % (name, int(amount), int(price)))
