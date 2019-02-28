import mysql.connector
import re

from admin.View.CropRotationView import CropRotationView


class PlanCropRotationModel(object):
    current_data = None
    Query = """select Location.height,Location.width,Culture.name,Crop_Rotation.amount_of_seed,Crop_Rotation.amount_collected from Crop_Rotation
                    LEFT JOIN Location On Location.id=Crop_Rotation.location_id
                        LEFT JOIN Culture On Culture.id=Crop_Rotation.culture_id
                            where year = %s
    """

    def __init__(self):
        self.mysql_db = mysql.connector.connect(user='kostya05983', password='root',
                                                host='172.17.0.2',
                                                database='farm')

    def validate_number(self, year):
        if not year:
            return -1
        result = re.match('\d*', year)
        if result is None:
            return -1
        if int(year) <= 0:
            return -1
        return 1

    def get_crop_rotation(self):
        return self.current_data

    def update(self, year):
        cursor = self.mysql_db.cursor()
        query = self.Query % year
        cursor.execute(query)

        result_list = []
        for (length, width, name, amount_of_seed, amount_collected) in cursor:
            if amount_collected is None:
                result_list.append(CropRotationView(length, width, name, amount_of_seed, "Не собрано"))
            else:
                result_list.append(CropRotationView(length, width, name, amount_of_seed, amount_collected))
        self.current_data = result_list
