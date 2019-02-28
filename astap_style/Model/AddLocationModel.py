import mysql.connector

from admin.Settings import Settings


class AddLocationModel(object):
    def __init__(self):
        self.mysql_db = mysql.connector.connect(user='kostya05983', password='root',
                                                host=Settings.IP.value,
                                                database='farm')
        self.mysql_db.autocommit = True

    Insert_Culture = "insert into Location(width,height) values (%f,%f)"

    def insert_culture(self, width, height):
        cursor = self.mysql_db.cursor()
        cursor.execute(self.Insert_Culture % (float(width), float(height)))
