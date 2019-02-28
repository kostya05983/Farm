import mysql.connector

from admin.Settings import Settings


class AddTreatyModel(object):

    def __init__(self):
        self.mysql_db = mysql.connector.connect(user='kostya05983', password='root',
                                                host=Settings.IP.value,
                                                database='farm')
        self.mysql_db.autocommit = True

    Insert_Treaty_Query = """insert into Treaty(delivery_date, delivery_condition, payment_condition,
     culture_id, organization_id) VALUES ('%s','%s','%s',%d,
     (select id from Organization ORDER BY id DESC limit 1))"""

    Insert_Organization_Query = """insert into Organization(name,requisites,email,head,post_address,legal_address,site)
     values('%s','%s','%s','%s','%s','%s','%s')"""

    Insert_Phone_Number_Query = """insert into Phone_Numbers(number,organization_id) values('%s',(select organization_id from Treaty ORDER BY id DESC limit 1))"""

    Get_Cultures_Query = """
       select id,name from Culture
       """

    Update_amount_Query = """
    UPDATE Culture SET amount = amount - %d where id=%d
    """

    def insert_to_treaty(self, delivery_date, delivery_condition,
                         payment_condition, culture_id, amount, organization_name, requisites,
                         email, head, post_address, legal_address, site, phone_number):
        cursor = self.mysql_db.cursor()
        cursor.execute(self.Update_amount_Query % (int(amount), int(culture_id)))
        cursor.execute(self.Insert_Organization_Query
                       % (organization_name, requisites, email, head, post_address, legal_address, site))
        cursor.execute(
            self.Insert_Treaty_Query % (delivery_date, delivery_condition, payment_condition, int(culture_id)))
        cursor.execute(self.Insert_Phone_Number_Query % (phone_number))

    def get_cultures(self):
        cursor = self.mysql_db.cursor()

        cursor.execute(self.Get_Cultures_Query)

        result_list = []

        for (id, name) in cursor:
            result_list.append((id, name))

        return result_list
