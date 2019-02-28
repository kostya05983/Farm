from PyQt5.QtCore import *
from qtpy import QtCore

from admin.Model.Regex import validate_number
from admin.View.AddCropRotationView import AddCropRotationView
from admin.View.ErrorDialogView import ErrorDialogView


class PlanCropRotationController(object):

    def __init__(self, view, model):
        self.view = view
        self.model = model

    def key_input_form_event(self, event):
        if event.key() == Qt.Key_Return:
            if validate_number(self.view.q_line_edit.text()) == 1:
                self.model.update(self.view.q_line_edit.text())
                if len(self.model.get_crop_rotation()) != 0:
                    self.view.clear_layout()
                    self.view.init_input_form()
                    self.view.show_table()
                    self.view.year = int(self.view.q_line_edit.text())
                else:
                    self.view.clear_layout()
                    self.view.init_input_form()
                    self.view.show_nothing()
            else:
                error_dialog = ErrorDialogView("Проверьте год")
                error_dialog.setModal(True)
                error_dialog.setWindowTitle("Ошибка")
                error_dialog.exec_()

    def add_crop_rotation_view(self):
        add_crop_rotation_view = AddCropRotationView(self.view.update_view)
        add_crop_rotation_view.setModal(True)
        add_crop_rotation_view.setWindowTitle("Ввод севооборота")
        add_crop_rotation_view.exec_()

    def key_input(self, event):
        if event.key() == Qt.Key_Delete:
            self.remove_row()
            return
        if event.key() == Qt.Key_Plus:
            self.add_crop_rotation_view()
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
