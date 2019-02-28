import operator
import os
from threading import Thread

from PyQt5.QtCore import QAbstractTableModel, QModelIndex, Qt
from PyQt5.QtGui import QBrush, QColor
from PyQt5.QtWidgets import QProgressDialog, QFileDialog, qApp

from admin.Settings import Settings
import mysql.connector

from admin.View.ErrorDialogView import ErrorDialogView
from admin.View.Roles import Roles
import xlrd, xlwt


class CreateUserModel(QAbstractTableModel):
    current_list = None
    current_indexes_list = None
    header = ["Имя", "Роль"]
    user_columns = ["login"]

    Select_Users = """
    SELECT id,login from Users
    """

    Select_Roles = """
    Select role_id from Roles  where user_id = %d ORDER BY role_id ASC
    """

    def __init__(self, view):
        super().__init__()
        self.view = view
        self.mysql_db = mysql.connector.connect(user='kostya05983', password='root',
                                                host=Settings.IP.value,
                                                database='farm')
        self.mysql_db.autocommit = True
        self.update_users()

    def update(self):
        self.update_users()

    def update_users(self):
        cursor = self.mysql_db.cursor()

        cursor.execute(self.Select_Users)
        logins = []
        self.current_indexes_list = []
        self.current_list = []

        for (id, login) in cursor:
            logins.append([login])
            self.current_indexes_list.append(id)

        for i in range(len(logins)):
            cursor.execute(self.Select_Roles % (self.current_indexes_list[i]))
            role = self.get_role(cursor.fetchall())
            self.current_list.append([logins[i][0], role])

    def get_role(self, roles):
        if roles.__eq__([(0,), (1,), (2,), (3,)]):
            return Roles.Owner.value
        elif roles.__eq__([(2,)]):
            return Roles.Technical_engineer.value
        elif roles.__eq__([(1,)]):
            return Roles.Lawyer.value
        elif roles.__eq__([(0,), (3,)]):
            return Roles.Technological_engineer.value
        elif roles.__eq__([(0,)]):
            return Roles.Tractor_Driver.value
        else:
            return Roles.Undifiend.value

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
            if self.check_column_value(col, value):
                self.update_data(self.current_indexes_list[row], col, value)
                self.current_list[row][col] = str(value)
                self.dataChanged.emit(index, index, (Qt.DisplayRole,))
                return True
            else:
                return False
        return False

    def check_column_value(self, column_id, value):
        if not value:
            self.show_message("Значение не должно быть пустое")
            return False
        if column_id == 1:
            if not value == Roles.Owner.value and not value == Roles.Lawyer.value \
                    and not value == Roles.Technological_engineer.value and not value == Roles.Technical_engineer.value \
                    and not value == Roles.Undifiend.value and not value == Roles.Tractor_Driver.value:
                self.show_message(
                    "Значение может быть только" + Roles.Owner.value + " " + Roles.Technical_engineer.value
                    + " " + Roles.Technological_engineer.value + " " + Roles.Undifiend.value + " " + Roles.Lawyer.value +
                    " " + Roles.Tractor_Driver.value)
                return False
        return True

    @staticmethod
    def show_message(message):
        error_dialog = ErrorDialogView(message)
        error_dialog.setModal(True)
        error_dialog.setWindowTitle("Ошибка")
        error_dialog.exec_()

    def update_data(self, id, column_index, value):
        cursor = self.mysql_db.cursor()
        if column_index == 0:
            cursor.execute("Update Users set %s='%s' where id = %d" % (self.culture_columns[column_index], value, id))
            self.mysql_db.commit()
            return
        elif column_index == 1:
            self.update_role(id, value)
            return

    Delete_Role_Query = """Delete from Roles where user_id=%d"""
    Insert_Role_Query = """insert into Roles(role_id,user_id) values(%d,%d)"""

    def update_role(self, id, value):
        cursor = self.mysql_db.cursor()
        cursor.execute(self.Delete_Role_Query % (id))
        if value == Roles.Owner.value:
            cursor.execute(self.Delete_Role_Query % (id))
            cursor.execute(self.Insert_Role_Query % (0, id))
            cursor.execute(self.Insert_Role_Query % (1, id))
            cursor.execute(self.Insert_Role_Query % (2, id))
            cursor.execute(self.Insert_Role_Query % (3, id))
        elif value == Roles.Technical_engineer.value:
            cursor.execute(self.Insert_Role_Query % (2, id))
        elif value == Roles.Lawyer.value:
            cursor.execute(self.Insert_Role_Query % (1, id))
        elif value == Roles.Technological_engineer.value:
            cursor.execute(self.Insert_Role_Query % (0, id))
            cursor.execute(self.Insert_Role_Query % (3, id))
        elif value == Roles.Tractor_Driver:
            cursor.execute(self.Insert_Role_Query % (Roles.CropRotation.value, id))

    Remove_Query = """
        delete from Users where id = %d
        """
    Remove_Roles = """
    delete from Roles where user_id=%d
    """

    def removeRow(self, row: int, parent: QModelIndex = ...):
        try:
            cursor = self.mysql_db.cursor()
            cursor.execute(self.Remove_Roles % self.current_indexes_list[row])
            cursor.execute(self.Remove_Query % self.current_indexes_list[row])
        except:
            error_dialog = ErrorDialogView("Произошла ошибка, попробуйте позже")
            error_dialog.setModal(True)
            error_dialog.setWindowTitle("Ошибка")
            error_dialog.exec_()

    def export(self):
        timer = QTimer(self.view)
        timer.setSingleShot(True)
        timer.timeout.connect(self.run)
        timer.start()

    def run(self, view):
        # Открываем файл
        wb = xlwt.Workbook()
        # Выбираем активный лист
        sheet = wb.add_sheet("Output")
        progress = QProgressDialog(view)
        progress.setMinimum(0)
        progress.setMaximum(100)
        progress.setAutoClose(True)
        progress.setVisible(True)
        progress.setValue(0)
        progress.show()
        for i in range(len(self.current_list[0])):
            sheet.write(0, i, self.header[i])
            qApp.processEvents()
        progress.setValue(50)
        for i in range(len(self.current_list)):
            for j in range(len(self.current_list[i])):
                sheet.write(i + 1, j, self.current_list[i][j])
                qApp.processEvents()
            progress.setValue(70)
        progress.setValue(100)

        wb.save('../output.xls')
        os.system("libreoffice ../output.xls")
        qFileDialog = QFileDialog.getExistingDirectory()
        if not qFileDialog:
            os.system("rm ../output.xls")
        else:
            os.system("cp ../output.xls %s" % qFileDialog)
            os.system("rm ../output.xls")
