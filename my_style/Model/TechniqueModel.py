import mysql.connector

from admin.View.TechniqueElementView import TechniqueElementView


class TechniqueModel(object):

    def __init__(self):
        self.mysql_db = mysql.connector.connect(user='kostya05983', password='root',
                                                host='172.17.0.2',
                                                database='farm')

    def get_technique(self):
        cursor = self.mysql_db.cursor()
        query = "select id,name,path from farm.Technique where state=1"

        cursor.execute(query)

        result_list = []

        for (mysql_id, name, path) in cursor:
            result_list.append(TechniqueElementView(mysql_id, name, path))
        return result_list
