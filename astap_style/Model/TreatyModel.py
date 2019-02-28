import operator
# import os
import os
import re
from threading import Thread

import mysql.connector
import xlwt
from PyQt5.QtCore import QAbstractTableModel, QModelIndex, Qt, QTimer
from PyQt5.QtGui import QBrush, QColor
from PyQt5.QtWidgets import QProgressDialog, QFileDialog, qApp

from admin.Settings import Settings
from admin.View.ErrorDialogView import ErrorDialogView


class TreatyModel(QAbstractTableModel):
    current_list = []
    current_indexes_list = []
    header = ["Дата доставки", "Условие доставки",
              "Условие оплаты", "Название культуры","Цена в рублях за единицу",
              "Имя организации", "Реквизиты", "Email",
              "Глава", "Почтовый адресс", "Юридический адресс",
              "Сайт", "Телефонный номер"]
    columns_treaty = ["delivery_date", "delivery_condition", "payment_condition", "culture_id", "organization_id"]
    columns_organization = ["name", "requisites", "email", "head", "post_address", "legal_address", "site"]

    SELECT_QUERY = """
    SELECT Treaty.id, Treaty.delivery_date,Treaty.delivery_condition,Treaty.payment_condition, Culture.name,Culture.price,
        O.name, O.requisites, O.email,O.head,O.post_address,O.legal_address,O.site, P.number FROM Treaty
         LEFT JOIN Culture ON culture_id=Culture.id LEFT JOIN Organization  O ON organization_id=O.id Left Join Phone_Numbers P ON O.id = P.organization_id
    """

    def __init__(self, view):
        super().__init__()
        self.view = view
        self.mysql_db = mysql.connector.connect(user='kostya05983', password='root',
                                                host=Settings.IP.value,
                                                database='farm')
        self.mysql_db.autocommit = True
        self.get_treaties()

    def get_treaties(self):
        cursor = self.mysql_db.cursor()
        cursor.execute(self.SELECT_QUERY)

        self.current_list = []
        self.current_indexes_list = []

        for (id, delivery_date, delivery_condition, payment_condition, culture_name,culture_price, organization_name, requisites,
             email, head,
             post_address, legal_address, site, number) in cursor:
            self.current_list.append(
                [delivery_date, delivery_condition, payment_condition, culture_name,culture_price, organization_name,
                 requisites, email, head, post_address, legal_address, site, number])
            self.current_indexes_list.append(id)

    def rowCount(self, parent):
        return len(self.current_list)

    def columnCount(self, parent):
        if len(self.current_indexes_list) == 0:
            return 0
        return len(self.current_list[0])

    def headerData(self, section: int, orientation: Qt.Orientation, role: int = ...):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self.header[section]

    def data(self, index: QModelIndex, role: int = ...):
        value = str(self.current_list[index.row()][index.column()])
        if role == Qt.EditRole:
            return value
        elif role == Qt.DisplayRole:
            return value
        elif role == Qt.BackgroundColorRole:
            return QBrush(QColor("#3b3b3d"))

    def sort(self, column: int, order: Qt.SortOrder = ...):
        self.current_list = sorted(self.current_list, key=operator.itemgetter(column))
        if order == Qt.DescendingOrder:
            self.current_list.reverse()

    def flags(self, index):
        fl = super(self.__class__, self).flags(index)
        fl |= Qt.ItemIsEditable
        fl |= Qt.ItemIsSelectable
        fl |= Qt.ItemIsEnabled
        fl |= Qt.ItemIsDragEnabled
        fl |= Qt.ItemIsDropEnabled
        return fl

    def setData(self, index, value, role=Qt.EditRole):
        if index.isValid():
            row = index.row()
            col = index.column()
            if self.checkColumnValue(col, value):
                self.updateInTable(self.current_indexes_list[row], value, col)
                self.current_list[row][col] = str(value)
                self.dataChanged.emit(index, index, (Qt.DisplayRole,))
                return True
            else:
                return False
        return False

    def checkColumnValue(self, index_column, value):
        if not value:
            self.showMessage("Нельзя вводить пустоту")
            return False
        if index_column == 0:
            if not re.fullmatch("([12]\d{3}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01]))", value):
                self.showMessage("Неверный формат даты")
                return False
        elif index_column == 6:
            if not re.fullmatch("\d*", value):
                self.showMessage("Реквизит должен состоять из цифр")
                return False
        elif index_column == 7:
            if not re.fullmatch(
                    "^[-a-z0-9!#$%&'*+/=?^_`{|}~]+(?:\.[-a-z0-9!#$%&'*+/=?^_`{|}~]+)" \
                    + "*@(?:[a-z0-9]([-a-z0-9]{0,61}[a-z0-9])?\.)" \
                    + "*(?:aero|arpa|asia|biz|cat|com|coop|edu|gov|info|int|jobs|mil|mobi" \
                    + "|museum|name|net|org|pro|tel|travel|[a-z][a-z])$", value):
                self.showMessage("Неверный формат email")
                return False
        elif index_column == 12:
            if not re.fullmatch("^((\+7|7|8)+([0-9]){10})$", value):
                self.showMessage("Неверный формат номера")
                return False
        return True

    def showMessage(self, message):
        error_dialog = ErrorDialogView(message)
        error_dialog.setModal(True)
        error_dialog.setWindowTitle("Ошибка")
        error_dialog.exec_()

    def updateInTable(self, id, value, index_column):
        cursor = self.mysql_db.cursor()
        if index_column == 3:
            cursor.execute(
                """Update Culture set name='%s' where id=(select organization_id from Treaty where id=%d)""" % (
                    value, id))
            self.mysql_db.commit()
            return
        if index_column == 4:
            cursor.execute(
                """Update Culture set price=%d where id=(select organization_id from Treaty where id=%d)""" % (
                    int(value), id))
            self.mysql_db.commit()
            return
        if index_column == 12:
            cursor.execute("""
                   Update Phone_Numbers set number = '%s' where organization_id=(select Treaty.organization_id from Treaty where id=%d)
                   """ % (value, id))
            self.mysql_db.commit()
            return
        if index_column > 4:
            cursor.execute(
                """Update Organization set %s='%s' where id=(select organization_id from Treaty where id=%d)""" % (
                    self.columns_organization[index_column - 4], value, id))
            self.mysql_db.commit()
            return

        cursor.execute("UPDATE Treaty set %s='%s' where id = %d" % (self.columns_treaty[index_column], value, id))
        self.mysql_db.commit()

    Remove_Query = """
           delete from Treaty where id = %d
           """

    def removeRow(self, row: int, parent: QModelIndex = ...):
        cursor = self.mysql_db.cursor()
        cursor.execute(self.Remove_Query % self.current_indexes_list[row])

    def export(self):
        timer = QTimer(self.view)
        timer.setSingleShot(True)
        timer.timeout.connect(self.run)
        timer.start()

    def run(self, ):
        # Открываем файл
        wb = xlwt.Workbook()
        # Выбираем активный лист
        sheet = wb.add_sheet("Output")
        progress = QProgressDialog(self.view)
        progress.setMinimum(0)
        progress.setMaximum(100)
        progress.setAutoClose(True)
        progress.setVisible(True)
        progress.setValue(0)
        progress.show()
        interval = 50 / len(self.current_list[0])
        for i in range(len(self.current_list[0])):
            sheet.write(0, i, self.header[i])
            progress.setValue(int(interval * i))
            qApp.processEvents()
        new_interval = 50 / len(self.current_list)

        for i in range(len(self.current_list)):
            for j in range(len(self.current_list[i])):
                sheet.write(i + 1, j, self.current_list[i][j])
                qApp.processEvents()
            progress.setValue(int(interval + new_interval * i))
        progress.setValue(100)
        wb.save('../output.xls')
        os.system("libreoffice ../output.xls")
        qFileDialog = QFileDialog.getExistingDirectory()
        if not qFileDialog:
            os.system("rm ../output.xls")
        else:
            os.system("cp ../output.xls %s" % qFileDialog)
            os.system("rm ../output.xls")
