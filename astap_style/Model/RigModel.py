import operator
import os
import re

import mysql.connector
import xlwt
from PyQt5.QtCore import QAbstractTableModel, Qt, QModelIndex, QTimer
from PyQt5.QtGui import QBrush, QColor
from PyQt5.QtWidgets import QProgressDialog, QFileDialog, qApp

from admin.Settings import Settings
from admin.View.ErrorDialogView import ErrorDialogView


class RigModel(QAbstractTableModel):
    current_list = None
    current_indexes_list = None
    header = ["Время работы в часах", "Имя", "Длина участка", "Ширина участка", "Назначена", "Дата"]
    rig_columns = ["time_work", "technique_id", "location_id", "date"]
    location_columns = ["height", "width"]

    Select_Rigs = """
    SELECT Rig.id, time_work,T.name,L.width,L.height, U.login, Rig.date
         from Rig left join  Technique T on technique_id=T.id left join Location L on location_id=L.id left join Users U 
         on user_id=U.id
    """

    def __init__(self, view):
        super().__init__()
        self.view = view
        self.mysql_db = mysql.connector.connect(user='kostya05983', password='root',
                                                host=Settings.IP.value,
                                                database='farm')
        self.mysql_db.autocommit = True
        self.update_rigs()

    def update(self):
        self.update_rigs()
        self.setData()

    def update_rigs(self):
        cursor = self.mysql_db.cursor()

        cursor.execute(self.Select_Rigs)
        self.current_list = []
        self.current_indexes_list = []

        for (id, time_work, name, width, length, user, date) in cursor:
            self.current_list.append([time_work, name, width, length, user, date])
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
            self.showMessage("Значение не должно бть пустое")
            return False
        if column_id == 0 or (column_id >= 2 and column_id < 4):
            if not re.fullmatch("\d*", value):
                self.showMessage("Значение должно быть числом")
                return False
        if column_id == 4:
            self.showMessage("Нельзя изменять имя пользователя")
            return False

        return True

    def showMessage(self, message):
        error_dialog = ErrorDialogView(message)
        error_dialog.setModal(True)
        error_dialog.setWindowTitle("Ошибка")
        error_dialog.exec_()

    UPDATE_LOCATION_QUERY = "Update Location set %s='%s' where id = (select location_id from Rig where id = %d)"
    UPDATE_TECHNIQUE_QUERY = "Update Technique set name='%s' where id = (select technique_id from Rig where id = %d)"

    def update_data(self, id, column_index, value):
        cursor = self.mysql_db.cursor()
        if column_index == 1:
            cursor.execute(self.UPDATE_TECHNIQUE_QUERY % (value, id))
            self.mysql_db.commit()
            return

        if 2 <= column_index < 4:
            cursor.execute(self.UPDATE_LOCATION_QUERY % (self.location_columns[column_index], value, id))
            self.mysql_db.commit()
            return

        if column_index == 5:
            cursor.execute("Update Rig set %s='%s' where id = %d" % (self.rig_columns[3], value, id))
            return

        cursor.execute("Update Rig set %s='%s' where id = %d" % (self.rig_columns[column_index], value, id))
        self.mysql_db.commit()

    Remove_Query = """
delete from Rig where id = %d
"""

    def removeRow(self, row: int, parent: QModelIndex = ...):
        cursor = self.mysql_db.cursor()
        cursor.execute(self.Remove_Query % self.current_indexes_list[row])

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
