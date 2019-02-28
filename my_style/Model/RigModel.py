import mysql.connector

from admin.View.RigElementView import RigElementView


class RigModel(object):
    current_data = None

    Select_Rigs = """
    SELECT time_work,T.name,T.production_date,T.capital_date,T.next_repair,L.width,L.height
         from Rig left join  Technique T on technique_id=T.id left join Location L on location_id=L.id
    """

    def update_rigs(self):
        mysql_db = mysql.connector.connect(user='kostya05983', password='root',
                                           host='172.17.0.2',
                                           database='farm')
        cursor = mysql_db.cursor()

        cursor.execute(self.Select_Rigs)
        result_list = []

        for (time_work, name, production_date, capital_date, next_repait, width, length) in cursor:
            result_list.append(
                RigElementView(time_work, name, production_date, capital_date, next_repait, width, length))
        self.current_data = result_list
        mysql_db.close()

    def get_rigs(self):
        return self.current_data
