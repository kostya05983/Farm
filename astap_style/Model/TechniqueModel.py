import operator
import os
import re
from threading import Thread
from time import sleep

import mysql.connector
import xlwt
from PyQt5.QtCore import QAbstractTableModel, QModelIndex, Qt, QThread, QEventLoop, QTimer
from PyQt5.QtGui import QBrush, QColor
from PyQt5.QtWidgets import QProgressBar, QDialog, QProgressDialog, QFileDialog, qApp
from gevent import thread
from qtconsole.qt import QtGui
from qtpy import QtCore

from admin.Settings import Settings
from admin.View.ErrorDialogView import ErrorDialogView


class TechniqueModel(QAbstractTableModel):
    current_list = None
    current_indexes_list = None
    header = ["Имя", "Дата производства", "Дата капиттального ремонта", "Дата следующего ремонта", "Состояние"]
    columns_technique = ["name", "production_date", "capital_date", "next_repair", "state"]

    def __init__(self, view):
        super().__init__()
        self.view = view
        self.mysql_db = mysql.connector.connect(user='kostya05983', password='root',
                                                host=Settings.IP.value,
                                                database='farm')
        self.mysql_db.autocommit = True
        self.get_technique()

    def get_technique(self):
        cursor = self.mysql_db.cursor()
        query = "select id,name,production_date,capital_date,next_repair,state from farm.Technique"

        cursor.execute(query)

        self.current_list = []
        self.current_indexes_list = []

        for (mysql_id, name, production_date, capital_date, next_repair, state) in cursor:
            if state == 0:
                self.current_list.append([name, production_date, capital_date, next_repair, "Сломана"])
            else:
                self.current_list.append([name, production_date, capital_date, next_repair, "В работе"])
            self.current_indexes_list.append(mysql_id)

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
            self.showMessage("Значение не может быть пустым")
            return False
        elif index_column == 1 or index_column == 2 or index_column == 3:
            if not re.fullmatch("([12]\d{3}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01]))", value):
                self.showMessage("Неверный формат даты")
                return False
        elif index_column == 4:
            if not re.fullmatch("(В работе|Сломана)", value):
                self.showMessage("Неверный формат состояние, состояние может быть В работе или Сломано")
                return False
        return True

    def showMessage(self, message):
        error_dialog = ErrorDialogView(message)
        error_dialog.setModal(True)
        error_dialog.setWindowTitle("Ошибка")
        error_dialog.exec_()

    def updateInTable(self, id, value, index_column):
        cursor = self.mysql_db.cursor()
        if index_column == 4:
            if value == "Сломана":
                cursor.execute(
                    "UPDATE Technique set %s='%s' where id=%d" % (self.columns_technique[index_column], str(0), id))

            elif value == "В работе":
                cursor.execute(
                    "UPDATE Technique set %s='%s' where id=%d" % (self.columns_technique[index_column], str(1), id))
            self.mysql_db.commit()
            return

        cursor.execute("UPDATE Technique set %s='%s' where id=%d" % (self.columns_technique[index_column], value, id))
        self.mysql_db.commit()

    Remove_Query = """
       delete from Technique where id = %d
       """

    def removeRow(self, row: int, parent: QModelIndex = ...):
        try:
            cursor = self.mysql_db.cursor()
            cursor.execute(self.Remove_Query % self.current_indexes_list[row])
        except:
            error_dialog = ErrorDialogView("Техника используется, удаление невозможно")
            error_dialog.setModal(True)
            error_dialog.setWindowTitle("Ошибка")
            error_dialog.exec_()

    currentProgress = 0

    def export(self):
        timer = QTimer(self.view)
        timer.setSingleShot(True)
        timer.timeout.connect(self.run)
        timer.start()

    def run(self):
        # loop = QEventLoop(self.view)
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
        for i in range(len(self.current_list[0])):
            sheet.write(0, i, self.header[i])
            progress.setValue(50)
            qApp.processEvents()
        for i in range(len(self.current_list)):
            for j in range(len(self.current_list[i])):
                sheet.write(i + 1, j, self.current_list[i][j])
                qApp.processEvents()
        progress.setValue(100)
        wb.save('../output.xls')
        os.system("libreoffice ../output.xls")
        qFileDialog = QFileDialog.getExistingDirectory()
        if not qFileDialog:
            os.system("rm ../output.xls")
        else:
            os.system("cp ../output.xls %s" % qFileDialog)
            os.system("rm ../output.xls")
