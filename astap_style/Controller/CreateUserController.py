from PyQt5.QtCore import Qt
from qtpy import QtCore

from admin.View.AddUserView import AddUserView


class CreateUserController(object):

    def __init__(self, model, view):
        self.view = view
        self.model = model

    def add_user(self):
        add_user_view = AddUserView(self.view.update_view)
        add_user_view.setModal(True)
        add_user_view.setWindowTitle("Ввод пользователя")
        add_user_view.exec_()

    def key_input(self, event):
        if event.key() == Qt.Key_Delete:
            self.remove_row()
            return
        if event.key() == Qt.Key_Plus:
            self.add_user()
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
