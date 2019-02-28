from PyQt5.QtCore import *

from admin.View.AddCropRotationView import AddCropRotationView
from admin.View.ErrorDialogView import ErrorDialogView


class PlanCropRotationController(object):

    def __init__(self, view, model):
        self.view = view
        self.model = model

    def key_input_form_event(self, event):
        if event.key() == Qt.Key_Return:
            if self.model.validate_number(self.view.q_line_edit.text()) == 1:
                self.model.update(self.view.q_line_edit.text())
                if len(self.model.get_crop_rotation()) != 0:
                    self.view.clear()
                    self.view.init_input_form()
                    self.view.show_labels()
                    self.view.show_crop_rotation()
                    self.view.init_add_button()
                else:
                    self.view.clear()
                    self.view.init_input_form()
                    self.view.show_nothing()
                    self.view.init_add_button()
            else:
                error_dialog = ErrorDialogView("Проверьте год")
                error_dialog.setModal(True)
                error_dialog.setWindowTitle("Ошибка")
                error_dialog.exec_()

    def show_add_crop_rotation_view(self):
        add_crop_rotation_view = AddCropRotationView()
        add_crop_rotation_view.setModal(True)
        add_crop_rotation_view.setWindowTitle("Ввод севооборота")
        add_crop_rotation_view.exec_()
