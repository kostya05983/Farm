import re

import mysql.connector


class AddCropRotationModel(object):
    def __init__(self):
        self.mysql_db = mysql.connector.connect(user='kostya05983', password='root',
                                                host='172.17.0.2',
                                                database='farm')

    Get_Cultures_Query = """
    select id,name from Culture
    """

    Get_locations_Query = """
    select id,width,height from Location"""

    Insert_Crop_Rotation_Query = """
    insert into Crop_Rotation(location_id,culture_id,amount_of_seed,year) values(%d,%d,%d,%d)
    """

    def validate_number(self, year):
        if not year:
            return -1
        result = re.match('\d*', year)

        if result is None:
            return -1
        return 1

    def get_cultures(self):
        cursor = self.mysql_db.cursor()

        cursor.execute(self.Get_Cultures_Query)

        result_list = []

        for (id, name) in cursor:
            result_list.append((id, name))

        return result_list

    def get_locations(self):
        cursor = self.mysql_db.cursor()

        cursor.execute(self.Get_locations_Query)

        result_list = []

        for (id, width, height) in cursor:
            result_list.append((id, "%sx%s" % (str(width), str(height))))
        return result_list

    def insert_crop_rotation(self, location_id, culture_id, amount_of_seed, year):
        cursor = self.mysql_db.cursor()
        cursor.execute(self.Insert_Crop_Rotation_Query % (location_id, culture_id, amount_of_seed, year))
        self.mysql_db.commit()
