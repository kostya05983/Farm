import datetime
import re

import mysql.connector
from mysql.connector import Date


class DialogTreatyModel(object):

    def __init__(self):
        self.mysql_db = mysql.connector.connect(user='kostya05983', password='root',
                                                host='172.17.0.2',
                                                database='farm')
        self.mysql_db.autocommit = True

    def valid_phone_number(self, phone):
        result = re.fullmatch('^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$', phone)

        if not result:
            return -1
        return 1

    Insert_Organization_Query = """
    insert into Organization(name,requisites,email,head,post_address,legal_address,site) values('%s','%s','%s','%s','%s','%s','%s')
    """

    Insert_Phone_Number = """
        insert into Phone_Number(number,organzization_id) values('%s', %d)
    """

    Insert_Treaty = """insert into Treaty(delivery_date,delivery_condition,payment_condition,culture_id,organization_id) values('%s','%s','%s',%d,%d)
    """

    Select_Good_id = """select good_id from Cart where session_id='%s'"""

    Select_last_id = """SELECT LAST_INSERT_ID()"""
    Delete_all_records_by_Session = """delete from Cart where session_id='%s'"""

    def insert_treaty(self, delivery_condition, payment_condition, name,
                      requisites, email, head, post_address, legal_address, site,
                      phone_number, session_id):
        cursor = self.mysql_db.cursor()
        cursor.execute(
            self.Insert_Organization_Query % (name, requisites, email,
                                              head, post_address, legal_address, site))
        cursor.execute(self.Select_last_id)
        organization_id = cursor.fetchall().pop()

        cursor.execute(self.Insert_Phone_Number % (phone_number, organization_id[0]))

        cursor.execute(self.Select_Good_id % session_id)
        goods = cursor.fetchall()

        for good_id in goods:
            cursor.execute(
                self.Insert_Treaty % (
                    datetime.date(2018, 1, 2), delivery_condition, payment_condition, good_id[0], organization_id[0]))

        print("")
        cursor.execute(self.Delete_all_records_by_Session % session_id)
