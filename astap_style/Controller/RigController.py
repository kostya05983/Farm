from PyQt5.QtCore import Qt
from qtpy import QtCore

from admin.View.AddRigView import AddRigView


class RigController(object):

    def __init__(self, view, model):
        self.view = view
        self.model = model

    def show_rigs(self):
        self.model.update_locations()
        if len(self.model.get_rigs()) != 0:
            self.view.show_culture()
        else:
            self.view.show_nothing()

    def add_rig_view(self):
        add_rig_view = AddRigView(self.view.update_view)
        add_rig_view.setModal(True)
        add_rig_view.setWindowTitle("Ввод наряда")
        add_rig_view.exec_()

    def key_input(self, event):
        if event.key() == Qt.Key_Delete:
            self.remove_row()
            return
        if event.key() == Qt.Key_Plus:
            self.add_rig_view()
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
