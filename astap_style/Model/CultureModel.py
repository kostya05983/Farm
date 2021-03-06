import os
import re
from threading import Thread

import xlwt
from PyQt5.QtCore import QAbstractTableModel, QModelIndex, Qt, QTimer
from PyQt5.QtGui import QBrush, QColor
from PyQt5.QtWidgets import QProgressDialog, QFileDialog, qApp

from admin.Settings import Settings
from admin.View.ErrorDialogView import ErrorDialogView
import mysql.connector


class CultureModel(QAbstractTableModel):
    current_list = None
    current_indexes_list = None
    header = ["Имя", "Количество", "Ценна в рублях"]
    culture_columns = ["name", "amount", "price"]

    Select_Culture = """
    SELECT id,name, amount,price from Culture
    """

    def __init__(self, view):
        super().__init__()
        self.view = view
        self.mysql_db = mysql.connector.connect(user='kostya05983', password='root',
                                                host=Settings.IP.value,
                                                database='farm')
        self.mysql_db.autocommit = True
        self.update_culture()

    def update(self):
        self.update_culture()

    def update_culture(self):
        cursor = self.mysql_db.cursor()

        cursor.execute(self.Select_Culture)
        self.current_list = []
        self.current_indexes_list = []

        for (id, name, amount, price) in cursor:
            self.current_list.append([name, amount, price])
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
        if column_id == 1:
            if not re.fullmatch("\d*", value):
                self.showMessage("Значение должно быть числом")
                return False
        return True

    def showMessage(self, message):
        error_dialog = ErrorDialogView(message)
        error_dialog.setModal(True)
        error_dialog.setWindowTitle("Ошибка")
        error_dialog.exec_()

    def update_data(self, id, column_index, value):
        cursor = self.mysql_db.cursor()

        cursor.execute("Update Culture set %s='%s' where id = %d" % (self.culture_columns[column_index], value, id))
        self.mysql_db.commit()

    Remove_Query = """
        delete from Culture where id = %d
        """

    def removeRow(self, row: int, parent: QModelIndex = ...):
        try:
            cursor = self.mysql_db.cursor()
            cursor.execute(self.Remove_Query % self.current_indexes_list[row])
        except:
            error_dialog = ErrorDialogView("Культура используется, удаление невозможно")
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
