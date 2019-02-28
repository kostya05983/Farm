import mysql.connector

from admin.Settings import Settings


class AddTechniqueModel(object):

    def __init__(self):
        self.mysql_db = mysql.connector.connect(user='kostya05983', password='root',
                                                host=Settings.IP.value,
                                                database='farm')
        self.mysql_db.autocommit = True

    Insert_Technique = """insert into Technique(name,production_date,capital_date,next_repair,state) values('%s','%s','%s','%s',%d)"""

    def insert_to_technique(self, name, production_date, capital_date, next_repair, state):
        cursor = self.mysql_db.cursor()

        if state == "Сломана":
            cursor.execute(self.Insert_Technique % (name, production_date, capital_date, next_repair, 0))
        else:
            cursor.execute(self.Insert_Technique % (name, production_date, capital_date, next_repair, 1))

        self.mysql_db.commit()

    def data_state(self):
        return [(0, "В работе"), (1, "Сломана")]
