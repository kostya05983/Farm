import mysql.connector

from admin.View.TreatyElementView import TreatyElementView


class TreatyModel(object):
    def __init__(self):
        self.mysql_db = mysql.connector.connect(user='kostya05983', password='root',
                                                host='172.17.0.2',
                                                database='farm')

    def get_treaties(self):
        cursor = self.mysql_db.cursor()
        query = """
        SELECT Treaty.delivery_date,Treaty.delivery_condition,Treaty.payment_condition, Culture.name,
        O.name, O.requisites, O.email,O.head,O.post_address,O.legal_address,O.site FROM Treaty
         LEFT JOIN Culture ON culture_id=Culture.id LEFT JOIN Organization  O ON organization_id=O.id
        """
        cursor.execute(query)

        result_list = []

        for (
                delivery_date, delivery_condition, payment_condition, culture_name, organization_name, requisites,
                email, head,
                post_address, legal_address, site) in cursor:
            result_list.append(
                TreatyElementView(delivery_date, delivery_condition, payment_condition, culture_name, organization_name,
                                  requisites, email, head, post_address, legal_address, site))
        return result_list
