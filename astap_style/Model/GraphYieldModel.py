import mysql.connector

from admin.Settings import Settings


class GraphYieldModel(object):

    def __init__(self):
        self.mysql_db = mysql.connector.connect(user='kostya05983', password='root',
                                                host=Settings.IP.value,
                                                database='farm')

    def get_pairs_by_year(self, year):
        cursor = self.mysql_db.cursor()
        query = """
        SELECT DISTINCT Culture.name, SUM(Crop_Rotation.amount_collected) FROM Crop_Rotation
LEFT JOIN Culture on Crop_Rotation.culture_id = Culture.id WHERE year =%s GROUP BY  Culture.name
        """ % year

        cursor.execute(query)
        result_list = []
        for (name, sum) in cursor:
            result_list.append((name, sum))
        return result_list

    def get_all_years(self):
        cursor = self.mysql_db.cursor()
        query = "select DISTINCT year from Crop_Rotation where amount_collected is NOT NULL"

        cursor.execute(query)

        result_list = []

        for year in cursor:
            result_list.append(year)
        return result_list

    def export(self, views):
        for i in range(len(views)):
            p = views[i].grab()
            p.save("graph%d.png" % i, "PNG")
