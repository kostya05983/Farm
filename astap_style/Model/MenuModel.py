import mysql

from admin.Settings import Settings


class EmptyViewModel(object):

    def __init__(self):
        super(EmptyViewModel, self).__init__()
        self.mysql_db = mysql.connector.connect(user='kostya05983', password='root',
                                                host=Settings.IP.value,
                                                database='farm')
        self.mysql_db.autocommit = True

