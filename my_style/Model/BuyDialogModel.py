import re

import mysql.connector


class BuyDialogModel(object):
    def __init__(self):
        self.mysql_db = mysql.connector.connect(user='kostya05983', password='root',
                                                host='172.17.0.2',
                                                database='farm')

    Insert_Query = """insert into Cart(good_id,amount,session_id) values(%d,%d,'%s')
    """

    def insert_to_db(self, good_id, amount, session_id):
        cursor = self.mysql_db.cursor()
        cursor.execute(self.Insert_Query % (int(good_id), int(amount), str(session_id)))
        self.mysql_db.commit()

    def validate_amount(self, amount):
        if not amount:
            return -1
        result = re.fullmatch('\d*', amount)

        if not result:
            return -1
        if int(amount) <= 0:
            return -1
        return 1
