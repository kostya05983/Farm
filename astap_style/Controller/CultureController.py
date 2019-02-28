from PyQt5.QtCore import Qt
from qtpy import QtCore

from admin.View.AddCultureView import AddCultureView


class CultureController(object):

    def __init__(self, model, view):
        self.view = view
        self.model = model

    def add_culture(self):
        add_culture_view = AddCultureView(self.view.update_view)
        add_culture_view.setModal(True)
        add_culture_view.setWindowTitle("Ввод культуры")
        add_culture_view.exec_()

    def key_input(self, event):
        if event.key() == Qt.Key_Delete:
            self.remove_row()
            return
        if event.key() == Qt.Key_Plus:
            self.add_culture()
            return
        if event.key() == Qt.Key_R:
            self.view.update_view()
            return
        if event.key() == Qt.Key_E:
            self.model.export()

    def remove_row(self):
        index_list = []
        for model_index in self.view.table.selectionModel().selectedRows():
            index = QtCore.QPersistentModelIndex(model_index)
            index_list.append(index)

        for index in index_list:
            self.model.removeRow(index.row())
        self.view.update_view()
