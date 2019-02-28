import mysql.connector

from admin.View.ProductView import ProductView


class ShopModel(object):

    def __init__(self):
        self.mysql_db = mysql.connector.connect(user='kostya05983', password='root',
                                                host='172.17.0.2',
                                                database='farm')
        self.mysql_db.autocommit = True

    Select_Goods_Query = """
    select Cart.id,Culture.name,Cart.amount,Culture.price from Cart left join Culture on Cart.good_id=Culture.id where session_id='%s'
    """

    Get_Sum_Query = """
    Select Sum(Cart.amount*price) from Cart left Join Culture C on Cart.good_id = C.id where session_id='%s'
    """

    Select_Products = """ select id,name,path,price from Culture where amount>0 and type=%d
    """

    def get_products(self, type, session_id):
        cursor = self.mysql_db.cursor()

        cursor.execute(self.Select_Products % type)

        result_list = []

        for (mysql_id, name, path, price) in cursor:
            result_list.append(ProductView(mysql_id, name, path, price, session_id))

        return result_list

    def get_goods(self, session_id):
        cursor = self.mysql_db.cursor()
        cursor.execute(self.Select_Goods_Query % session_id)

        result_list = []

        for (id, name, amount, price) in cursor:
            result_list.append((id,name, amount, price * amount))
        return result_list

    def get_sum(self, session_id):
        cursor = self.mysql_db.cursor()
        cursor.execute(self.Get_Sum_Query % session_id)

        for sum in cursor:
            return sum

    def delete_from_cart(self, id):
        cursor = self.mysql_db.cursor()
        cursor.execute("delete from Cart where id = %d" % id)
