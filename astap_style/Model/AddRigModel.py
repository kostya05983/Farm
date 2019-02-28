import mysql.connector

from admin.Settings import Settings


class AddRigModel(object):
    def __init__(self):
        self.mysql_db = mysql.connector.connect(user='kostya05983', password='root',
                                                host=Settings.IP.value,
                                                database='farm')

    Techniquue_Query = """
        SELECT id,name from Technique where state = 1
    """

    Location_Query = """
    select id,width,height from Location
    """

    Insert_Query = """
    insert into Rig (time_work,technique_id,location_id,user_id,date) values(%d,%d,%d,%d,'%s')
    """

    Select_Users = """
    select Users.id, login
from Users
       left outer join Rig R2 on Users.id = R2.user_id
where R2.user_id is NULL and
  (select Count(role_id) from Roles where user_id = Users.id) = 1
  and (select role_id from Roles where user_id = Users.id) = 0
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

    def insert_to_rig(self, technique_id, location_id, user_id, time, date):
        cursor = self.mysql_db.cursor()
        cursor.execute(self.Insert_Query % (int(time), technique_id, location_id, user_id, date))
        self.mysql_db.commit()

    def get_users(self):
        cursor = self.mysql_db.cursor()
        cursor.execute(self.Select_Users)
        result = []
        for (id, login) in cursor:
            result.append([id, login])
        return result
