import re

import mysql.connector


class AddRigModel(object):
    def __init__(self):
        self.mysql_db = mysql.connector.connect(user='kostya05983', password='root',
                                                host='172.17.0.2',
                                                database='farm')

    Techniquue_Query = """
        SELECT id,name from Technique where state = 0
    """

    Location_Query = """
    select id,width,height from Location
    """

    Insert_Query = """
    insert into Rig (time_work,technique_id,location_id) values(%d,%d,%d)
    """

    def get_technique(self):
        cursor = self.mysql_db.cursor()
        cursor.execute(self.Techniquue_Query)

        result_list = []
        for (id, name) in cursor:
            result_list.append((id, name))
        return result_list

    def get_locations(self):
        cursor = self.mysql_db.cursor()
        cursor.execute(self.Location_Query)

        result_list = []
        for (id, width, height) in cursor:
            result_list.append((id, "%s x %s" % (str(width), str(height))))
        return result_list

    def validate_time(self, time):
        if not time:
            return -1
        result = re.match('\d*', time)
        if result is None:
            return -1
        if int(time) <= 0:
            return -1
        return 1

    def insert_to_rig(self, location_id, technique_id, time):
        cursor = self.mysql_db.cursor()
        cursor.execute(self.Insert_Query % (int(time), technique_id, location_id))
        self.mysql_db.commit()
