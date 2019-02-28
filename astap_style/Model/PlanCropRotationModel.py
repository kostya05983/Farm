import operator
import os
from threading import Thread

import mysql.connector
import xlwt
from PyQt5.QtCore import QAbstractTableModel, QModelIndex, Qt, QTimer
from PyQt5.QtGui import QBrush, QColor
from PyQt5.QtWidgets import QProgressDialog, QFileDialog, qApp

from admin.Model.Regex import validate_number
from admin.Settings import Settings
from admin.View.ErrorDialogView import ErrorDialogView


class PlanCropRotationModel(QAbstractTableModel):
    current_list = []
    current_indexes_list = []
    header = ["Длина", "Ширина", "Название посева", "Засеяно", "Собрано"]
    crop_rotation_column = ["width", "height", "name", "amount_of_seed", "amount_collected"]

    Query = """select Crop_Rotation.id, Location.height,Location.width,Culture.name,Crop_Rotation.amount_of_seed,Crop_Rotation.amount_collected from Crop_Rotation
                    LEFT JOIN Location On Location.id=Crop_Rotation.location_id
                        LEFT JOIN Culture On Culture.id=Crop_Rotation.culture_id
                            where year = %s
    """

    def __init__(self, view):
        super().__init__()
        self.view = view
        self.mysql_db = mysql.connector.connect(user='kostya05983', password='root',
                                                host=Settings.IP.value,
                                                database='farm')
        self.mysql_db.autocommit = True
        self.update(2014)

    def get_crop_rotation(self):
        return self.current_list

    def update(self, year):
        cursor = self.mysql_db.cursor()
        query = self.Query % year
        cursor.execute(query)

        self.current_list = []
        self.current_indexes_list = []
        for (id, length, width, name, amount_of_seed, amount_collected) in cursor:
            if amount_collected is None:
                self.current_list.append([length, width, name, amount_of_seed, "Не собрано"])
                self.current_indexes_list.append(id)
            else:
                self.current_list.append([length, width, name, amount_of_seed, amount_collected])
                self.current_indexes_list.append(id)

    def rowCount(self, parent):
        return len(self.current_list)

    def columnCount(self, parent):
        if len(self.current_list) == 0:
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

    def validate_data(self, col, value):
        if (col <= 1 or col == 2) and not validate_number(value):
            error_dialog = ErrorDialogView("Ширина,длина,количество посеянного может быть только числом")
            error_dialog.setModal(True)
            error_dialog.setWindowTitle("Ошибка")
            error_dialog.exec_()
            return False
        return True

    def setData(self, index, value, role=Qt.EditRole):
        if index.isValid() and self.validate_data(index.column(), value):
            row = index.row()
            col = index.column()
            self.update_data(self.current_indexes_list[row], col, value)
            self.current_list[row][col] = str(value)
            self.dataChanged.emit(index, index, (Qt.DisplayRole,))
            return True
        return False

    def update_data(self, id, col, value):
        cursor = self.mysql_db.cursor()
        if col <= 1:
            cursor.execute(
                "Update Location set %s='%s' where id=(select location_id from Crop_Rotation where id=%d)" % (
                    self.crop_rotation_column[col], value, id))
        elif col == 2:
            cursor.execute("Update Culture set %s='%s' where id=(select culture_id from Crop_Rotation where id=%d)" % (
                self.crop_rotation_column[col], value, id))
        elif col >= 3:
            cursor.execute(
                "Update Crop_Rotation set %s='%s' where id = %d" % (self.crop_rotation_column[col], value, id))

    Remove_Query = """
               delete from Crop_Rotation where id = %d
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
